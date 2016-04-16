
# this class has to be adaptated to state signature and fmu model name

from pymodelica import compile_fmu
from pyfmi import load_fmu
import matplotlib.pyplot as plt
import logging

class ModelState:

     def __init__(self):

          self.TimeStep = 1   # in seconds

          self.TimeZero = 0   # in TimeStep steps
          self.t = 0          # current time in TimeStep steps
 
        


          self.statekeys = ['env.avg0', 'env.adm0', 'env.n0', 'env.depth0', 'monitor.y0', 'sys.x0']
          self.inputkeys = ['noise0', 'failures0']

          self.getdict = {}
          self.getdict['env.avg0'] = 'env.x.avg' 
          self.getdict['env.adm0'] = 'env.x.adm' 
          self.getdict['env.n0'] = 'env.x.n' 
          self.getdict['env.depth0'] = 'env.x.depth' 
          self.getdict['env.noise0'] = 'env.d.noise'
          self.getdict['env.failures0'] = 'env.d.failures' 
          self.getdict['monitor.y0'] = 'monitor.y' 
          self.getdict['sys.x0'] = 'sys.x'
 
          # self.state = {}
          #for k in self.statekeys :
          #     self.state[k] = self.model.get(self.getdict[k])

          self.time = {}
          self.time['start'] = self.t

          #self.act = {}
          # self.act['time'] = self.StartTime
          #for k in self.inputkeys :
          #     self.act[k] = self.model.get(self.getdict[k])

          self.actlist = [-1, 0.0, 1]
       
          self.fmu = compile_fmu('ClosedSystem', ['closed-system.mo', 'system.mo', 'monitor.mo', 'environment.mo', 'dictionary.mo', 'state.mo'])

          self.create_model()
          #self.model = load_fmu(self.fmu)
          #self.opts = self.model.simulate_options()
          #self.opts['CVode_options']['verbosity'] = 50 # No output
          #self.opts['initialize'] = False 
          #self.model.time = self.start_time(self.t)
          #self.model.initialize()

          #for k in self.statekeys :
          #     self.state[k] = self.model.get(self.getdict[k]) 


          #for k in self.inputkeys :
          #     self.state[k] = self.model.get(self.getdict[k]) 

          # get time step from disturbance model
          self.TimeStep = self.model.get('env.T')    # in seconds


     def start_time(self, t):
        return (t*self.TimeStep)

     def end_time(self, t):
        return ((t + 0.99999)*self.TimeStep)


     def model_get(self, key):
#        return self.state[key]
         return self.model.get(self.getdict[key]) 


     def model_set(self, key, value):
         self.model.set(key, value)
         return


     def model_next(self):
# advance simulation
           logging.debug("model_next: start_time = %f, final_time = %f", 
                        self.start_time(self.t), self.end_time(self.t))

           #self.model.initialize() 

           res = self.model.simulate(start_time=self.start_time(self.t), final_time=self.end_time(self.t), options=self.opts)



           #for k in self.statekeys :
           #    self.state[k] = self.model.get(self.getdict[k]) 


           #for k in self.inputkeys :
           #    self.state[k] = self.model.get(self.getdict[k]) 

           # store next state at time t + 1
          # self.tindex = self.find_argval(res['time'], (self.t + 1)*self.TimeStep)

          # logging.info("model_next: res['time'][%d] = %f", self.tindex, res['time'][self.tindex])

          # for k in self.statekeys :
         #      self.state[k] = res[self.getdict[k]][self.tindex]

         #  for k in self.inputkeys :
         #      self.state[k] = res[self.getdict[k]][self.tindex]

           return


     def create_model(self):
           self.model = load_fmu(self.fmu)
           self.opts = self.model.simulate_options()
           self.opts['result_handling'] = 'memory'
           self.opts['CVode_options']['verbosity'] = 50 # No output

           #self.opts['initialize'] = False 
           #self.model.time = self.start_time(self.t)
           #self.model.initialize() 

           #for k in self.statekeys :
           #    self.state[k] = self.model.get(self.getdict[k]) 


           #for k in self.inputkeys :
           #    self.state[k] = self.model.get(self.getdict[k]) 

           return


     def get_model_state(self):
         x = {}
         for k in self.statekeys :
               x[k] = self.model_get(k)
              # print "get_model_state: %s %s" % (k, x[k])
         logging.debug("get_model_state return: %s", x)
         return x
 
     def get_model_initial_state(self):
         x = {}
         for k in self.statekeys :
               x[k] = self.model.get(k) 
               # print "get_model_initial_state: %s %s" % (k, x[k])
         logging.debug("get_model_initial_state return: %s", x)
         return x

  


     def get_init_time(self):
         mytime = {}
         mytime['start'] = self.TimeZero
         return mytime

     def advance_time(self, mytime):
         newtime = {}
         newtime['start'] = mytime['start'] + 1
         return newtime

     def set_model_time(self, mytime):
           self.t = mytime['start']
           return 


     def init_act(self):
          a = {}
          a['index'] = -1
          a['value'] = -1
          return a

     def next_action(self, a):
         if (a['index'] < len(self.actlist) - 1) :
            a['index'] = a['index'] + 1
            a['value'] = self.actlist[a['index']]
            return 1
         else : 
            return 0


     def set_model_state(self, x):
         for k in self.statekeys :
              logging.debug("set_model_state: key %s, value %r ... ", k, x[k])
              self.model_set(k, x[k])
              logging.debug("set_model_state: done")
         return

 

     def set_model_input(self, a):
          self.model_set('env.noise0', a['value'])
          self.model_set('env.failures0', 0)
          return 

     # advance simulation
     def compute_next_state(self):
       self.model_next()
       return 

    # check if state is admissible
     def adm(self, x):
       return x['env.adm0']
 
   # check if state is unsafe
     def error(self, x):
       return x['monitor.y0']
 
    # Possible actions
    # def actions(self):
    #   return [-1, 0.0, 1]
 
    # find index with value val
    # def find_argval(self, x, val):
    #    for k in xrange(len(x)) :
    #          if (x[k] >= val) :
    #               return k
    #    return -1

#     def get_state_depth(self):
#          return self.state['depth0']      

#     def set_state_depth(self, depth):
#          self.state['depth0'] = depth


     def get_model_next_state(self, mytime, x, a):

# advance simulation
          logging.debug("get_model_next_state: begin")

          self.create_model()

          logging.debug("get_model_next_state: present state: %r", x)
          self.set_model_state(x)

          logging.debug("get_model_next_state: action: %r", a)
          self.set_model_input(a)

          logging.debug("get_model_next_state: time: %r", mytime)
          self.set_model_time(mytime)

          logging.debug("get_model_next_state: time %d, action %d", 
                       mytime['start'], a['value'])

          # compute next state
          self.model_next()
          
          y = self.get_model_state()

          logging.debug("get_model_next_state: new state: %r", y)

          return (y)


 
