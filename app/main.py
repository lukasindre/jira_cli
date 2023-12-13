import click

from app.subcommands.create_issue import CreateIssue
from app.subcommands.get_issue import GetIssue
from app.subcommands.search_issues import SearchIssues
from app.subcommands.transition_issue import TransitionIssue

SUBCOMMANDS = {
    "search-issues": SearchIssues,
    "get-issue": GetIssue,
    "transition-issue": TransitionIssue,
    "create-issue": CreateIssue,
}


@click.group()
def cli():
    pass


for subcommand in SUBCOMMANDS:
    cli.add_command(SUBCOMMANDS[subcommand]().command, name=subcommand)  # type: ignore
