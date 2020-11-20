#!/usr/bin/env python3
"""
Unittests for utils
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, requests


class TestAccessNestedMap(unittest.TestCase):
    """
    Unittests for nested map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, map):
        """
        Test access nested map
        """
        self.assertEqual(access_nested_map(nested_map, path), map)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test access nested map exception
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Unittests for get json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """
        Test get json
        """
        my_mock = unittest.mock.Mock()
        my_mock.json.return_value = payload
        with patch('requests.get', return_value=my_mock):
            my_json = get_json(url)
            my_mock.json.assert_called_once()
            self.assertEqual(my_json, payload)


if __name__ == '__main__':
    unittest.main()
