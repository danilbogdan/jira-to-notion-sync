# Jira to Notion Sync

This Python script allows you to sync Jira issues with a Notion database.

## Table of Contents
- [Introduction](#introduction)
- [Usage](#usage)
- [Requirements](#requirements)
- [Configuration](#configuration)
- [License](#license)

## Introduction

The `Jira to Notion Sync` script is designed to connect to your Jira instance, retrieve a list of issues based on a specified Jira filter, and then create corresponding entries in a Notion database. This can be useful for keeping track of Jira issues in a Notion workspace for better project management and collaboration.

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/danilbogdan/jira_to_notion.git
   ```

2. Install the required Python packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. Set the `.env` file with your Jira and Notion credentials and configurations.

4. Run the script:

   ```bash
   python3 main.py
   ```

The script will connect to your Jira instance, fetch issues from the specified filter, and create corresponding entries in your Notion database.

## Requirements

- Python 3.x
- Jira account with API access
- Notion account with API access

## Configuration

Before running the script, you need to configure it by updating the `settings.py` file. Here's what you need to configure:

- Jira Configuration:
  - `JIRA_BASE_URL`: The base URL of your Jira instance.
  - `JIRA_USERNAME`: Your Jira username.
  - `JIRA_PASSWORD`: Your Jira password or API token.

- Notion Configuration:
  - `NOTION_TOKEN`: Your Notion API token.
  - `NOTION_DATABASE`: The ID of your Notion database where you want to create entries.

- Jira Filter:
  - `JIRA_FILTER`: The Jira filter ID or query to specify which issues to sync.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

You should place this README in the root of your project directory and make sure to update any placeholders with actual values and descriptions. Additionally, ensure that you have the required dependencies installed and properly configured before running the script.
