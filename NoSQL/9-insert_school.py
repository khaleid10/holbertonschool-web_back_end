#!/usr/bin/env python3
"""Module for inserting a school document into MongoDB."""


def insert_school(mongo_collection, **kwargs):
    """Insert a new school document and return its new ID."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
