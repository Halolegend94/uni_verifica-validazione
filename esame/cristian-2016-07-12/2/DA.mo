function DA
   input Real y;
   output Real r;
   constant Real Delta = 0.01;
   parameter Integer xMax = 1;
   parameter Integer xMin = 0;

algorithm
   if y > xMax then
      r := xMax;
   elseif y < xMin then
      r := xMin;
   else
      r := Delta*(floor(y / Delta) + 0.5);
   end if;

end DA;
