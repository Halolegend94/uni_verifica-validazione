class System
   Missile m;
   Monitor mo;

equation
   m.h = mo.h;
   m.v = mo.v;
   m.u = 2 * m.m0 * m.g;
   m.m = mo.m;
end System;
