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

    @patch('client.get_json')
    def test_public_repos(self, my_mock):
        """
        Test public_repos
        """
        return_value = [{'name': 'google'}, {'name': 'abc'}]
        my_mock.return_value = return_value
        with patch('client.GithubOrgClient._public_repos_url',
                   PropertyMock(return_value=return_value)) as public:
            g = client.GithubOrgClient('test')
            self.assertEqual(g.public_repos(), ['google', 'abc'])
            my_mock.assert_called_once()
            public.assert_called_once()


if __name__ == '__main__':
    unittest.main()
