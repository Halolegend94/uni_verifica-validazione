model System
   Plant p;

initial equation
   p.i_L = 0;
   p.v_O = 0;
equation
   p.u = 1;

end System;
