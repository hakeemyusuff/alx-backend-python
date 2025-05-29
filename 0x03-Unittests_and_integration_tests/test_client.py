#!/usr/bin/env python3
"""Test file to test client.py"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
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


if __name__ == "__main__":
    unittest.main()
