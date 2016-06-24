function AD
   input Real y;
   output Real r;
   constant Real Delta = 0.5;
   parameter Integer xMax = 999990;
   parameter Integer xMin = 0;

algorithm
   if y > xMax then
      r := xMax;
   elseif y < xMin then
      r := xMin;
   else
      r := Delta*(floor(y / Delta) + 0.5);
   end if;

end AD;
