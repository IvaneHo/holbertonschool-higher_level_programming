#!/usr/bin/env python3
"""Custom iterator that keeps track of how many items have been iterated."""

class CountedIterator:
    def __init__(self, iterable):
        self._iter = iter(iterable)
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = next(self._iter)
        self._count += 1
        return value

    def get_count(self):
        return self._count
