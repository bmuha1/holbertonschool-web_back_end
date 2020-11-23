#!/usr/bin/env python3
"""
Unittests for client
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


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
        g = GithubOrgClient(url)
        self.assertEqual(g.org, True)
        my_mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
