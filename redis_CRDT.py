"""
execute tests:
python -m unittest discover -s . -p "test*.py"
"""

import redis

class redisCRDT:
    def __init__(self, server):
        self.__client = server

    def get_add_ts(self, e):
        ts = self.__client.zscore("add_set", e)
        if ts:
            return ts
        else:
            return None

    def get_rem_ts(self, e):
        ts = self.__client.zscore("rem_set", e)
        if ts:
            return ts
        else:
            return None

    def add(self, e, t):
        # check if element in add_set
        old_ts = self.get_add_ts(e)
        if old_ts:
            if t > old_ts:
                self.__client.zadd("add_set", {str(e):str(t)})
        else:
            res = self.__client.zadd("add_set", {str(e):str(t)})
    
    def remove(self, e, t):
        old_ts = self.get_rem_ts(e)
        if old_ts:
            if t > old_ts:
                self.__client.zadd("rem_set", {str(e):str(t)})
        else:
            res = self.__client.zadd("rem_set", {str(e):str(t)})

