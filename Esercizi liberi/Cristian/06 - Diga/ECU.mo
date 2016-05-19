model ECU

   parameter Real T = 1;
   output Integer pOpen;
   input Real x; //water level

equation
   when sample(0, T) then
      /*algoritmo qui*/
      if(x > 800) then
         pOpen = 1;
      elseif(x < 200) then
          pOpen = 0;
      else pOpen = pre(pOpen);
      end if;
      /*Domande. Possiamo misurare solo x o anche i disturbi ?*/
   end when;

end ECU;
