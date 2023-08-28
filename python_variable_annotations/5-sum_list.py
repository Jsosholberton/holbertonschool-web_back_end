#!/usr/bin/env python3
'''
-------------------------------------------------------------------------------
MODULE NAME : 5-sum_list
-------------------------------------------------------------------------------
MODULE DESCRIPTION:
-------------------------------------------------------------------------------
    Write a type-annotated function sum_list which takes a list input_list of f
    loats as argument and returns their sum as a float.
-------------------------------------------------------------------------------
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    """return the sum of a list of floats"""
    return sum([a for a in input_list])
