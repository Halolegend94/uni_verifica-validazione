
def product(*args):
    p = product_set_cardinality(*args)
    i = 0
    while i < p:
        yield lex_order_item(i, *args)
        i += 1

def product_set_cardinality(*args):
    return reduce(lambda x, y : x * y, [len(_) for _ in args])

def lex_order_item(i, *args):
    p = product_set_cardinality(*args)
    assert i < p, "Index {} out of bounds.".format(i)
    res = [None] * len(args)
    for j in range(len(args)):
        res[j] = args[j][i % len(args[j])]
        i = i / len(args[j])
    return res

