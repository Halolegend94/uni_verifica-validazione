model ECU

   parameter Real T = 20;
   parameter Integer pOpen0 = 0;
   constant Real xMin = 50; //measured in Kl
   constant Real xMax = 1050;
   output Integer pOpen;
   input Real x; //water level
   Real quantX;
   parameter Real quantX0 = 500;

function ad
   input Real x;
   output Real y;
   constant Integer Delta = 50;

algorithm
   if x > xMax then
      y:= xMax;
   elseif x < xMin then
      y:= xMin;
   else
      y := Delta*(floor(x / Delta) + 0.5);
   end if;
end ad;

initial equation
   pOpen = pOpen0;
   quantX = quantX0;
equation
   when sample(0, T) then
      quantX = ad(x);
      /*algoritmo qui*/
      if(quantX > 800) then
         pOpen = 1;
      elseif(quantX < 200) then
          pOpen = 0;
      else pOpen = pre(pOpen);
      end if;
      /*Domande. Possiamo misurare solo x o anche i disturbi ?*/
   end when;
end ECU;
