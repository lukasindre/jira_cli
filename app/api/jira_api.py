from os import environ
from typing import Any, Union
from urllib.parse import urljoin

import requests


class JiraApi:
    SITE_URL = environ["JIRA_SITE_URL"]

    def __init__(self):
        """Initialize the API Client."""
        self.s = requests.Session()
        self.s.auth = (environ["JIRA_USERNAME"], environ["JIRA_API_TOKEN"])
        self.s.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def get_issue(self, issue_key: str, fields: list[str]) -> requests.models.Response:
        """Retrieve a Jira issue.

        Keyword arguments:
        issue_key: str -- the issue key of the issue you want.
        fields: list[str] -- a list of strings that represent the fields you want to be
            displayed.

        Returns a requests.models.Response object.
        """
        return self._get(
            path=f"/rest/api/3/issue/{issue_key}", params={"fields": fields}
        )

    def search_issues(self, jql: str, fields: list[str]) -> requests.models.Response:
        """Search issues via jql.

        Keyword arguments:
        jql: str -- a JQL string to search Jira by.
        fields: list[str] -- a string list of fields you want to be displayed.

        Returns a requests.models.Response object.
        """
        return self._post(
            path="/rest/api/3/search", params={"fields": fields}, json={"jql": jql}
        )

    def get_issue_types_for_project(self, project: str) -> requests.models.Response:
        """Get the available issue types for a Project.

        Keyword arguments:
        project: str -- the key of the jira project.

        Returns a requests.models.Response object.
        """
        return self._get(
            path=f"/rest/api/3/project/{project}", params={"expand": ["issueTypes"]}
        )

    def create_issue(
        self, project_id: str, issue_type_id: str, summary: str
    ) -> requests.models.Response:
        """Creates a Jira issue.

        Keyword arguments:
        project_id: str -- the ID of the project you want to create the ticket
            under.
        issue_type_id: str -- the issue type ID you'd like the ticket to have.
        summary: str -- the summary of the ticket.

        Returns a requests.models.Response object.
        """
        return self._post(
            path="/rest/api/3/issue",
            json={
                "fields": {
                    "summary": summary,
                    "project": {"id": project_id},
                    "issuetype": {"id": issue_type_id},
                }
            },
        )

    def get_issue_transitions(self, issue_key: str) -> requests.models.Response:
        """Get available transitions for an issue.

        Keyword arguments:
        issue_key: str -- the key of the issue you want to transition.

        Returns requests.models.Response object
        """
        return self._get(f"/rest/api/3/issue/{issue_key}/transitions")

    def transition_issue(
        self, issue_key: str, transition_id: str
    ) -> requests.models.Response:
        """Transition an issue.

        Keyword arguments:
        issue_key: str -- the key of the issue you want to transition.
        transition_id: str -- the id of the transition you want to use against
            the issue.

        Returns a requests.models.Response object.
        """
        return self._post(
            f"/rest/api/3/issue/{issue_key}/transitions",
            json={"transition": {"id": transition_id}},
        )

    def _get(
        self, path: str, params: Union[dict[str, Any] | None] = None
    ) -> requests.models.Response:
        """HTTP GET request.

        Keyword arguments:
        path: str -- the path of the http request.
        params: Union[dict[str, Any] | None] -- query parameters of
            the GET request (default = None).

        Returns a requests.models.Response object.
        """
        return self.s.get(url=self._url(path), params=params)

    def _post(
        self,
        path: str,
        params: Union[dict[str, Any] | None] = None,
        json: Union[dict[str, Any] | None] = None,
    ) -> requests.models.Response:
        """HTTP POST request.

        Keyword arguments:
        path: str -- the path of the http request.
        params: Union[dict[str, Any] | None] -- query parameters of
            the GET request (default = None).
        json: Union[dict[str, Any] | None] -- json body of
            the POST request (default = None).

        Returns a requests.models.Response object.
        """
        return self.s.post(url=self._url(path), params=params, json=json)

    def _url(self, path: str) -> str:
        """Return absolute URI.

        Keyword arguments:
        path: str -- the path of the request.

        Returns a string.
        """
        return urljoin(self.SITE_URL, path)
