model System "This model represents a dam"
   /*the unit measure is Kl */
   parameter Real x0 = 550; //water level
   parameter Integer pOpen0 = 0;
   parameter Real consumption = 1;
   parameter Real outflow = 10;
   input Integer pOpen;
   Real x; //water level, must be between 100 and 1000 Kl
   input Real riverLoad; //between 1 and 10 Kl/s
   
initial equation
   x = x0;
   pOpen = pOpen0;

equation
   der(x) = riverLoad - consumption -  pOpen*outflow;

end System;
