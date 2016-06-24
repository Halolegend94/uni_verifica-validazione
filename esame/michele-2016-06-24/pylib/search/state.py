"""
STATE
+ get_variable(var)
+ admissible()
+ error()

A State should be hashable (and therefore immutable).
"""

adm_var = 'admissible'
err_var = 'error'

class State(object):
    def __init__(self, state_vars):
        assert adm_var in state_vars
        assert err_var in state_vars
        self.variables = { k: v for k, v in state_vars.items() }

    def get_variable(self, var):
        return self.variables[var]

    def admissible(self):
        return bool(self.variables[adm_var])

    def error(self):
        return bool(self.variables[err_var])

    def __hash__(self):
        return hash(tuple((k, v) for k, v in self.variables.items()))

    def __cmp__(self, o):
        if type(self) != type(o):
            return -1
        return self.variables.__cmp__(o.variables)

    def __str__(self):
        res = "=== STATE ===\n"
        max_len = max([len(_) for _ in self.variables.keys()])
        fmt_str = "{0:" + str(max_len) + "s} : {1}\n"
        for v in self.variables:
            res += fmt_str.format(v, self.variables[v])
        return res

