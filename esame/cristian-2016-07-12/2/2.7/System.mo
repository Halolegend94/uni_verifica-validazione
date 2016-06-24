model System
   Controller c;
   Plant p;

initial equation
   p.i_L = 0;
   p.v_O = 0;

equation
   c.r = AD(p.y);
   p.u = 1;

end System;
