
# HW-003a Develop with Testing in Mind


[![CircleCI](https://circleci.com/gh/endiesworld/codes.svg?style=svg)](https://circleci.com/gh/endiesworld/codes)

This project demonstrates how to develop with testing in mind, using GitHub API calls and unit tests with mocking.

## How to run tests

```bash
pytest test/test_fetch_user_repo.py
```

## Continuous Integration

This repository is set up with CircleCI. Every push will trigger a build and run the tests. The badge above shows the current build status for the `HW-003a` branch.

## CircleCI Setup

1. The configuration file is at `.circleci/config.yml`.
2. Enable your repository on https://circleci.com/ and follow the prompts.
3. After your first build, the badge above will show your build status.
