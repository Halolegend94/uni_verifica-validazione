
# we assume keys needs to be serialized

import cPickle

class HashTable:
     def __init__(self):
         self.items = {}

     def isEmpty(self):
         return self.items == {}

     def insert(self, key):
          "mark state as visited"
          self.items[cPickle.dumps(key)] = 1;
          return;

     def ispresent(self, key):
          "check if state already visited"
          if (cPickle.dumps(key) in self.items) :
               #print "ispresent: state already visited", key
               return 1  # true
          else : 
               return 0  # false
