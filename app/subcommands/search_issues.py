import click
import json

from app.subcommands.base_subcommand import BaseSubcommand
from app.common.shared_functions import initialize_api, split_fields


class SearchIssues(BaseSubcommand):
    DEFAULT_FIELDS = "summary"
    HELP_STRING = (
        "A comma separated string of Jira fields. Example: 'summary,description'"
    )

    @click.command()
    @click.option(
        "--fields", default=DEFAULT_FIELDS, show_default=True, help=HELP_STRING
    )
    @click.argument("jql", type=str)
    def command(jql, fields):
        api = initialize_api()
        field_list = split_fields(fields)
        response = api.search_issues(jql, field_list)
        response.raise_for_status()
        click.echo(json.dumps(response.json(), indent=4))
