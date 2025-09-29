
import requests

def get_user_repos_and_commits(user_id: str) -> list[tuple[str, int]]:
    """
    Given a GitHub user ID, returns a list of tuples (repo_name, num_commits)
    """
    repos_url = f"https://api.github.com/users/{user_id}/repos"
    try:
        repos_response = requests.get(repos_url)
        repos_response.raise_for_status()
        repos = repos_response.json()
    except Exception as e:
        print(f"Error fetching repos for user {user_id}: {e}")
        return []

    result = []
    for repo in repos:
        repo_name = repo.get("name")
        if not repo_name: 
            continue
        commits_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
        try:
            commits_response = requests.get(commits_url)
            commits_response.raise_for_status()
            commits = commits_response.json()
            num_commits = len(commits)
        except Exception as e:
            print(f"Error fetching commits for repo {repo_name}: {e}")
            num_commits = 0
        result.append((repo_name, num_commits))
    return result

def main():
    user_id = input("Enter GitHub user ID: ")
    repo_commits = get_user_repos_and_commits(user_id)
    for repo, count in repo_commits:
        print(f"Repo: {repo} Number of commits: {count}")


if __name__ == "__main__":
    main()
