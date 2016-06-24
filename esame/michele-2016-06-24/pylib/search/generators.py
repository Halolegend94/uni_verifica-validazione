
def product(*args):
    """
    Returns the cartesian product of ``args``.

    :param *args:
        A list of lists. Each ``arg`` is a domain.
    """
    p = product_set_cardinality(*args)
    i = 0
    while i < p:
        yield lex_order_item(i, *args)
        i += 1

def product_set_cardinality(*args):
    """
    Returns the cardinality of the cartesian product set of ``args``
    (a list of lists).
    """
    return reduce(lambda x, y : x * y, [len(_) for _ in args])

def lex_order_item(i, *args):
    """
    Returns the ``i``-th element of the canonical order of the
    cartesian product of ``args``, i.e. the order obtained by ordering by
    ``args[-1]``, then by ``args[-2]``, etc. up to ``args[0]``.
    An example: ::

        args = [[1,2], [3,4]]

        i = 0 -> [1,3]
        i = 1 -> [2,3]
        i = 2 -> [1,4]
        i = 3 -> [2,4]
    """
    p = product_set_cardinality(*args)
    assert i < p, "Index {} out of bounds.".format(i)
    res = [None] * len(args)
    for j in range(len(args)):
        res[j] = args[j][i % len(args[j])]
        i = i / len(args[j])
    return res

