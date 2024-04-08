#!/usr/bin/env python3
"""
Implement the TestAccessNestedMap.test_access_nested_map
method to test that the method
returns what it is supposed to
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


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
