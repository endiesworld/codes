import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.main import get_user_repos_and_commits

def test_get_user_repos_and_commits_real_user():
    user_id = "richkempinski"
    result = get_user_repos_and_commits(user_id)
    assert isinstance(result, list)
    assert all(isinstance(repo, tuple) and len(repo) == 2 for repo in result)
    assert len(result) > 0
    repo_names = [r[0] for r in result]
    assert "hellogitworld" in repo_names

def test_get_user_repos_and_commits_nonexistent_user():
    user_id = "thisuserdoesnotexist1234567890"
    result = get_user_repos_and_commits(user_id)
    assert result == []