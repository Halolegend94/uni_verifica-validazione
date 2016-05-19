class SharedMemory

   Integer kw1;
   Integer kw2;
   Boolean reset1;
   Boolean reset2;
   Boolean set1;
   Boolean set2;
   Integer kr;
   parameter Integer k0 = 0;
   parameter Real T = 1;

initial equation
   kr = k0;
   reset1 = true;
   reset2 = true;

equation

   reset1 = kw1 == 0;
   reset2 = kw2 == 0;
   set1 = kw1 == 1;
   set2 = kw2 == 2;
   when edge(set1) or edge(reset1) then
      kr = kw1;
   elsewhen edge(set2) or edge(reset2) then
      kr = kw2;
   end when;

end SharedMemory;
