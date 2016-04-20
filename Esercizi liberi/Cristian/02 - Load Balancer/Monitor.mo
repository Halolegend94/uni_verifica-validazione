class Monitor "This class represents the monitor of the system"

   parameter Real startUpTime = 1; //1 sec of startup time
   parameter Boolean y0 = false; //at the beginning, we can't say if there is an error
   parameter Integer T = 1; //1 sec. Note that this sampling rate is less than the one in the environment.
   Real x; //this is the load from the system
   Boolean y; //the signal that is 1 iff the system never enters in an invalid state

initial equation
   y = y0;

equation

   when sample(0, T) then
      if((pre(y) or abs(x) > 0.1)  and time > startUpTime) then
         y = true;
      else
         y = false;
      end if;
   end when;

end Monitor;
