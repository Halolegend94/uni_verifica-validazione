
from state_set import StateSet
from stack import Stack

import numpy

def dfs(model):
    visited = 0
    state_set = StateSet()
    stack = Stack()
    state = model.get_initial_state()
    inputs = model.get_inputs()
    if state.admissible():
        if state.error():
            print "Initial state is not admissible:"
            print state
            return False
        step = 0
        stack.push((state, step))
        stack.push(model.get_actions())
    while stack.size() > 0:
        actions = stack.pop()
        state, step = stack.peek()
        try:
            action = actions.next()
            stack.push(actions)
            new_state = model.get_next_state(step, state, action)
            if new_state.admissible() and not state_set.contains(new_state):
                new_step = step + 1
                stack.push((new_state, new_step))
                if new_state.error():
                    print "Found error at step {}, state is:".format(new_step)
                    print new_state
                    print_input_sequence(stack, inputs)
                    return False
                stack.push(model.get_actions())
        except StopIteration:
            visited += 1
            state_set.add(state)
            stack.pop()
    print "{} states visited, no error found.".format(visited)
    return True

def variables_evolution(stack, variables):
    stack_view = stack.view()
    seq = []
    for i in range(0, len(stack_view), 2):
        state, time = stack_view[i]
        seq.append([state.get_variable(v) for v in variables])
    return numpy.array(seq)

def print_input_sequence(stack, inputs):
    input_sequence = numpy.transpose(variables_evolution(stack, inputs))
    for i in range(len(inputs)):
        print "{} : {}".format(inputs[i], input_sequence[i])

