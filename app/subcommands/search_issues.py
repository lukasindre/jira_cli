import click

from app.subcommands.base_subcommand import BaseSubcommand


class SearchIssues(BaseSubcommand):
    DEFAULT_FIELDS = ["summary"]

    @click.command()
    @click.option("--fields", default=DEFAULT_FIELDS)
    @click.argument("jql", type=str)
    def command(jql, fields):
        # TODO: do something cool here
        pass
