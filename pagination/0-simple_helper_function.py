#!/usr/bin/env python3
"""Simple helper function for pagination."""


def index_range(page: int, page_size: int) -> tuple:
    """Return start and end indexes for a pagination page."""
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
