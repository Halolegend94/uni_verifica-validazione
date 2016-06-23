model ClosedSystem "The whole system"

   input Real noise;
   input Real failures;

   Monitor m;
   System s;
   //Environment e;

equation
   s.d.noise = noise;
   s.d.failures = failures;
   m.x = s.x;

end ClosedSystem;
