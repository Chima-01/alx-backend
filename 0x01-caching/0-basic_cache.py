#!/usr/bin/env python3
"""
Create a class BasicCache that inherits
from BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
        class to implement a basic caching system
    """
    def get(self, key):
        """ returns cache_data by key given
        """
        if not key or key is None:
            return None
        return self.cache_data.get(key)

    def put(self, key, item):
        """ add items to cache_data
        """
        if key and item:
            self.cache_data.update({key: item})
