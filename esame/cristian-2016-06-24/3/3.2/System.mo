class System
   Missile m;
   Monitor mo;

equation
   m.h = mo.h;
   m.v = mo.v;
   m.u = 0;
   mo.m = m.m;

end System;
