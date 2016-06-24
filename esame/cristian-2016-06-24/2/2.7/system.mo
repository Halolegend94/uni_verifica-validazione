model System

   Plant p;
   Controller c;
   constant Real alpha = 0.2;
   parameter Real startup_time = 0.01;
   Boolean b;
   Boolean v;
   parameter Real p1 = 0;
   parameter Real p2 = 0;
initial equation
   p.i_L = p1;
   pre(v) = false;
   p.v_O = p2;
equation
   c.w =p.u;
   c.r = AD(p.y);

   //monitor
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
