#!/usr/bin/env python3
"""
Unittests for client
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
import client


class TestGithubOrgClient(unittest.TestCase):
    """
    Unittests for GithubOrgClient
    """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, url, my_mock):
        """
        Test GithubOrgClient.org
        """
        my_mock.return_value = True
        g = client.GithubOrgClient(url)
        self.assertEqual(g.org, True)
        my_mock.assert_called_once()

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    def test_public_repos_url(self, org):
        """
        Test _public_repos_url
        """
        url = 'https://api.github.com/orgs/{}/repos'.format(org)
        payload = {'repos_url': url}
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=payload)):
            g = client.GithubOrgClient(org)
            self.assertEqual(g._public_repos_url, url)


if __name__ == '__main__':
    unittest.main()
