from os import environ
from typing import Any, Union
from urllib.parse import urljoin

import requests


class JiraApi:
    SITE_URL = environ["JIRA_SITE_URL"]

    def __init__(self):
        self.s = requests.Session()
        self.s.auth = (environ["JIRA_USERNAME"], environ["JIRA_API_TOKEN"])
        self.s.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def get_issue(self, issue_key: str, fields: list[str]) -> requests.models.Response:
        return self._get(
            path=f"/rest/api/3/issue/{issue_key}", params={"fields": fields}
        )

    def search_issues(self, jql: str, fields: list[str]) -> requests.models.Response:
        return self._post(
            path="/rest/api/3/search", params={"fields": fields}, json={"jql": jql}
        )

    def get_issue_types_for_project(self, project: str) -> requests.models.Response:
        return self._get(
            path=f"/rest/api/3/project/{project}", params={"expand": ["issueTypes"]}
        )

    def create_issue(
        self, project_id: str, issue_type_id: str, summary: str
    ) -> requests.models.Response:
        return self._post(
            path="/rest/api/3/issue",
            json={
                "summary": summary,
                "project": {"id": project_id},
                "issuetype": {"id": issue_type_id},
            },
        )

    def get_issue_transitions(self, issue_key: str) -> requests.models.Response:
        return self.s.get(f"/rest/api/3/{issue_key}/transitions")

    def transition_issue(self, issue_key: str, transition_id: str) -> requests.models.Response:
        return self.s.post(f"/rest/api/3/{issue_key}/transitions", json={"transition": {"id": transition_id}})

    def _get(
        self, path: str, params: Union[dict[str, Any] | None] = None
    ) -> requests.models.Response:
        return self.s.get(url=self._url(path), params=params)

    def _post(
        self,
        path: str,
        params: Union[dict[str, Any] | None] = None,
        json: Union[dict[str, Any] | None] = None,
    ) -> requests.models.Response:
        return self.s.post(url=self._url(path), params=params, json=json)

    def _url(self, path: str):
        return urljoin(self.SITE_URL, path)
