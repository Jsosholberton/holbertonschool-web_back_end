#!/usr/bin/env python3
'''
-------------------------------------------------------------------------------
MODULE NAME = 0-simple_helper_function
-------------------------------------------------------------------------------
DESCRIPTION:
-------------------------------------------------------------------------------
Implement a method named get_page that takes two integer arguments page with de
fault value 1 and page_size with default value 10.

    -You have to use this CSV file (same as the one presented at the top of the
    project)
    -Use assert to verify that both arguments are integers greater than 0.
    -Use index_range to find the correct indexes to paginate the dataset correc
    tly and return the appropriate page of the dataset (i.e. the correct list o
    f rows).
    -If the input arguments are out of range for the dataset, an empty list sho
    uld be returned.
'''
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ That return a list with the values of the index"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        index: tuple = index_range(page, page_size)

        return self.dataset()[index[0]: index[1]]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    ''' That return a range of indexes '''
    return ((page_size * page) - page_size, page_size * page)
