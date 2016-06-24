model train

   parameter Real x0 = -1000;
   parameter Real far = -1000;
   parameter Real past = 100;
   parameter far_vmax = 50;
   parameter far_min = 40;
   parameter near_vmax = 50;
   parameter near_vmin = 30;
   parameter past_vmax = 50;
   parameter past_vmin = 30;

   Real x; //Posizione
   input Real v; //Velocità in input
   Integer m; //modo

initial equation
   x = x0;

equation
   der(x) = v;

   /*if(x <= far) then
      m = 0;
   else if(x > 100) then
      m = 2;
   else
      m = 1;
   end if;*/

end train;
