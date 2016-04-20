class System "this class models the system we have built"
   /*we can imagine that this system is a load balancer*/

   Real x; //load
   Real u; //action
   Real z; //integral of error
   Disturb d; //Disturb from the system and enviroment

   parameter Real x0 = 1;
   parameter Real u0 = 1;

   /*params used to compute the action. We need to chose them carefully.*/
   parameter Real k0 = 100;
   parameter Real k1 = 10;
   parameter Real k2 = 10;

   /*costants*/
   constant Real a = 1;
   constant Real omega = 10 * 3.14;

initial equation
   x = x0;
   u = u0;

equation
   d.failures = sin(omega * time);
   der(x) = a*x + u + d.noise + d.failures;
   der(z) = 0 - x;
   /*PID (proportional integrative derivative) MONITOR
   In this case we incorporate it right in the system since it's just one equation*/
   u = k0 * (0 - x) + k1 * z + k2 * der(x);
end System;
