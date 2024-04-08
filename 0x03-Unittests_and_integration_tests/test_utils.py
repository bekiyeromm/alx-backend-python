#!/usr/bin/env python3
"""
Implement the TestAccessNestedMap.test_access_nested_map
method to test that the method
returns what it is supposed to
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ('a',), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        method to test that the method returns what it is supposed to
        args:
            nested_map:-nested map
            path:-a sequence of key representing a path to the value
            expected:-expected test result
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "KeyError: 'a'"),
        ({"a": 1}, ("a", "b"), "KeyError: 'b'")
    ])
    def test_access_nested_map_exception(
            self, nested_map, path, expected_message):
        """
        Use the assertRaises context manager to test that
        a KeyError is raised
        args:
            nested_map:-nested map (input)
            path:a sequence of key representing path to the value
            expected_message: expected out put
        """
        with self.assertRaises(KeyError) as context:
            data_item = nested_map
            for key in path:
                if isinstance(data_item, dict) and key in data_item:
                    data_item = data_item[key]
                else:
                    raise KeyError(key)
            self.assertEqual(str(context.exception), expected_message)


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Mocking the response of requests.get
        args:
            tets_url:- url
            test_payload:- expected out put
        """
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        """test the out put for the method memoiz"""
        class TestClass:

            def a_method(self):
                """return 42"""
                return 42

            @memoize
            def a_property(self):
                """calls a method one times"""
                return self.a_method()
        with patch.object(TestClass, 'a_method',
                          return_value=lambda: 42,) as mock_method:
            test_instance = TestClass()
            self.assertEqual(test_instance.a_property(), 42)
            self.assertEqual(test_instance.a_property(), 42)
            mock_method.assert_called_once()
