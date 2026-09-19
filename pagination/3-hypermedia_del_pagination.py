#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return the dataset indexed by sorting position."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }

        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return deletion-resilient pagination information."""
        if index is None:
            index = 0

        assert isinstance(index, int)
        assert index >= 0
        assert index < len(self.dataset())
        assert isinstance(page_size, int)
        assert page_size > 0

        indexed_data = self.indexed_dataset()
        data = []
        current_index = index

        while (
            len(data) < page_size
            and current_index < len(self.dataset())
        ):
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
            current_index += 1

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': current_index,
        }
