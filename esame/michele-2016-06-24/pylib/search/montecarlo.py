
import random
import numpy
import math
from matplotlib import pyplot

def montecarlo(model, inputs, trials, duration, samples, continuous=False, monitor_name="error", inspect_vars=[]):
    """
    :param model:
        An FMU.
    :param inputs:
        A dictionary 'var_name' : [list of input values].
        The list of input values must have size 2 for all variables if
        ``continuous == True``.
    :param trials:
        Number of trials.
    :param length:
        Length of each trial.
    :param samples:
        How many times the input changes during simulation.
    :param continuous:
        ``True`` iff each domain is continuous.
    """
    inspect_vars += [monitor_name]
    inspect_vars += inputs.keys()
    opts = model.simulate_options()
    opts['ncp'] = samples+1
    opts['CVode_options']['verbosity'] = 50
    opts['result_handling'] = 'memory'
    for i in range(trials):
        print "{}/{}".format(i+1, trials)
        model.reset()
        input_tuple = random_input(inputs, duration, samples, continuous)
        res = model.simulate(0, duration, input = input_tuple, options = opts)
        display_variables(res, inspect_vars)
        if model.get(monitor_name)[0]:
            return False
    return True

def display_variables(values, names):
    print "Plotting {} variables ({})".format(len(names), names)
    n_plots = len(names)
    n_cols, n_rows = grid(n_plots)
    for i in range(n_plots):
        pyplot.subplot(n_cols, n_rows, i+1)
        pyplot.plot(values['time'], values[names[i]])
        ymin, ymax = pyplot.ylim()
        d = abs(ymax - ymin)
        pyplot.ylim(ymin - (0.1 * d), ymax + (0.1 * d))
        pyplot.title(names[i])
    pyplot.show()

def grid_adj(t):
    s = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (1, -1), (1, 0), (0, 1), (1, 1)]
    for i in range(len(s)):
        yield (t[0] + s[i][0], t[1] + s[i][1])

def grid_kpi(s, n):
    return (n - (s[0] * s[1]), abs((16. / 9) - (1.0 * s[0] / s[1])))

def grid(n_plots):
    s = int(math.ceil(math.sqrt(n_plots)))
    s = (s, s)
    done = False
    while not done:
        done = True
        for x in grid_adj(s):
            if x[1] <= 0 or x[0] <= 0:
                continue
            kpi_x = grid_kpi(x, n_plots)
            kpi_s = grid_kpi(s, n_plots)
            if kpi_x[0] > kpi_s[0] and kpi_x[1] < kpi_s[1] and x[0] * x[1] >= n_plots:
                s = x
                done = False
    return s

def random_input(inputs, duration, samples, continuous):
    v = []
    t = numpy.linspace(0.0, duration, samples+1)
    d = [t]
    for key, domain in inputs.iteritems():
        v += [key]
        d += [random_sequence(len(t), domain, continuous)]
    return (v, numpy.transpose(numpy.vstack((d))))

def random_sequence(length, domain, continuous):
    """
    :param length:
        The length of the sequence.
    :param domain:
        A list of all allowed values. The list consists only of [min, max]
        if ``continuous == True``.
    """
    if continuous:
        res = [ random_continuous(*domain) for i in range(length) ]
    else:
        res = [ random_discrete(domain) for i in range(length) ]
    return res

def random_continuous(lower, upper):
    r = random.random()
    return r * lower + (1.0 - r) * upper

def random_discrete(seq):
    return random.choice(seq)

