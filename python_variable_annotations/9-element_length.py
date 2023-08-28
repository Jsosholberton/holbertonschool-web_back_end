#!/usr/bin/env python3
'''
-------------------------------------------------------------------------------
MODULE NAME : 8-element_length
-------------------------------------------------------------------------------
MODULE DESCRIPTION:
-------------------------------------------------------------------------------
    Annotate the below function's parameters and return values with the appropr
    iate types
-------------------------------------------------------------------------------
'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return any"""
    return [(i, len(i)) for i in lst]
