jira-cli
========

A command line interface for JIRA.

## Usage
### `create <PROJECT> "<Issue Summary>"`
Creates a new issue

#### Options
* `--type` (or `-t`): specify an issue type
* `--epic` (or `-e`): link to an epic (ex. PRO-123)
* `--parent` (or `-p`): make the subtask of a parent (ex. PRO-123)
* `--component` (or `-c`): add to a component
* `--due` (or `-d`): add a due date (YYYY-MM-DD)

### `batch <PROJECT> <file-name.txt>`
Creates issues from a file. Issues separated by line. Other fields separated by semicolons.

#### Options
* `--type` (or `-t`): specify an issue type
* `--epic` (or `-e`): link to an epic (ex. PRO-123)
* `--parent` (or `-p`): make the subtask of a parent (ex. PRO-123)
* `--component` (or `-c`): add to a component
* `--due` (or `-d`): add a due date (YYYY-MM-DD)
