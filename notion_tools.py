from copy import deepcopy
import settings

from notion_client import Client


class NotionRepository:
    def __init__(self) -> None:
        self._connection = None

    def connect(self, token=settings.NOTION_TOKEN):
        client = Client(auth=token)
        self._connection = client

    def get_pages(self, database_id=settings.NOTION_DATABASE):
        return self._connection.databases.query(database_id=settings.NOTION_DATABASE)[
            "results"
        ]

    def get_page_name(self, page):
        return (
            page.get("properties", {})
            .get("Name", {})
            .get("title", "")[0]
            .get("text", "")
            .get("content")
        )

    def get_row(self, database, title):
        existing_row = None
        for page in database:
            if self.get_page_name(page) == title:
                existing_row = page
                break
        return existing_row

    def create_row(self, database, title, description, url):
        existing_row = self.get_row(database, title)
        if not existing_row:
            template = deepcopy(database[0])
            template["properties"].pop("Property", None)
            template["properties"].pop("Created", None)
            template["properties"].update(
                **{
                    "Name": {
                        "type": "title",
                        "title": [{"text": {"content": title}}],
                    },
                    "Description": {
                        "type": "rich_text",
                        "rich_text": [{"type": "text", "text": {"content": description[:2000]}}],
                    },
                    "URL": {
                        "type": "url",
                        "url": url,
                    },
                }
            )
            self._connection.pages.create(**template)
