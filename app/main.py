import click

from app.subcommands.search_issues import SearchIssues

SUBCOMMANDS = {"search-issues": SearchIssues}


@click.group()
def cli():
    pass


for subcommand in SUBCOMMANDS:
    cli.add_command(SUBCOMMANDS[subcommand]().command, name=subcommand)
