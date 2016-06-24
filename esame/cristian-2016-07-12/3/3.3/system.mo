
class System

   fifo f;
   Monitor m;

equation
   f.x = m.z;
   f.v_read = 0.3;
   f.v_write = 0;
   f.u = 0;
   
end System;
