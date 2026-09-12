#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination module."""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset of popular baby names."""
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
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }

        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict:
        """Return a deletion-resilient page using dataset indexes."""
        assert type(index) is int
        assert type(page_size) is int
        assert index >= 0
        assert index < len(self.indexed_dataset())

        indexed_dataset = self.indexed_dataset()
        data = []
        next_index = index

        for item in range(page_size):
            while indexed_dataset.get(next_index) is None:
                next_index += 1

            data.append(indexed_dataset.get(next_index))
            next_index += 1

        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index
        }
