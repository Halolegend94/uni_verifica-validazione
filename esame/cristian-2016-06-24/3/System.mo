class ClosedSystem

   Controller c;

   Missile m;
   Monitor mo;

equation
   m.h = c.h;
   m.u = c.u;
   m.m  = c.m;
   mo.h = m.h;
   mo.v = m.v;
   mo.m = m.m;


end ClosedSystem;
