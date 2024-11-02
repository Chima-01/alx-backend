#!/usr/bin/env python3
"""
    This module i'll be implementing a simple
    pagination
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """
        Args:
            page: index of page
            page_size: total page size
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


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
        """get page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        data_set = self.dataset()
        size = len(data_set)
        if start > size or end > size:
            return []
        else:
            return data_set[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ implement Hypermedia pagination
        """
        data = self.get_page(page, page_size)
        size = math.ceil(len(self.__dataset) / page_size)
        next_page = None if (page + 1) => size else page + 1
        prev_page = None if (page - 1) < 1 else page - 1
        return {
                "page_size": len(data),
                "page": page,
                "data": data,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_page": size
                }
