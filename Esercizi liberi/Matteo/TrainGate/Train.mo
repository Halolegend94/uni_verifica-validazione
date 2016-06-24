model Train
   parameter Real x0 = -1000; //posizione iniziale
   parameter Real len = 50; //lunghezza treno

   Real x; //Posizione
   input Real v; //Velocità in input come disturbo

initial equation
   x = x0;

equation
   der(x) = v;
end Train;
