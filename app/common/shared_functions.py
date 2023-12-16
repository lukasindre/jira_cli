from app.api.jira_api import JiraApi


def initialize_api() -> JiraApi:
    """Initialize an instance of the JiraApi class."""
    return JiraApi()


def split_fields(fields: str) -> list[str]:
    """Split a string on commas.

    Keyword arguments:
    fields -- a string of fields separated by commas
    """
    return fields.split(",")
