import click

from app.subcommands.create_issue import CreateIssue
from app.subcommands.get_issue import GetIssue
from app.subcommands.search_issues import SearchIssues
from app.subcommands.transition_issue import TransitionIssue

# Dict of subcommands to their respective classes to load
# into the CLI later
SUBCOMMANDS = {
    "search-issues": SearchIssues,
    "get-issue": GetIssue,
    "transition-issue": TransitionIssue,
    "create-issue": CreateIssue,
}


# start group context for the CLI
@click.group()
def cli():
    pass


# load each subcommand's command function into the CLI group object
for subcommand in SUBCOMMANDS:
    cli.add_command(SUBCOMMANDS[subcommand]().command, name=subcommand)  # type: ignore
