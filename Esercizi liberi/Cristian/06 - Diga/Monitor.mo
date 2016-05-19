model Monitor

   parameter Real T = 1;
   parameter Integer LevelMin = 100;
   parameter Integer LevelMax = 1000;
   parameter Boolean y0 = false;
   input Real x; //water level
   output Boolean y; //is unsafe ?

initial equation
   y = y0;

equation
   when sample(0, T) then
      if(pre(y) or  (x < LevelMin and x > LevelMax)) then
         y = true;
      else
         y = false;
      end if;

   end when;

end Monitor;
