model ClosedSystem

   System s;
   Environment e;
   Monitor m;
   ECU ec;

equation
   s.x = m.x;
   ec.x = s.x;
   s.pOpen = ec.pOpen;
   e.d.riverLoad = s.riverLoad;

end ClosedSystem;
