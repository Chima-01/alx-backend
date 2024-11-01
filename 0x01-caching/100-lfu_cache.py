#!/usr/bin/env python3
"""
    Class LFUCache (least Frequently used)
    inherits from BaseCaching and is a caching system
"""
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """ initialize class
    """
    key_count = {}

    def put(self, key, item):
        """ add to cache system
        """
        cache = self.cache_data
        if key and item:
            if (len(cache) + 1 > BaseCaching.MAX_ITEMS and key not in cache):
                lfu = self.get_lfu(None)
                del cache[lfu]
                del self.key_count[lfu]
                print(f"DISCARD: {lfu}")
            try:
                self.key_count[key] += 1
            except KeyError:
                self.key_count[key] = 1
            cache[key] = item

    def get(self, key):
        """ get item from key
        """
        if key is not None:
            self.get_lfu(key)
            if key in self.key_count:
                self.key_count[key] += 1
        return self.cache_data.get(key)

    def get_lfu(self, key):
        """ implement a lfu cache system
        """
        key_count = self.key_count
        if key is None:
            lfu = min(key_count, key=key_count.get)
            return lfu
        elif key in key_count:
            item = key_count.pop(key)
            key_count[key] = item
