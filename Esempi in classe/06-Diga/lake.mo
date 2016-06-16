
class Lake

// 1KL = 1 m3

parameter Real EProd = 1.0;  // KL/sec
parameter Real Popen = 10.0;  // KL/sec
parameter Real x0 = 550.0;  // KL

input Real p;  // portata 1-10  KL/sec
input Integer u;

// water volume x = S*z, where: S lake average surface, z water level

Real x;   // water in lake


initial equation
x = x0;

equation

der(x) = p - EProd - Popen*u;


end Lake;




