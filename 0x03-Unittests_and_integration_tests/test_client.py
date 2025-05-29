#!/usr/bin/env python3
"""Test file to test client.py"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
import client


class TestGithubOrgClient(unittest.TestCase):
    """A class to Test GithubClient from client module"""

    @parameterized.expand(["google", "abc"])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get):
        mock_get.return_value = {"login": org_name}

        obj = client.GithubOrgClient(org_name)
        result = obj.org
        self.assertEqual(result, {"login": org_name})
        mock_get.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}",
        )

    def test_public_repos_url(self):
        """A method that test the _public_repos_url"""
        payload = {
            "login": "google",
            "id": 12345,
            "url": "www.example.com",
            "description": "Google ❤️ Open Source",
            "repos_url": "https://api.github.com/orgs/google/repos",
        }
        with patch.object(
            client.GithubOrgClient,
            "org",
            new_callable=PropertyMock,
        ) as mock_org:
            mock_org.return_value = payload

            obj = client.GithubOrgClient("google")
            result = obj._public_repos_url

            self.assertEqual(result, payload["repos_url"])
    
    def test_public_repos(self):
        """A method to test the public_repos method"""


if __name__ == "__main__":
    unittest.main()
