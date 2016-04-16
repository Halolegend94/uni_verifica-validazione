
# this stack stores strings


class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         #print "push stackappend: %s" % item
         self.items.append(item)
         #print "push: ", ', '.join(map(str, self.items))
         return

     def pop(self):
         return self.items.pop()
         #print "pop: ", ', '.join(map(str, self.items))
         return

     def head(self):
         return self.items[len(self.items)-1]

     def size(self):
          # print "stack size %d" % (len(self.items))
          return len(self.items)

     def printstack(self):
          return  ', '.join(map(str, self.items))
