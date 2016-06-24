
class Monitor

   Real z;
   input Real w;
   Boolean temp, y;

initial equation
   pre(temp) = false;
   pre(y) = false;

equation

   der(z) = -w;
   temp = (z < 0);

   if edge(temp) then
      y = true;
   else
      y = pre(y);
   end if;

end Monitor;
