from jira.client import JIRA
import click
from secret import *

jira = JIRA(options={'server': JIRA_SERVER}, basic_auth=(JIRA_USERNAME, JIRA_PASSWORD))
