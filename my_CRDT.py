"""
Thread-operation are left on the caller' side (using Syncronized block/method, or other implementation) 
"""
class myCRDT:
    def __init__(self):
        self.__add_set = {} # key: e, value: timestamp or so-called "score"
        self.__rem_set = {}
        self.val_set = set()
    
    def get_addset(self):
        return self.__add_set
    
    def get_remset(self):
        return self.__rem_set
        
    def add(self, e, t):
        if e not in self.__add_set:
            if e not in self.__rem_set or t > self.__rem_set[e]:
                self.__add_set[e] = t
                self.val_set.add(e)
        else:
            if t > self.__add_set[e]:
                self.__add_set[e] = t
            if e in self.__rem_set and t > self.__rem_set[e]:
                self.val_set.add(e)
        
        
    def remove(self, e, t):
        if e not in self.__rem_set:
            if e not in self.__add_set or t > self.__add_set[e]:
                self.__rem_set[e] = t
                
                if e in self.val_set:
                    self.val_set.remove(e)
        else:
            if t > self.__rem_set[e]:
                self.__rem_set[e] = t
            if e in self.val_set and \
               e in self.__add_set and \
               t > self.__add_set[e]:
                self.val_set.remove(e)
    
    def exist(self, e):
        if e not in self.__add_set:
            return False
        else:
            if e in self.__rem_set and self.__add_set[e] < self.__rem_set[e]:
                return False
            return True
        # can I just check if e in self.val_set?
        
    def get(self):
        return self.val_set