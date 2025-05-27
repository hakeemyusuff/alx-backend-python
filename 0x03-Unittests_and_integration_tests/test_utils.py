#!/usr/bin/env python3
"""Test for the utils module"""

import unittest
from typing import Any
from parameterized import parameterized, parameterized_class

utils = __import__("utils")
access_nested_map = utils.access_nested_map

nested_map = {"a": {"b": {"c": 1}}}


class TestAccessNestedMap(unittest.TestCase):
    """The class inherits from unittest.TestCase.
    Methods:
        test_access_nested_map: Test the acess_access_nested_map function
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected) -> Any:
        """Test the access_nested_map() from the utils module"""
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
