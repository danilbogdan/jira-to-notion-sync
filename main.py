from notion_tools import NotionRepository
from jira_tools import JiraRepository


if __name__ == "__main__":
    j = JiraRepository()
    n = NotionRepository()
    j.connect()
    n.connect()
    issues = j.list_issues()
    notion_database = n.get_pages()

    for issue in issues:
        n.create_row(
            database=notion_database,
            title=j.get_summary(issue),
            description=j.get_description(issue),
            url=j.build_url(issue),
        )
