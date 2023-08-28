#!/usr/bin/env python3
'''
-------------------------------------------------------------------------------
MODULE NAME : 8-make_multiplier
-------------------------------------------------------------------------------
MODULE DESCRIPTION:
-------------------------------------------------------------------------------
    Write a type-annotated function make_multiplier that takes a float multipli
    er as argument and returns a function that multiplies a float by multiplier
-------------------------------------------------------------------------------
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that return a float"""
    def multiplier_func(x: float) -> float:
        """Return the result"""
        return x * multiplier
    return multiplier_func
