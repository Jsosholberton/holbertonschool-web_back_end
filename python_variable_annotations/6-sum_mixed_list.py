#!/usr/bin/env python3
'''
-------------------------------------------------------------------------------
MODULE NAME : 6-sum_mixed_list
-------------------------------------------------------------------------------
MODULE DESCRIPTION:
-------------------------------------------------------------------------------
    Write a type-annotated function sum_mixed_list which takes a list mxd_lst o
    f integers and floats and returns their sum as a float.
-------------------------------------------------------------------------------
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return the sum of a list"""
    return float(sum(mxd_lst))
