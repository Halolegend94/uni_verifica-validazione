
class Process

parameter Integer pid = 1;
parameter Real a_max = 1;
parameter Real b_max = 3;
parameter Real c_max = 5;
parameter Real a = 1;
parameter Real b = 2;
parameter Real c = 3;  // max soujourn time in a mode
parameter Real v = 0.1;  

parameter Real x0 = 0;
parameter Real m0 = 1;
parameter Real k0 = 0;

Integer kr, kw;

Integer m;
Real x;
Boolean ga, gb, gc;

initial equation

x = x0;
m = m0;
kr = 0;
kw = 0;
pre(kr) = 0;
pre(kw) = 0;
pre(m) = m0;
pre(ga) = false;
pre(gb) = false;
pre(gc) = false;

equation

if (m == 1) 
then  der(x) = 1 + v;
else 
     if (m == 2) 
     then der(x) = 1 + v;
     else 
          if (m == 3) then der(x) = 1 + v;
          else der(x) = 1 + v;  // m == 4
          end if;
     end if;
end if;

ga = (x > a);
gb = (x > b);
gc = (x > c);


// reset of x
when (((pre(m) == 1) or (pre(m) == 4)) and gc) or 
     (((pre(m) == 2) and ga)) or
     ((pre(m) == 3) and gb) 
then
reinit(x, 0);
end when;

// reset of k
if ((pre(m) == 2) and edge(ga)) 
then  kw = pid;
else  
      if ( ((pre(m) == 4) and edge(gc)) 
           //  or ((pre(m) == 3) and (not (pre(kr) == pid)) and  edge(gb)) 
         )
      then  kw = 0;
      else  kw = pre(kw);
      end if;
end if;

// mode transitions
if (pre(m) == 1) 
then if (edge(gc))
     then if (pre(kr) == 0) then m = 2; else m = 1; end if; 
     else m = pre(m);
     end if;
else
if (pre(m) == 2) 
then
     if edge(ga)
     then m = 3; 
     else m = pre(m);
     end if;
else
if (pre(m) == 3) 
then
     if edge(gb)
     then if (pre(kr) == pid) then m = 4; else m = 1; end if; 
     else m = pre(m); 
     end if;
else // (pre(m) == 4) 
     if edge(gc)
     then m = 1; 
     else m = pre(m);
     end if;
end if;  // (pre(m) == 3) 
end if;  // (pre(m) == 2) 
end if; // (pre(m) == 1)





end Process;




