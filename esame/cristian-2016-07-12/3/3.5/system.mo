
class System

   fifo f;
   Monitor m;
   Controller c;
   input Real vr, vw;

equation
   f.x = m.z;
   f.v_read = vr;
   f.v_write = vw;
   c.x = f.x;
   f.u = c.u;

end System;
