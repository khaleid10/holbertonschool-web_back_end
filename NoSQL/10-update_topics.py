#!/usr/bin/env python3
"""Module for updating school topics in MongoDB."""


def update_topics(mongo_collection, name, topics):
    """Update topics of all school documents matching the given name."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
