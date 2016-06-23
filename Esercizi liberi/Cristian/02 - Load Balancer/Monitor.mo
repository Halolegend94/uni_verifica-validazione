class Monitor "This class represents the monitor of the system"

   parameter Real startUpTime = 1; //1 sec of startup time
   parameter Boolean y0 = false; //at the beginning, we can't say if there is an error
   Real x; //this is the load from the system
   Boolean y; //the signal that is 1 iff the system never enters in an invalid state
   Boolean z;

initial equation
   pre(y) = false;

equation
   z = (abs(x) > 0.1  and time > startUpTime);
   if edge(z) then
      y = true;
   else
      y = pre(y);
   end if;


end Monitor;
