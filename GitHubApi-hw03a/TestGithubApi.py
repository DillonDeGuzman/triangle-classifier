import unittest
from unittest.mock import Mock, patch
import requests

from GithubApi import get_repo_commit_counts


class TestGithubApi(unittest.TestCase):
    """Unit tests that mock all GitHub API requests."""

    @patch("GithubApi.requests.get")
    def test_two_repositories_with_commits(self, mock_get):
        """Return known repository names and known commit totals."""
        repositories_response = Mock()
        repositories_response.raise_for_status.return_value = None
        repositories_response.json.return_value = [
            {"name": "Triangle567"},
            {"name": "Square567"}
        ]

        triangle_commits_response = Mock()
        triangle_commits_response.raise_for_status.return_value = None
        triangle_commits_response.json.return_value = [
            {"sha": "commit1"},
            {"sha": "commit2"},
            {"sha": "commit3"}
        ]

        square_commits_response = Mock()
        square_commits_response.raise_for_status.return_value = None
        square_commits_response.json.return_value = [
            {"sha": "commit1"},
            {"sha": "commit2"}
        ]

        mock_get.side_effect = [
            repositories_response,
            triangle_commits_response,
            square_commits_response
        ]

        expected = [
            "Repo: Triangle567 Number of commits: 3",
            "Repo: Square567 Number of commits: 2"
        ]

        actual = get_repo_commit_counts("John567")

        self.assertEqual(actual, expected)
        self.assertEqual(mock_get.call_count, 3)

    @patch("GithubApi.requests.get")
    def test_user_with_no_repositories(self, mock_get):
        """Return an empty result for a user with no repositories."""
        repositories_response = Mock()
        repositories_response.raise_for_status.return_value = None
        repositories_response.json.return_value = []

        mock_get.return_value = repositories_response

        actual = get_repo_commit_counts("NoReposUser")

        self.assertEqual(actual, [])
        self.assertEqual(mock_get.call_count, 1)

    @patch("GithubApi.requests.get")
    def test_repository_with_no_commits(self, mock_get):
        """Return zero for a repository whose mock commit list is empty."""
        repositories_response = Mock()
        repositories_response.raise_for_status.return_value = None
        repositories_response.json.return_value = [
            {"name": "EmptyRepository"}
        ]

        commits_response = Mock()
        commits_response.raise_for_status.return_value = None
        commits_response.json.return_value = []

        mock_get.side_effect = [
            repositories_response,
            commits_response
        ]

        expected = [
            "Repo: EmptyRepository Number of commits: 0"
        ]

        actual = get_repo_commit_counts("TestUser")

        self.assertEqual(actual, expected)
        self.assertEqual(mock_get.call_count, 2)

    @patch("GithubApi.requests.get")
    def test_request_error_returns_empty_list(self, mock_get):
        """Handle a mocked GitHub or network request error."""
        mock_get.side_effect = requests.RequestException("Mocked network problem")

        actual = get_repo_commit_counts("BadUser")

        self.assertEqual(actual, [])
        self.assertEqual(mock_get.call_count, 1)


if __name__ == "__main__":
    unittest.main()