import click

from app.subcommands.base_subcommand import BaseSubcommand
from app.common.shared_functions import initialize_api


def parse_issue_types(project_response) -> dict[str, str]:
    return {x["name"]: x["id"] for x in project_response["issueTypes"]}


def get_desired_issue_type(issue_types: dict[str, str]) -> str:
    keys = "\n".join(issue_types.keys())
    x = input(
        f"""Please select the appropriate issue type:

{keys}

Selection: """
    ).strip()
    while x not in issue_types.keys():
        x = input(
            f"""You have made an incorrect selection: {x}
Please provide a valid selection by name from the following options:

{keys}

Selection: """
        ).strip()
    return x


class CreateIssue(BaseSubcommand):
    @click.command()
    @click.argument("project", type=str)
    @click.argument("summary", type=str)
    def command(project, summary):
        api = initialize_api()
        response = api.get_issue_types_for_project(project)
        response.raise_for_status()
        project_json = response.json()
        project_id = project_json["id"]
        issue_types = parse_issue_types(project_json)
        desired_issue_type_id = issue_types[get_desired_issue_type(issue_types)]
        response = api.create_issue(project_id, desired_issue_type_id, summary)
        response.raise_for_status()
        click.echo(f"Issue created: {api.SITE_URL}/browse/{response.json()['key']}")
