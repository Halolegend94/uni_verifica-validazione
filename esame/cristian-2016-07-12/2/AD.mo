function AD
   input Real y;
   output Real r;
   constant Real Delta = 0.001;
   parameter Integer xMax = 20;
   parameter Integer xMin = -20;

algorithm
   if y > xMax then
      r := xMax;
   elseif y < xMin then
      r := xMin;
   else
      r := Delta*(floor(y / Delta) + 0.5);
   end if;

end AD;
