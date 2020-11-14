from collections.abc import Iterator

from singleton.singleton import Singleton


class UUID(Singleton, Iterator):
    _idx = 1

    def __init__(self, start=None):
        if start is not None:
            self._idx = start

    def __iter__(self):
        return self

    def __next__(self):
        result = self._idx
        self._idx += 1
        return result
