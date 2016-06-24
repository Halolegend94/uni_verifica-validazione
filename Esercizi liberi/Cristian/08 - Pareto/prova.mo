class prova
   parameter Real p1 = 5;
   parameter Real p2 = 2;

   input Real i1;
   input Real i2;
   Real x;
   Boolean y;
   Boolean z;
initial equation
   pre(z) = false;
equation
   x = p1*i1 + p2*i2;
   y = x > 100;
   if edge(y) then
      z = true;
   else
      z = pre(z);
   end if;
end prova;
