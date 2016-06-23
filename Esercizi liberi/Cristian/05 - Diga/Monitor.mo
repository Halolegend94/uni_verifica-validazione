model Monitor

   parameter Integer LevelMin = 100;
   parameter Integer LevelMax = 1000;
   parameter Boolean y0 = false;
   parameter Boolean z0 = false;
   input Real x; //water level
   output Boolean y; //is unsafe ?
   Boolean z;
initial equation
   y = y0;
   z = z0;
   pre(y) = false;
   pre(z) = false;
equation
   z = (x < LevelMin or x > LevelMax);
   if edge(z) then
      y = true;
   else
      y = pre(y);
   end if;
end Monitor;
