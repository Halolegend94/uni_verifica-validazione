import sys
import logging
import time
from PyLib.HashSet import HashSet
from PyLib.Stack import Stack
from PyLib.ModelState import ModelState
class Search:

    def dfs(self):
        H = HashSet()
        S = Stack()
        M = ModelState()

        x = M.get_model_next_state()
        if(not(M.adm(x))):
            print "System has no admissible state"
            sys.exit()

        elif(M.isUnsafe(x)):
            print "System does not satisfy specifications at initial state %r" % map(str, x)
            sys.exit()

        state_time = {}
        state_time['state'] = x
        state_time['time'] = M.get_init_time()
        S.push(state_time)
        S.push(M.init_actions())

        while(not(S.isEmpty())):

            a = S.pop() #get the last transition explored
            state_time = S.head()
            x = state_time['state']
            currentTime = state_time['time']

            if(M.next_action(a)):
                S.push(a)
                newState = M.get_model_next_state(x, a)
                if(M.adm(newState) and not(H.contains(newState))):
                    newTime = M.advance_time(currentTime)
                    state_time = {}
                    state_time['state'] = newState
                    state_time['time'] = newTime
                    S.push(state_time)
                    if(M.isUnsafe(newState)):
                        print "System does not satisfy requirements as shown by this trace: %r" % S.printstack()
                        sys.exit()
                    S.push(M.init_actions())
            else:
                H.insert(x)
                state_time = S.pop()
