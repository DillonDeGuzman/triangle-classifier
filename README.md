[![CircleCI](https://dl.circleci.com/status-badge/img/circleci/AzFYMT5aGW6W8wRBgJHgCs/16KQGiTu69EUWdTaNDwd3m/tree/HW-03b_Mocking.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/circleci/AzFYMT5aGW6W8wRBgJHgCs/16KQGiTu69EUWdTaNDwd3m/tree/HW-03b_Mocking)

# triangle-classifier

## HW 03b — Mocking GitHub API Calls

This repository contains the GitHub API homework application in the
`GitHubApi-hw03a` folder.

The `HW-03b_Mocking` branch contains unit tests that mock all calls to the
GitHub REST API. The tests use Python's `unittest.mock` module to patch
`GithubApi.requests.get`, so test execution does not make external requests
to GitHub and does not depend on GitHub API rate limits or changing repository
data.

To run the mocked tests locally:

```bash
cd GitHubApi-hw03a
python -m unittest -v TestGithubApi.py
```

The CircleCI workflow runs the same mocked tests in continuous integration.