#!/usr/bin/env python3
"""
    Class MRUCache (most recently used)
    inherits from BaseCaching and is a caching system
"""
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """ initialize a class
    """

    def __init__(self):
        super().__init__()
        self.cache_copy = self.cache_data.copy()

    def put(self, key, item):
        """ add to catch system
        """
        cache = self.cache_data
        if key and item:
            if len(cache) + 1 > BaseCaching.MAX_ITEMS:
                mru = self.get_mru(None)
                del cache[mru]
                print(f"DISCARD: {mru}")
            self.cache_copy[key] = item
            cache[key] = item

    def get(self, key):
        """ get item from key
        """
        if key is not None:
            self.get_mru(key)
        return self.cache_data.get(key)

    def get_mru(self, key):
        """ implement a mru cache system
        """
        cache_copy = self.cache_copy
        if key is None:
            return cache_copy.popitem()[0]
        elif key in cache_copy:
            item = cache_copy.get(key)
            del cache_copy[key]
            cache_copy[key] = item
