
# this class has to be adaptated to state signature and fmu model name

import sys
import logging
import time
from mypylib.hashtable import HashTable
from mypylib.stack import Stack
from mypylib.getset import ModelState

class Search :

    def dfs(self):

          PR_FREQ = 1
          t0 = time.clock()

          print "Begin DFS based reachability analysis.\n"
          logging.debug('dfs: begin')

          visited = 0
          logging.debug("dfs: init visited states %d", visited)
          H = HashTable()
          S = Stack()   # time, state, action stack
          M = ModelState()
          x = M.get_model_initial_state()     # get init state

          if (M.adm(x)) :   # state is admissible
              if M.error(x):
                   # error, return witness and exit
                   print "System does not satisfy specifications as witnessed by the following counterexample:\n"
                   print "%s" % S.printstack()
                   sys.exit()
              # push state-time-act transition in stack
              PresentTime = M.get_init_time()
              state_time = {}
              state_time['state'] = x
              state_time['time'] = PresentTime
              S.push(state_time)  # push initial state-time
#             S.push(x)  # push state
              S.push(M.init_act())  # push act index
              logging.debug("dfs: Admissible init state-time-act: %r", S.printstack())

          #print "dfs: init stack"
          #S.printstack()

          while (not(S.isEmpty())) : # at least a transition is present in the stack

              logging.debug("dfs: nonempy state stack: %r", S.printstack())

              a = S.pop() # last act explored
              state_time = S.head() # read last state-time
              x = state_time['state'] # read last state
              PresentTime = state_time['time'] # read last time

              logging.debug("dfs: exploting transitions from state %r,  action %r, time %r", x, a, PresentTime)

# explore next transition
              if (M.next_action(a)) :  # true iff next act from a exists

                  S.push(a)  # push act index

                  y = M.get_model_next_state(PresentTime, x, a)


                  if (M.adm(y) and (not(H.ispresent(y))) ) :   # state is admissible and fresh
                       PresentTime = M.advance_time(PresentTime)
                       state_time = {}
                       state_time['state'] = y
                       state_time['time'] = PresentTime
                       S.push(state_time)  # push initial state-time
                       logging.debug("dfs: pushing new state-time %r", state_time)
                       #S.push(PresentTime)   # store time
                       #S.push(y)             # store state
                       #print "Admissible new stack:"
                       #S.printstack()
                       #print "dfs: adm new state y", y

                       if M.error(y) :
                          # error, return witness and exit
                          print "System does not satisfy specifications as witnessed by the following counterexample:\n"
                          print "%s" % S.printstack()
                          sys.exit()

                       S.push(M.init_act())  # push act index
                  #else :
                      #logging.info("dfs: reached nonadm or old state y: %r", y)
                      #logging.info("dfs: stack: %r", S.printstack())
                      #logging.info("dfs: visited states so far: %d", visited)

              else :  # no more transitions from x
                  logging.debug("dfs: completed exploration from state %r", x)
                  logging.debug("dfs: completed exploration for stack: %r", S.printstack())

                  # mark x as visited
                  H.insert(x)
                  visited = visited + 1

                  state_time = S.pop() # remove state_time from stack

                  #x = S.pop() # remove x from stack
                  #PresentTime = S.pop()  # remove time from stack   (back in time)

                  #logging.info("dfs: popped old state-time %r", state_time)
                  if (visited % PR_FREQ == 0) :
                      t1 = time.clock()   # time elapsed since begin of dfs
                      print "dfs: visited states so far %d, cpu time %f seconds, states per second: %f" % (visited, (t1 - t0), visited/(t1 - t0))
                      print "state ", x
                      print "stack ", S.printstack()


                    #if (nextlevel == 1) : depth = depth + 1
                    #print "dfs: new level depth %d" % (depth)

          print "System satisfies specifications. Visited states %d." % visited
          logging.debug('dfs: end: visited states: %d', visited)
