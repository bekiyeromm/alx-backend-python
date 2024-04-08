#!/usr/bin/env python3
'''
unit Test module for clients
'''
import unittest
from typing import Dict
from unittest.mock import (
    MagicMock,
    Mock,
    PropertyMock,
    patch
)
from parameterized import parameterized, parameterized_class
from requests import HTTPError

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    '''
    Tests GithubOrgClient function
    '''
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, resp: Dict, mocked_fxn: MagicMock) -> None:
        '''
        Tests the output for org function
        '''
        mocked_fxn.return_value = MagicMock(return_value=resp)
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), resp)
        mocked_fxn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    def test_public_repos_url(self) -> None:
        '''
        Tests public_repos_url output
        '''
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
        ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @patch("client.get_json", return_value=[{"name": "holberton"}])
    def test_public_repos(self, mock_get):
        """ to unit-test GithubOrgClient.public_repos """
        with patch.object(GithubOrgClient,
                          "_public_repos_url",
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/") as mock_pub:
            test_client = GithubOrgClient("hoberton")
            test_return = test_client.public_repos()
            self.assertEqual(test_return, ["holberton"])
            mock_get.assert_called_once
            mock_pub.assert_called_once

    """ inputs to test the functionality """
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_return):
        """ to unit-test GithubOrgClient.has_license """
        test_client = GithubOrgClient("holberton")
        test_return = test_client.has_license(repo, license_key)
        self.assertEqual(expected_return, test_return)

    @parameterized_class(
        ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
        TEST_PAYLOAD
    )
    class TestIntegrationGithubOrgClient(unittest.TestCase):
        """ TESTCASE """
        @classmethod
        def setUpClass(cls):
            """ It is part of the unittest.TestCase API
            method to return example payloads found in the fixtures """
            cls.get_patcher = patch('requests.get', side_effect=HTTPError)
            cls.get_patcher.start()

        def test_public_repos(self):
            """ method to test GithubOrgClient.public_repos """
            test_class = GithubOrgClient("holberton")
            assert True

        def test_public_repos_with_license(self):
            """ method to test the public_repos with the argument license """
            test_class = GithubOrgClient("holberton")
            assert True

        @classmethod
        def tearDownClass(cls):
            """ It is part of the unittest.TestCase API
            method to stop the patcher """
            cls.get_patcher.stop()
