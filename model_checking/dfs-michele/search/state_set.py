"""
State Set
+ contains(state)
+ add(state)
"""

class StateSet(object):
    def __init__(self):
        self.state_set = set()

    def contains(self, state):
        return state in self.state_set

    def add(self, state):
        self.state_set.add(state)

