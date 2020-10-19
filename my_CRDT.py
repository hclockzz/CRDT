"""
execute tests:
python -m unittest discover -s . -p "test*.py"
"""
class myCRDT:
    def __init__(self):
        self.__add_set = {} # key: e, value: timestamp or so-called "score"
        self.__rem_set = {}
        self.__val_set = set()
    
    def get_addset(self):
        return self.__add_set
    
    def get_remset(self):
        return self.__rem_set
        
    def add(self, e, t):
        if e not in self.__add_set:
            self.__add_set[e] = t
            if e not in self.__rem_set or t > self.__rem_set[e]:
                self.__val_set.add(e)
        else:
            if t > self.__add_set[e]:
                self.__add_set[e] = t
            if e in self.__rem_set and t > self.__rem_set[e]:
                self.__val_set.add(e)
        
        
    def remove(self, e, t):
        if e not in self.__rem_set:
            self.__rem_set[e] = t
            if e in self.__val_set and t > self.__add_set[e]:
                self.__val_set.remove(e)
        else:
            if t > self.__rem_set[e]:
                self.__rem_set[e] = t
            if e in self.__val_set and \
               e in self.__add_set and \
               t > self.__add_set[e]:
                self.__val_set.remove(e)
    
    def exist(self, e):
        if e not in self.__add_set:
            return False
        else:
            if e in self.__rem_set and self.__add_set[e] < self.__rem_set[e]:
                return False
            return True
        
    def get(self):
        return self.__val_set