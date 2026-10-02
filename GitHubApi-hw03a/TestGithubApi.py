import unittest
from unittest.mock import Mock, patch
import requests

from GithubApi import get_repo_commit_counts


class TestGithubApi(unittest.TestCase):

    @patch("GithubApi.requests.get")
    def test_two_repositories_with_commits(self, mock_get):
        """Test two repositories with known numbers of commits."""
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

        self.assertEqual(get_repo_commit_counts("John567"), expected)

    @patch("GithubApi.requests.get")
    def test_user_with_no_repositories(self, mock_get):
        """Test an empty repository response."""
        repositories_response = Mock()
        repositories_response.raise_for_status.return_value = None
        repositories_response.json.return_value = []

        mock_get.return_value = repositories_response

        self.assertEqual(get_repo_commit_counts("NoReposUser"), [])

    @patch("GithubApi.requests.get")
    def test_repository_with_no_commits(self, mock_get):
        """Test that a repository with no commits returns zero."""
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

        self.assertEqual(get_repo_commit_counts("TestUser"), expected)

    @patch("GithubApi.requests.get")
    def test_github_request_error(self, mock_get):
        """Test that a request failure does not crash the function."""
        mock_get.side_effect = requests.RequestException("Network problem")

        self.assertEqual(get_repo_commit_counts("BadUser"), [])


if __name__ == "__main__":
    unittest.main()