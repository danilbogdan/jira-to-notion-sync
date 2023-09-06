import dotenv
import os

dotenv.load_dotenv()


JIRA_BASE_URL = os.environ.get('JIRA_BASE_URL')
JIRA_USERNAME = os.environ.get('JIRA_USERNAME')
JIRA_PASSWORD = os.environ.get('JIRA_PASSWORD')
JIRA_DEFAULT_FILTER = "filter=13022"

NOTION_TOKEN = os.environ.get('NOTION_TOKEN')
NOTION_DATABASE = os.environ.get('NOTION_DATABASE')
