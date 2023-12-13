import click

from app.subcommands.base_subcommand import BaseSubcommand
from app.common.shared_functions import initialize_api


def get_desired_issue_transition(issue_transitions: dict[str, str]) -> str:
    keys = "\n".join(issue_transitions.keys())
    x = input(
        f"""What status would you like to transition to:

{keys}

Selection: """
    ).strip()
    while x not in keys:
        x = input(
            f"""You have made an incorrect selection. Please choose from the options below:

{keys}

Selection: """
        ).strip()
    return x


class TransitionIssue(BaseSubcommand):
    @click.command()
    @click.argument("key", type=str)
    def command(key):
        api = initialize_api()
        response = api.get_issue_transitions(key)
        response.raise_for_status()
        transitions = {x["to"]["name"]: x["id"] for x in response.json()["transitions"]}
        desired_transition_id = transitions[get_desired_issue_transition(transitions)]
        response = api.transition_issue(key, desired_transition_id)
        response.raise_for_status()
        click.echo(f"{key} has been transitioned successfully")
        click.echo(f"{api.SITE_URL}/browse/{key}")
