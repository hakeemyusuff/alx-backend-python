#!/usr/bin/env python3
"""Test file to test client.py"""

from typing import Any
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, PropertyMock
import client
from fixtures import TEST_PAYLOAD


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

    @patch("client.get_json")
    def test_public_repos(self, mock_get: Mock) -> Any:
        """A method to test the public_repos method"""

        repos = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        with patch.object(
            client.GithubOrgClient,
            "_public_repos_url",
            new_callable=PropertyMock,
        ) as mock_public:
            mock_public.return_value = "http://www.example.com"
            mock_get.return_value = repos

            obj = client.GithubOrgClient("google")
            result = [repo["name"] for repo in repos]

            self.assertEqual(obj.public_repos(), result)
            mock_get.assert_called_once()
            mock_public.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(
        self,
        repo: dict,
        license_key: str,
        expected: bool,
    ) -> None:
        """Test the has_license static method with different license keys"""
        result = client.GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD,
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test class for GithubOrgClient.public_repos"""

    @classmethod
    def setUpClass(cls):
        """Set up patcher to mock requests.get with side effects"""
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        # Setup mock side_effects for requests.get().json() calls
        def side_effect(url):
            if url == "https://api.github.com/orgs/google":
                response = unittest.mock.Mock()
                response.json.return_value = cls.org_payload
                return response
            elif url == cls.org_payload["repos_url"]:
                response = unittest.mock.Mock()
                response.json.return_value = cls.repos_payload
                return response
            return None

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test that public_repos returns the correct result"""
        org_client = client.GithubOrgClient("google")
        self.assertEqual(org_client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test that public_repos filters repos by license"""
        org_client = client.GithubOrgClient("google")
        self.assertEqual(
            org_client.public_repos(license="apache-2.0"),
            self.apache2_repos,
        )


if __name__ == "__main__":
    unittest.main()
