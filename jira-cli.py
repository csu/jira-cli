from jira.client import JIRA
import click
from secret import *

jira = JIRA(options={'server': JIRA_SERVER}, basic_auth=(JIRA_USERNAME, JIRA_PASSWORD))

@click.group()
def cli1():
    pass

@cli1.command()
# @click.option('--project', '-p', default='PER', help='project key')
@click.option('--type', '-t', default='Task', help='issue type name')
@click.option('--epic', '-e', help='an epic to link to (issue id)')
@click.option('--component', '-c', help='a component name')
@click.argument('project')
@click.argument('summary')
def create(project, component, type, epic, summary):
    """Create an issue"""
    issue_dict = {
        'project': {'key': project},
        'issuetype': {'name': type},
        'summary': summary,
    }
    if epic:
        issue_dict['customfield_10001'] = epic
    if component:
        issue_dict['components'] = [{'name': component}]
    new_issue = jira.create_issue(fields=issue_dict)

@cli1.command()
# @click.option('--project', '-p', default='PER', help='project key')
@click.option('--type', '-t', default='Task', help='issue type name')
@click.option('--epic', '-e', help='an epic to link to (issue id)')
@click.option('--component', '-c', help='a component name')
@click.argument('project')
@click.argument('file')
def batch(project, component, epic, type, file):
    issue_dict = {}
    issue_dict['project'] = {'key': project}
    issue_dict['issuetype'] = {'name': type}
    if epic:
        issue_dict['customfield_10001'] = epic
    if component:
        issue_dict['components'] = [{'name': component}]

    with open(file) as f:
        content = f.readlines()

    for line in content:
        issue_dict['summary'] = line
        new_issue = jira.create_issue(fields=issue_dict)

cli = click.CommandCollection(sources=[cli1])

if __name__ == '__main__':
    cli()