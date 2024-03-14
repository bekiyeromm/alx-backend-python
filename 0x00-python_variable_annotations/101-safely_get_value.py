#!/usr/bin/env python3
"""
adding annotation to function
"""
from typing import Union, TypeVar, Any, Mapping

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    obtain dictionary using key value pair
    """
    if key in dct:
        return dct[key]
    else:
        return default
