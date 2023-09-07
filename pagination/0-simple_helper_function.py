#!/usr/bin/env python3
'''
-------------------------------------------------------------------------------
MODULE NAME = 12-log_stats
-------------------------------------------------------------------------------
DESCRIPTION:
-------------------------------------------------------------------------------
Write a function named index_range that takes two integer arguments page and
page_size.

The function should return a tuple of size two containing a start index and an
end index corresponding to the range of indexes to return in a list for those
particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.
'''
from typing import Tuple

def index_range(page, page_size) -> Tuple[int, int]:
    ''''''

    return (page * 10 if page > 1 else 0, page_size * page)
