import cPickle

class HashSet:
    def __init__(self):
        self.items = {}

    def isEmpty(self):
        return self.items == {}

    def insert(self, key):
        "mark the state as visited"
        self.items[cPickle.dumps(key)] = 1;

    def contains(self, key):
        return cPickle.dumps(key) in self.items
