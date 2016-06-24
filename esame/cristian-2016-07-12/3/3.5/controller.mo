
class Controller


   parameter Real T = 1e-2;
   input Real x;
   output Integer u;

   Real sensor;

initial equation

   u = 0;
   pre(u) = 0;

equation


   when sample(0, T) then

      sensor = AD(x);

      if (sensor <= 9)
         then u = 1;
      elseif (sensor >= 9.5)
         then u = 0;
      else
         u = pre(u);
      end if;

   end when;

end Controller;
