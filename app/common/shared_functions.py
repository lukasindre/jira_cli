from app.api.jira_api import JiraApi


def initialize_api() -> JiraApi:
    return JiraApi()


def split_fields(fields: str) -> list[str]:
    return fields.split(",")
