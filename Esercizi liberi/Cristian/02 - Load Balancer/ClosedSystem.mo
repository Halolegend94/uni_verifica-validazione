class ClosedSystem "The whole system"
   input Real noise;
   input Real failures;

   Monitor m;
   System s;
   Environment e;

equation
   s.d.noise = e.d.noise;
   s.d.failures = e.d.failures;
   m.x = s.x;

end ClosedSystem;
