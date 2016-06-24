model ClosedSystem

   Plant p;
   Controller c;

equation
   c.w =p.u;
   c.r = AD(p.y);

end ClosedSystem;
