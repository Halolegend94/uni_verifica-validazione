class ActionGenerator:

    def __init__(self, args):
        self.args = args
        self.cardinality = reduce(lambda x, y : x * y, [len(i) for i in args])
        self.index = -1


    def next(self):
        self.index = self.index + 1
        temp = self.index
        if(temp < self.cardinality):
            out = [None] * len(self.args)
            for i in range(len(self.args)):
                out[i] = self.args[i][temp % len(self.args[i])]
                temp = temp / len(self.args[i])
            return out
        else:
            return None

    def __str__(self):
        temp = self.index
        if(temp < self.cardinality):
            out = [None] * len(self.args)
            for i in range(len(self.args)):
                out[i] = self.args[i][temp % len(self.args[i])]
                temp = temp / len(self.args[i])
            return "actions: " + str(out)
        else:
            return str(None)
