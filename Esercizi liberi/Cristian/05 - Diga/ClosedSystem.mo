model ClosedSystem

   System s;
   //Environment e;
   Monitor m;
   ECU ec;

   input Real riverLoad;

equation
   s.x = m.x;
   ec.x = s.x;
   s.pOpen = ec.pOpen;
   riverLoad = s.riverLoad;

end ClosedSystem;
