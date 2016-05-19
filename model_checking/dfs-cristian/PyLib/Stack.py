class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop()

    def top(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items[len(self.items) - 1]

    def printStack(self):
        return ', '.join(map(str, self.items))
