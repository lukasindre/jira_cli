# Jira CLI

This CLI offers a couple useful actions to take in Jira including:
* Create Issue
* Search Issues
* Get Issue by Issue Key
* Transition Issue

To install, run the following:
```bash
git clone git@github.com:lukasindre/jira_cli.git
cd /path/to/jira_cli
poetry install
export PATH="$PATH:/path/to/jira_cli/bin"
source $HOME/.(bash_profile, zshrc, <shell_profile>)
```

Currently, the CLI will authenticate you with the following environment variables that you can set:
```bash
export JIRA_SITE_URL="https://your-site-url.atlassian.net"
export JIRA_USERNAME="foo@bar.com"
export JIRA_API_TOKEN="neener-neener-coby-fleener"
```

Things to do:
* add tests
* add easier user input options (numbers instead of typing case sensitive words)
* config file for default options, future configs
* Better guidance or process on installing the CLI
