"""
Model
=== private methods
- set(variable, value)
- get(variable)
- reset_model()
- set_state(state)
- get_state()
=== public methods
+ get_initial_state()
+ get_initial_action()
+ get_next_state(state, time, action)
"""

from generators import product
from state import State

from pyfmi import load_fmu

class Model(object):
    def __init__(self, fmu_path, state_vars, action_values, var_map, time_step):
        """
        :param dict(str: [int]) action_values:
            A dictionary { action name : list of action values }.
        """
        # store parameters
        self.fmu_path      = fmu_path
        self.state_vars    = state_vars
        self.action_values = action_values
        self.var_map       = var_map
        self.time_step     = time_step
        # names of inputs
        self.action_vars = action_values.keys()
        # load model
        self.fmu = None
        self.__reset_model()
        # set default options
        self.opts = self.fmu.simulate_options()
        self.opts['result_handling'] = 'memory'
        self.opts['CVode_options']['verbosity'] = 50

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Model reset
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def __reset_model(self):
        """
        Loads the model / resets it if it's loaded.
        """
        if self.fmu == None:
            self.fmu = load_fmu(self.fmu_path)
        else:
            self.fmu.reset()

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # State set/get
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def __set_state(self, state):
        for v in self.state_vars:
            self.__set(v, state.get_variable(v))

    def __get_state(self):
        var_values = {}
        for v in self.state_vars:
            var_values[v] = self.__get(v)
        state = State(var_values)
        return state

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Variable/input set/get
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def __get(self, var):
        """
        Gets the value of state variable ``var``.
        """
        return self.fmu.get(var)[0]

    def __set(self, var, value):
        """
        Sets the value of state variable ``var``.
        The value is set through a start parameter.
        """
        self.fmu.set(self.var_map[var], value)

    def __set_input_action(self, action):
        for i in range(len(self.action_vars)):
            self.__set(self.action_vars[i], action[i])

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Simulation start & end time
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def __start_time(self, current_step):
        return current_step * self.time_step

    def __end_time(self, current_step):
        return (current_step + 1) * self.time_step

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Public methods
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def get_initial_state(self):
        """
        Returns the initial state of the model.
        """
        self.__reset_model()
        var_values = {}
        for v in self.state_vars:
            var_values[v] = self.fmu.get(self.var_map[v])[0]
        state = State(var_values)
        return state

    def get_next_state(self, current_step, state, action):
        """
        Returns the state the model gets to after injection ``action``
        at ``time`` starting from ``state``.
        """
        self.__reset_model()
        self.__set_state(state)
        self.__set_input_action(action)
        self.fmu.time = self.__start_time(current_step)
        self.fmu.simulate(self.__start_time(current_step), self.__end_time(current_step), options = self.opts)
        return self.__get_state()

    def get_inputs(self):
        """
        Returns a list of the name of the inputs.
        """
        return self.action_vars

    def get_actions(self):
        """
        Returns a generator of all possible actions.
        """
        return product(*self.action_values.values())


