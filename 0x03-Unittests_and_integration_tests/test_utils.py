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
        """Test the access_nested_map() from the utils module
        to ensure that the right result is returned.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",)),
            ({"a": 1}, ("a", "b")),
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path) -> Any:
        """Test that the access_nested_map() return the right exception
        when a wrong argument is passed.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


if __name__ == "__main__":
    unittest.main()
