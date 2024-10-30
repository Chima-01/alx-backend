#!/usr/bin/env python3
"""
    Aclass LIFOCache that inherits from
    BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    class to implement lifocaching system
    """
    def __init__(self):
        super().__init__

    def put(self, key, item):
        """add to cache system
        """
        cache = self.cache_data
        if key and item:
            cache[key] = item
            if len(cache) > BaseCaching.MAX_ITEMS:
                key = list(cache.keys())[-2]
                del cache[key]
                print(f"DISCARD: {key}")

    def get(self, get):
        """get item from cache_data
        """
        return self.cache_data.get(key, "None")
