class ClosedSystem "The whole system"

   Monitor m;
   System s;
   Environment e;
equation
   e.d = s.d;
   m.x = s.x;

end ClosedSystem;
