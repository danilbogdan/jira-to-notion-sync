import settings

from jira import JIRA


class JiraRepository:
    def __init__(self) -> None:
        self._connection = None

    @staticmethod
    def get_description(issue):
        return issue.fields.description

    @staticmethod
    def get_summary(issue):
        return issue.fields.summary

    @staticmethod
    def build_url(issue):
        return f"{settings.JIRA_BASE_URL}/browse/{issue.key}"

    def connect(
        self,
        server=settings.JIRA_BASE_URL,
        username=settings.JIRA_USERNAME,
        password=settings.JIRA_PASSWORD,
    ):
        jira = JIRA(server=server, basic_auth=(username, password))
        self._connection = jira
        return jira

    def list_issues(self, search_query=settings.JIRA_DEFAULT_FILTER, **kwargs):
        issues = self._connection.search_issues(search_query, **kwargs)
        return issues
