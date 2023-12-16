import click

from app.common.shared_functions import initialize_api
from app.subcommands.base_subcommand import BaseSubcommand


def parse_issue_types(project_response) -> dict[str, str]:
    """Parse issue type response for a project.

    Keyword arguments:
    project_response -- API response for getting a Jira project
        by its key.

    Returns dict[str, str].
    """
    return {x["name"]: x["id"] for x in project_response["issueTypes"]}


def get_desired_issue_type(issue_types: dict[str, str]) -> str:
    """Get user input for desired issue type.

    Keyword arguments:
    issue_types: dict[str, str] -- a dict of issue type names to their IDs.

    Returns a string
    """
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
        """Create Issue Command.

        Keyword arguments:
        project: str -- the key of the project you want to create the
            issue in.
        summary: str -- the summary of the issue
        """
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
