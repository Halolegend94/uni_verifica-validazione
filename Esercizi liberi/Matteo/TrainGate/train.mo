model Train
   parameter Real T = 1;
   parameter Real x0 = -1000;
   

   Real x; //Posizione
   input Real v; //Velocità in input

initial equation
   x = x0;

equation
   der(x) = v;
end Train;
