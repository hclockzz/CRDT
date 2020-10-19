import redis
# import config

class redisCRDT:
    def __init__(self, server):
        self.client = server

    def get_add_ts(self, e):
        ts = self.client.zscore("add_set", e)
        if ts:
            return ts
        else:
            return None

    def get_rem_ts(self, e):
        ts = self.client.zscore("rem_set", e)
        if ts:
            return ts
        else:
            return None

    def add(self, e, t):
        # check if element in add_set
        old_ts = self.get_add_ts(e)
        if old_ts:
            if t > old_ts:
                self.client.zadd("add_set", {str(e):str(t)})
        else:
            res = self.client.zadd("add_set", {str(e):str(t)})
            print(res)
    
    def remove(self, e, t):
        old_ts = self.get_rem_ts(e)
        if old_ts:
            if t > old_ts:
                self.client.zadd("rem_set", {str(e):str(t)})
        else:
            res = self.client.zadd("rem_set", {str(e):str(t)})
            print(res)

