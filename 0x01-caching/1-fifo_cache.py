#!/usr/bin/env python3
"""
A class FIFOCache that inherits from
BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
        a fifocahe system
    """

    def __init__(self):
        """ initialize class
        """
        super().__init__()

    def put(self, key, item):
        """ add item to cache
        """
        cache_data = self.cache_data
        if key and item:
            cache_data.update({key: item})
        if len(cache_data) > super().MAX_ITEMS:
            first = next(iter(cache_data))
            del cache_data[first]
            print(f"DISCARD: {first}")

    def get(self, key):
        """ get value by key
        """
        if key not in self.cache_data or key is None:
            return None
        return self.cache_data.get(key)
