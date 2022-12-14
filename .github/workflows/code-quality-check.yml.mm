# Github action that checks Python code quality.
# Action is fired on PR open against dev branch,
# when new commit is pushed against branch that
# has PR open to dev branch and on actual push
# to dev branch (if someone skips the PR process).

name: Run code quality checks
on:
  # pull_request_target:
  #   branches: [main]
  #   types: [opened, synchronize]
  push:
    branches:
      - main
  workflow_dispatch:
jobs:
  code-quality-check:
    name: Perform python code quality check
    #runs-on: [self-hosted, cicd-runner]
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v3
      - name: Install Python
        uses: actions/setup-python@v3
        with:
          python-version: "3.10"
      - name: Install Python code checking dependencies
        run: pip install black pylint flake8 isort
      - name: isort check
        id: isort-check
        run: isort --check-only --diff .
        continue-on-error: true
      - name: black check
        id: black-check
        run: black --diff --check $(git ls-files '*.py')
        continue-on-error: true
      - name: pylint check
        id: pylint-check
        run: pylint --disable=all --enable=unused-import $(git ls-files '*.py')
        continue-on-error: true
      - name: flake8 check
        id: flake8-check
        run: flake8 $(git ls-files '*.py')
        continue-on-error: true
      # - name: Final code quality status
      #   run: echo "::error::Blah your code quality is terrible"
      - name: Final status
        if: steps.isort-check.outcome != 'success' || steps.black-check.outcome != 'success' || steps.pylint-check.outcome != 'success' || steps.flake8-check.outcome != 'success'
        run: |
          echo ${{ steps.issort-check.outputs.stderr }}
          echo ${{ steps.issort-check.outputs.stdout }}
          exit 1