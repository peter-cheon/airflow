# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# NOTE! THIS FILE IS AUTOMATICALLY GENERATED AND WILL BE OVERWRITTEN!
#
# IF YOU WANT TO MODIFY THIS FILE, YOU SHOULD MODIFY THE TEMPLATE
# `get_provider_info_TEMPLATE.py.jinja2` IN the `dev/breeze/src/airflow_breeze/templates` DIRECTORY


def get_provider_info():
    return {
        "package-name": "apache-airflow-providers-slack",
        "name": "Slack",
        "description": "`Slack <https://slack.com/>`__ services integration including:\n\n  - `Slack API <https://api.slack.com/>`__\n  - `Slack Incoming Webhook <https://api.slack.com/messaging/webhooks>`__\n",
        "integrations": [
            {
                "integration-name": "Slack",
                "external-doc-url": "https://slack.com/",
                "logo": "/docs/integration-logos/Slack.png",
                "tags": ["service"],
            },
            {
                "integration-name": "Slack API",
                "external-doc-url": "https://api.slack.com/",
                "how-to-guide": ["/docs/apache-airflow-providers-slack/operators/slack_api.rst"],
                "tags": ["service"],
            },
            {
                "integration-name": "Slack Incoming Webhook",
                "external-doc-url": "https://api.slack.com/messaging/webhooks",
                "how-to-guide": ["/docs/apache-airflow-providers-slack/operators/slack_webhook.rst"],
                "tags": ["service"],
            },
        ],
        "operators": [
            {"integration-name": "Slack API", "python-modules": ["airflow.providers.slack.operators.slack"]},
            {
                "integration-name": "Slack Incoming Webhook",
                "python-modules": ["airflow.providers.slack.operators.slack_webhook"],
            },
        ],
        "hooks": [
            {"integration-name": "Slack API", "python-modules": ["airflow.providers.slack.hooks.slack"]},
            {
                "integration-name": "Slack Incoming Webhook",
                "python-modules": ["airflow.providers.slack.hooks.slack_webhook"],
            },
        ],
        "transfers": [
            {
                "source-integration-name": "Common SQL",
                "target-integration-name": "Slack",
                "python-module": "airflow.providers.slack.transfers.base_sql_to_slack",
            },
            {
                "source-integration-name": "Common SQL",
                "target-integration-name": "Slack API",
                "python-module": "airflow.providers.slack.transfers.sql_to_slack",
                "how-to-guide": "/docs/apache-airflow-providers-slack/operators/sql_to_slack.rst",
            },
            {
                "source-integration-name": "Common SQL",
                "target-integration-name": "Slack Incoming Webhook",
                "python-module": "airflow.providers.slack.transfers.sql_to_slack_webhook",
                "how-to-guide": "/docs/apache-airflow-providers-slack/operators/sql_to_slack_webhook.rst",
            },
        ],
        "connection-types": [
            {"hook-class-name": "airflow.providers.slack.hooks.slack.SlackHook", "connection-type": "slack"},
            {
                "hook-class-name": "airflow.providers.slack.hooks.slack_webhook.SlackWebhookHook",
                "connection-type": "slackwebhook",
            },
        ],
        "notifications": [
            "airflow.providers.slack.notifications.slack.SlackNotifier",
            "airflow.providers.slack.notifications.slack_webhook.SlackWebhookNotifier",
        ],
    }
