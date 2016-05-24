class ActionGenerator:

    def __init__(self, *args):
        self.args = args
        self.cardinality = reduce(lambda x, y : x * y, [len(i) for i in args])
        self.index = 0


    def next(self):
        temp = self.index
        self.index = self.index + 1
        if(temp < self.cardinality):
            out = [None] * len(self.args)
            for i in range(len(self.args)):
                out[i] = self.args[i][temp % len(self.args[i])]
                temp = temp / len(self.args[i])
            return out
        else:
            return None
