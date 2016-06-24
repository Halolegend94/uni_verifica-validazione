import sys
import logging
import time
from PyLib.HashSet import HashSet
from PyLib.Stack import Stack
from PyLib.ModelState import ModelState
from PyLib.ActionGenerator import ActionGenerator

class Search:
    def dfs(self, model, actions, maxDepth):
        H = HashSet()
        S = Stack()
        nodevisited = 0
        AG = ActionGenerator(actions)
        x = model.get_model_next_state()
        #check if the environment model has no admissible state
        if(not(model.isAdmissible(x))):
            print "environment model has no admissible state"
            sys.exit()

        state_time = {}
        state_time['state'] = x
        state_time['time'] = model.get_init_time()
        S.push(state_time)
        S.push(AG)
        currentDepth = 0;
        while(not(S.isEmpty())):
            a = S.pop() #get the last transition explored
            state_time = S.top()
            x = state_time['state']
            currentTime = state_time['time']
            out = a.next()
            if(out != None):
                S.push(a)
                newState = model.get_model_next_state(x, out, currentTime)
                if(model.isAdmissible(newState) and not(H.contains(newState)) and currentDepth < maxDepth):
                    #print (" " * currentDepth) + "".join(str(e) for e in out)
                    newTime = model.advance_time(currentTime)
                    state_time = {}
                    state_time['state'] = newState
                    state_time['time'] = newTime
                    S.push(state_time)
                    if(model.isUnsafe(newState)):
                        print "System does not satisfy requirements as shown by this trace:"
                        S.printStack()
                        sys.exit()
                    S.push(ActionGenerator(actions))
                    currentDepth = currentDepth + 1
            else:
                nodevisited += 1
                H.insert(x)
                currentDepth = currentDepth - 1
                state_time = S.pop()
