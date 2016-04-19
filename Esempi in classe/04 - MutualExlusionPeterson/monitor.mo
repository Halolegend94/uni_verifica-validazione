
class System

constant Real omega = 2*3.14*10;

parameter Real a = 1;
parameter Real x0 = 1;

parameter Real k0 = 100;
parameter Real k1 = 10;
parameter Real k2 = 10;

Real noise;
Real failures;

Real x;
Real u;
Real z;

initial equation

x = x0;
z = 0;
// noise = 0;
// failures = 0;


equation

failures = 1*sin(omega*time);

der(x) = a*x + u + noise + failures;

der(z) = 0 - x;  // integral of error

u = k0*(0 - x) + k1*z - k2*der(x);


end System;