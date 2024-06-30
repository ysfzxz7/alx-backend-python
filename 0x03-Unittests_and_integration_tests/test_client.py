#!/usr/bin/env python3
"""
    Module that contains test on test_client Module
"""
import unittest
from unittest.mock import Mock, patch, PropertyMock, call
from parameterized import parameterized, parameterized_class
import client
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
        TestGithubOrgClient class that inherits from unittest.TestCase
    """

    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, get_patch):
        """
            Method that tests the GithubOrgClient.org() Method
        """
        get_patch.return_value = expected
        instance = GithubOrgClient(org)
        self.assertEqual(instance.org, expected)
        get_patch.assert_called_once_with(
            f'https://api.github.com/orgs/{org}'
        )

    def test_public_repos_url(self):
        """
            Method that tests the GithubOrgClient._public_repos_url Method
        """
        expected = "abdelemjidessaid"
        payload = {"repos_url": expected}
        mocked_method = 'client.GithubOrgClient.org'
        with patch(mocked_method, PropertyMock(return_value=payload)):
            client = GithubOrgClient('heroshima')
            self.assertEqual(client._public_repos_url, expected)

    @patch('client.get_json')
    def test_public_repos(self, get_json_mock):
        """
            Method that tests the GithubOrgClient.public_repos Method
        """
        abdo = {"name": "Abdo", "license": {"key": "a"}}
        ess = {"name": "Ess", "license": {"key": "b"}}
        user = {"name": "User"}
        to_mock = 'client.GithubOrgClient._public_repos_url'
        get_json_mock.return_value = [abdo, ess, user]
        with patch(
            to_mock, PropertyMock(return_value="abdelemjidessaid")
        ) as y:
            heroshima = GithubOrgClient("heroshima")
            self.assertEqual(
                heroshima.public_repos(), ['Abdo', 'Ess', 'User']
            )
            self.assertEqual(heroshima.public_repos("a"), ['Abdo'])
            self.assertEqual(heroshima.public_repos("c"), [])
            self.assertEqual(heroshima.public_repos(45), [])
            get_json_mock.assert_called_once_with("abdelemjidessaid")
            y.assert_called_once_with()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo, license, expected):
        """
            Test the license checker
        """
        self.assertEqual(GithubOrgClient.has_license(repo, license), expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
        class TestIntegrationGithubOrgClient inherits from unittest.TestCase
    """

    @classmethod
    def setUpClass(cls):
        """ prepare for testing """
        org = TEST_PAYLOAD[0][0]
        repos = TEST_PAYLOAD[0][1]
        org_mock = Mock()
        org_mock.json = Mock(return_value=org)
        cls.org_mock = org_mock
        repos_mock = Mock()
        repos_mock.json = Mock(return_value=repos)
        cls.repos_mock = repos_mock

        cls.get_patcher = patch('requests.get')
        cls.get = cls.get_patcher.start()

        options = {cls.org_payload["repos_url"]: repos_mock}
        cls.get.side_effect = lambda y: options.get(y, org_mock)

    @classmethod
    def tearDownClass(cls):
        """ unprepare for testing """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ public repos test """
        y = GithubOrgClient("x")
        self.assertEqual(y.org, self.org_payload)
        self.assertEqual(y.repos_payload, self.repos_payload)
        self.assertEqual(y.public_repos(), self.expected_repos)
        self.assertEqual(y.public_repos("NONEXISTENT"), [])
        self.get.assert_has_calls([call("https://api.github.com/orgs/x"),
                                   call(self.org_payload["repos_url"])])

    def test_public_repos_with_license(self):
        """ public repos test """
        y = GithubOrgClient("x")
        self.assertEqual(y.org, self.org_payload)
        self.assertEqual(y.repos_payload, self.repos_payload)
        self.assertEqual(y.public_repos(), self.expected_repos)
        self.assertEqual(y.public_repos("NONEXISTENT"), [])
        self.assertEqual(y.public_repos("apache-2.0"), self.apache2_repos)
        self.get.assert_has_calls([call("https://api.github.com/orgs/x"),
                                   call(self.org_payload["repos_url"])])
