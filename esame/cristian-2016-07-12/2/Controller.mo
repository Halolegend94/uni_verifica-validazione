class Controller
   parameter Real T = 1e-3;
   input Real r;
   output Real w;
   Real z;

   function F
      input Real z;
      input Real r;
      output Real s;

   algorithm

      if r >= 5.01 then
         s := z - 0.01;
      elseif r <= 4.99 then
         s := z + 0.01;
      else
         s := z;
      end if;

   end F;



equation
   when sample(0, T) then
      z = F(pre(z), pre(r));
      w = F(pre(z), pre(r));
   end when;

end Controller;
