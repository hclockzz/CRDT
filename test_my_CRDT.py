import unittest
from my_CRDT import myCRDT
from datetime import datetime
import time 

def getCurrentTime():
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    return timestamp
    
    
class TestCRDT(unittest.TestCase):
    def setUp(self):
        self.obj = myCRDT()
        
    def test_add_single_value(self):
        ts = getCurrentTime()
        test_obj = self.obj
        test_obj.add("Tomato", ts)
        self.assertEqual(test_obj.get(), {"Tomato"})
    
    def test_add_multi_values(self):
        test_obj = self.obj
        print("Before assert", test_obj.get_addset())
        ts = getCurrentTime()
        test_obj.add("Onion", ts)

        ts = getCurrentTime()
        test_obj.add("Egg", ts)
        self.assertEqual(test_obj.get(), {"Egg", "Onion"})
        print("After assert", test_obj.get_addset())
    
    def test_remove_single_value(self):
        ts = getCurrentTime()
        test_obj = self.obj
        test_obj.add("Spinach", ts)
        print("After adding", test_obj.get_addset())

        ts = getCurrentTime()
        test_obj.remove("Spinach",ts)
        self.assertEqual(test_obj.get(), set())
        print("After removing", test_obj.get_remset())
    
    def test_remove_multi_values(self):
        test_obj = self.obj
        ts = getCurrentTime()
        test_obj.add("Yu Choi", ts)

        ts = getCurrentTime()
        test_obj.add("Avocado", ts)

        ts = getCurrentTime()
        test_obj.add("Pie", ts)

        print("After adding", test_obj.get_addset())

        ts = getCurrentTime()
        test_obj.remove("Pie",ts)
        self.assertEqual(test_obj.get(), {"Yu Choi", "Avocado"})

        ts = getCurrentTime()
        test_obj.remove("Avocado",ts)
        self.assertEqual(test_obj.get(), {"Yu Choi"})

        ts = getCurrentTime()
        test_obj.remove("Yu Choi",ts)
        self.assertEqual(test_obj.get(), set())

    def test_add_existing_update_timestamp(self):
        test_obj = self.obj
        ts1 = getCurrentTime()
        test_obj.add("Onion", ts1)
        
        time.sleep(1)
        ts2 = getCurrentTime()
        test_obj.add("Onion", ts2)

        add_set = test_obj.get_addset()
        self.assertGreater(add_set["Onion"], ts1)
        self.assertEqual(add_set["Onion"], ts2)

    def test_remove_existing_update_timestamp(self):
        test_obj = self.obj
        ts1 = getCurrentTime()
        test_obj.add("Onion", ts1) 

        time.sleep(1)
        ts2 = getCurrentTime()
        test_obj.remove("Onion", ts2)

        time.sleep(1)
        ts3 = getCurrentTime()
        test_obj.remove("Onion", ts3)

        rem_set = test_obj.get_remset()
        self.assertGreater(rem_set["Onion"], ts2)
        self.assertEqual(rem_set["Onion"], ts3)
               

    def test_exist_true_membership(self):
        test_obj = self.obj
        ts1 = getCurrentTime()
        test_obj.add("Onion", ts1) 
        
        res = test_obj.exist("Onion")
        self.assertTrue(res)

    def test_exist_false_membership(self):
        test_obj = self.obj
        ts1 = getCurrentTime()
        test_obj.add("Onion", ts1) 
        
        res = test_obj.exist("Ginger")
        self.assertFalse(res)

    def test_exist_true_membership_bytimestamp(self):
        test_obj = self.obj
        ts1 = getCurrentTime()
        test_obj.add("Onion", ts1) 

        ts2 = getCurrentTime()
        test_obj.remove("Onion", ts2)

        ts3 = getCurrentTime()
        test_obj.add("Onion", ts3)    

        res = test_obj.exist("Onion")
        self.assertTrue(res)    

   
"""
test exist():
- test non-existant element
- add one element
- add one element, then remove
- add one element, then remove, then add the element again
"""

"""
test get():
- covered in above test cases.
"""
if __name__ == '__main__': 
    unittest.main()