"""
Stack
+ push(elem)
+ pop()
+ peek()
+ size()
+ view()
"""

import numpy

class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        assert self.size() > 0
        return self.stack.pop()

    def peek(self):
        assert self.size() > 0
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def view(self):
        """
        Returns a view of the full stack. The view is immutable.
        """
        # TODO make this immutable/a copy
        return self.stack

