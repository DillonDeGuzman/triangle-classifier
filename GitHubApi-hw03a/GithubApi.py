import requests


def get_repo_commit_counts(user_id):
    """Return repo names and commit counts for a GitHub user."""
    repo_url = f"https://api.github.com/users/{user_id}/repos?per_page=100"

    try:
        repo_response = requests.get(repo_url, timeout=10)
        repo_response.raise_for_status()
        repositories = repo_response.json()
    except requests.RequestException:
        return []

    results = []

    for repository in repositories:
        repo_name = repository["name"]

        commits_url = (
            f"https://api.github.com/repos/{user_id}/{repo_name}/commits?per_page=100"
        )

        try:
            commits_response = requests.get(commits_url, timeout=10)
            commits_response.raise_for_status()
            commits = commits_response.json()

            results.append(
                f"Repo: {repo_name} Number of commits: {len(commits)}"
            )
        except requests.RequestException:
            results.append(
                f"Repo: {repo_name} Number of commits: unavailable"
            )

    return results


def main():
    """Ask for a GitHub user ID and print repository/commit information."""
    user_id = input("Enter a GitHub user ID: ").strip()

    if not user_id:
        print("A GitHub user ID is required.")
        return

    results = get_repo_commit_counts(user_id)

    if not results:
        print("No repositories found, or GitHub could not be reached.")
        return

    for result in results:
        print(result)


if __name__ == "__main__":
    main()