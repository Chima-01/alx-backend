#!/usr/bin/env python3
"""
    This module i'll be implementing a simple
    pagination
"""


def index_range(page, page_size):
    """
        Args:
            page: index of page
            page_size: total page size
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
