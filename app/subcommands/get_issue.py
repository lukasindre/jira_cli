import json

import click

from app.common.shared_functions import initialize_api, split_fields
from app.subcommands.base_subcommand import BaseSubcommand


class GetIssue(BaseSubcommand):
    DEFAULT_FIELDS = "summary"
    HELP_STRING = (
        "A comma separated string of Jira fields. Example: 'summary,description'"
    )

    @click.command()
    @click.option(
        "--fields", default=DEFAULT_FIELDS, help=HELP_STRING, show_default=True
    )
    @click.argument("key", type=str)
    def command(key, fields):
        api = initialize_api()
        field_list = split_fields(fields)
        response = api.get_issue(api, key, field_list)
        response.raise_for_status()
        click.echo(json.dumps(response.json(), indent=4))
