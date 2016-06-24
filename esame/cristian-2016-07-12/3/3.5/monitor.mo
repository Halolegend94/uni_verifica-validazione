
class Monitor

   Real z;
   Boolean temp, y;

initial equation
   pre(temp) = false;
   pre(y) = false;

equation

   temp = (z > 10 or z < 0);

   if edge(temp) then
      y = true;
   else
      y = pre(y);
   end if;

end Monitor;
