class Controller
   input Real r;
   output Integer w;

   Integer z;
   parameter Real T = 1.0e-6;
equation

   when sample(0, T) then
      z = F(pre(z), pre(r));
      w = F(pre(z), pre(r));
   end when;

end Controller;

function F
   input Integer z;
   input Real r;
   output Integer x;

algorithm
   if r >= 5.01 then
      x := 0;
   elseif r <= 4.99 then
      x := 1;
   else
      x := z;
   end if;
end F;
