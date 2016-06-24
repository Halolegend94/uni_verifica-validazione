class System
   Missile m;
   Monitor mo;

equation
   m.h = mo.h;
   m.v = mo.v;
   mo.m = m.m;
   m.u = 0;

end System;
