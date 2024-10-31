#!/usr/bin/env python3
"""
    Class LRUCache (least recently used)
    inherits from BaseCaching and is a caching system
"""
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
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
            self.cache_copy[key] = item
            cache[key] = item
            if len(cache) > BaseCaching.MAX_ITEMS:
                lru = self.get_lru(None)
                del cache[lru]
                del self.cache_copy[lru]
                print(f"DISCARD: {lru}")

    def get(self, key):
        """ get item from key
        """
        if key is not None:
            self.get_lru(key)
        return self.cache_data.get(key)

    def get_lru(self, key):
        """ implement a lru cache system
        """
        cache = self.cache_copy
        if key is None:
            return next(iter(cache))
        elif key in cache:
            item = cache.get(key)
            del cache[key]
            cache[key] = item
