#!/usr/bin/env python3
"""Generic utilities for github org client"""

import requests
from functools import wraps
from typing import (
    Mapping,
    Sequence,
    Dict,
    Any,
    Callable,
)


__all__ = [
    "access_nested_map",
    "get_json",
    "memoize",
]

def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """Access nested map with key path.
    Parameters
    ----------
    nested_map: Mapping
        A nested map
    path: Sequence
        A sequence of key representing a path to the value
    Example
    -------
    >>> nested_map = {"a": {"b": {"c": 1}}}
    >>> access_nested_map(nested_map, ["a", "b", "c"])
    1
    """
    
    for key in path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]
        
    return nested_map