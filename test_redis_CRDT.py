import unittest
from redis_CRDT import redisCRDT
from datetime import datetime
import redis
import time 
import fakeredis

def getCurrentTime():
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    return timestamp
    
    
class TestCRDT(unittest.TestCase):
    def setUp(self):
        self.server = fakeredis.FakeStrictRedis()
        self.obj = redisCRDT(self.server)

    def __fetch_add_set(self):
        raw_res = self.server.zrange("add_set", 0, -1, withscores=True)
        res_add = dict()
        for entry in raw_res:
            res_add[entry[0].decode('utf-8')] = entry[1]

        return res_add

    def __fetch_rem_set(self):
        raw_res = self.server.zrange("rem_set", 0, -1, withscores=True)
        res_add = dict()
        for entry in raw_res:
            res_add[entry[0].decode('utf-8')] = entry[1]

        return res_add

    def test_add_values(self):
        test_obj = self.obj

        ts = getCurrentTime()
        test_obj.add("Tomato", ts)

        test_obj.add("Potato", ts)

        add_set = self.__fetch_add_set()
        self.assertEqual(set(add_set.keys()), {"Tomato", "Potato"})

    def test_rem_values(self):
        test_obj = self.obj

        ts = getCurrentTime()
        test_obj.add("Lemon", ts)
        ts = getCurrentTime()
        test_obj.add("Apple", ts)

        ts = getCurrentTime()
        test_obj.remove("Apple", ts)
        ts = getCurrentTime()
        test_obj.remove("Lemon", ts)

        add_set= self.__fetch_add_set()
        # print(add_set)
        rem_set = self.__fetch_rem_set()
        # print(rem_set)
        self.assertEqual(set(rem_set.keys()), {"Apple", "Lemon"})

        


if __name__ == '__main__': 
    unittest.main()