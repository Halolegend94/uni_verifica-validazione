class prova// Bouncing ball
   parameter Real e=0.5 "Coefficient of restitution";
   Real  v;
   constant Real g = 9.18;

equation
   der(v) = 2;

   when sample (0, 5) then
      if pre(v) > 4 then
     reinit(v, 0); end if;
   end when;

end prova;
