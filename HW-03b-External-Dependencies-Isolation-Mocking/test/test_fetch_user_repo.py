import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from unittest.mock import patch
from src.main import get_user_repos_and_commits

@patch('src.main.requests.get')
def test_get_user_repos_and_commits_success(mock_get):
	# Mock repo list response
	mock_get.side_effect = [
		# First call: repos
		MockResponse([
			{"name": "Triangle567"},
			{"name": "Square567"}
		], 200),
		# Second call: commits for Triangle567
		MockResponse([{}, {}], 200),  # 2 commits
		# Third call: commits for Square567
		MockResponse([{}, {}, {}], 200),  # 3 commits
	]
	result = get_user_repos_and_commits("John567")
	assert ("Triangle567", 2) in result
	assert ("Square567", 3) in result

@patch('src.main.requests.get')
def test_get_user_repos_and_commits_no_repos(mock_get):
	mock_get.return_value = MockResponse([], 200)
	result = get_user_repos_and_commits("NoReposUser")
	assert result == []

@patch('src.main.requests.get')
def test_get_user_repos_and_commits_repo_error(mock_get):
	# Simulate error on repo fetch
	mock_get.side_effect = Exception("API error")
	result = get_user_repos_and_commits("ErrorUser")
	assert result == []

class MockResponse:
	def __init__(self, json_data, status_code):
		self._json = json_data
		self.status_code = status_code
	def json(self):
		return self._json
	def raise_for_status(self):
		if self.status_code != 200:
			raise Exception("HTTP error")