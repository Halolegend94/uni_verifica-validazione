class Stack:

    def __init__(self):
        self.count = 0
        self.items = []

    def isEmpty(self):
        return self.count == 0

    def push(self, item):
        self.items.append(item)
        self.count += 1

    def pop(self):
        if self.count == 0:
            return None
        else:
            self.count  -= 1
            return self.items.pop()

    def head(self):
        if self.count == 0:
            return None
        else:
            return self.items[self.count - 1]

    def printStack(self):
        return ', '.join(map(str, self.items))
