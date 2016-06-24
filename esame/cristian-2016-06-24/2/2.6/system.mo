model System

   Plant p;
   Controller c;
   constant Real alpha = 0.9;
   parameter Real startup_time = 0.03;
   Boolean b;
   Boolean v;

initial equation
   p.i_L = 0;
   pre(v) = false;
   p.v_O = 0;
equation
   c.w =p.u;
   c.r = AD(p.y);
   if time < startup_time then
      b = false;
   else
      b = (p.y <=  5 - alpha or p.y >= 5 + alpha);
   end if;
   if edge(b) then
      v = true;
   else
      v = pre(v);
   end if;
end System;
