import sys
import logging
import time
from PyLib.HashSet import HashSet
from PyLib.Stack import Stack
from PyLib.ModelState import ModelState
class Search:
    def dfs(self, model, actions):
        H = HashSet()
        S = Stack()
        nodevisited = 0
        AG = ActionGenerator(actions)
        x = model.get_model_next_state()
        if(not(model.admissible(x))):
            print "System has no admissible state"
            sys.exit()

        state_time = {}
        state_time['state'] = x
        state_time['time'] = model.get_init_time()
        S.push(state_time)
        S.push(AG)

        while(not(S.isEmpty())):

            a = S.pop() #get the last transition explored
            state_time = S.head()
            x = state_time['state']
            currentTime = state_time['time']
            out = a.next()
            nodevisited += 1
            if(out != None):
                S.push(a)
                newState = model.get_model_next_state(x, out)
                if(model.admissible(newState) and not(H.contains(newState))):
                    newTime = model.advance_time(currentTime)
                    state_time = {}
                    state_time['state'] = newState
                    state_time['time'] = newTime
                    S.push(state_time)
                    if(model.isUnsafe(newState)):
                        print "System does not satisfy requirements as shown by this trace: %r" % S.printstack()
                        sys.exit()
                    S.push(ActionGenerator(actions))
            else:
                H.insert(x)
                state_time = S.pop()
