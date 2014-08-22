from jira.client import JIRA
import click
from secret import *
import csv

jira = JIRA(options={'server': JIRA_SERVER}, basic_auth=(JIRA_USERNAME, JIRA_PASSWORD))

@click.group()
def cli1():
    pass

@cli1.command()
@click.option('--type', '-t', default='Task', help='issue type name')
@click.option('--epic', '-e', help='an epic to link to (issue id)')
@click.option('--parent', '-p', help='a parent issue to link to')
@click.option('--component', '-c', help='a component name')
@click.option('--due', '-d', help='date in format YYYY-MM-DD')
@click.option('--schedule', '-s', help='date in format YYYY-MM-DD')
@click.argument('project')
@click.argument('summary')
def create(project, component, type, due, epic, parent, summary, schedule):
    """Create an issue"""
    issue_dict = {
        'project': {'key': project},
        'issuetype': {'name': type},
        'summary': summary
    }

    if epic:
        issue_dict['customfield_10001'] = epic
    if parent:
        issue_dict['parent'] = {'id': parent}
        issue_dict['issuetype'] = {'name' : 'Sub-task'}
    if component:
        issue_dict['components'] = [{'name': component}]
    if due:
        issue_dict['duedate'] = due
    if schedule:
        issue_dict['customfield_10012'] = schedule

    new_issue = jira.create_issue(fields=issue_dict)

@cli1.command()
@click.option('--type', '-t', default='Task', help='issue type name')
@click.option('--epic', '-e', help='an epic to link to (issue KEY-ID)')
@click.option('--parent', '-p', help='a parent issue to link to')
@click.option('--component', '-c', help='a component name')
@click.option('--due', '-d', help='date in format YYYY-MM-DD')
@click.option('--schedule', '-s', help='date in format YYYY-MM-DD from csv, index on line (starting from 1), ; delimited')
@click.argument('project')
@click.argument('file')
def batch(project, component, epic, parent, due, type, file, schedule):
    """Batch create issues"""
    issue_dict = {}
    issue_dict['project'] = {'key': project}
    issue_dict['issuetype'] = {'name': type}

    if epic:
        issue_dict['customfield_10001'] = epic
    if parent:
        issue_dict['parent'] = {'id': parent}
        issue_dict['issuetype'] = {'name' : 'Sub-task'}
    if component:
        issue_dict['components'] = [{'name': component}]
    if due:
        issue_dict['duedate'] = due

    with open('tasks.txt', 'rb') as file:
        reader = csv.reader(file, delimiter=';')
        for line in reader:
            issue_dict['summary'] = line[0]
            if schedule and len(line) > int(schedule):  # ex. if at index 1, len(line) needs to be >= 2
                issue_dict['customfield_10012'] = line[int(schedule)]  # use provided index to get scheduled date
            new_issue = jira.create_issue(fields=issue_dict)
            # print issue_dict  # use to debug before actually batch creating

cli = click.CommandCollection(sources=[cli1])

if __name__ == '__main__':
    cli()