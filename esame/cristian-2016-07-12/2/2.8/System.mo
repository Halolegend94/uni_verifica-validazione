model System
   Controller c;
   Plant p;
   parameter Real il = 0;
   parameter Real vo = 0;

initial equation
   p.i_L = il;
   p.v_O = vo;

equation
   c.r = AD(p.y);
   p.u = DA(c.w);
end System;
