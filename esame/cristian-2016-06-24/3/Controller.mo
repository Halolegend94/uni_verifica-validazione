class Controller
   constant Real T = 0.125;

   input Real h;
   Real dh, preh;
   input Real m;
   output Real u;

function trust
   input Real h;
   input Real p_h;
   input Real m;
   output Real t;

   parameter Real f1 = 38000;
protected
   Real v, tmp;
algorithm
   v := -((p_h - h) / T);
   tmp :=  m * 9.81;

   if h >= 5000  then  //Altezza uno
      if v <= -100  then
         t := f1;
      elseif v >= -80 then
         t := 0;
      else
         t := if tmp > f1 then f1 else tmp;
      end if;

   elseif  h >= 500 then
      if  v <= -20 then
         t:= f1;
      elseif v >= -10 then
         t:= 0;
      else
         t := if tmp > f1 then f1 else tmp;
      end if;

   else
      if v < -10 then
         t:=f1;
      elseif v > -1 then
         t:= 0;
      else
         t := if tmp > f1 then f1 else tmp;
      end if;

   end if;
end trust;

equation
   when sample(0, T) then
      dh = AD(h);
      preh = pre(dh);
      u = trust(dh, preh, pre(m));
   end when;


end Controller;
