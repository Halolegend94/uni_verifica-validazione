
class Store


Integer k;
Integer k1;
Integer k2;


Boolean g1k1, g2k1, g1k0, g2k0;

initial equation

k1 = 0;
k2 = 0;
k = 0;
pre(k) = 0;
pre(g1k1) = false;
pre(g2k1) = false;
pre(g1k0) = false;
pre(g2k0) = false;

equation

//when sample(0, 0.5) then
//k1 = 1 - pre(k1);
//end when;

//when sample(0, 0.8) then
//k2 = 1 - pre(k2);
//end when;


g1k1 = (k1 >= 1);
g2k1 = (k2 >= 1);
g1k0 = (k1 <= 0);
g2k0 = (k2 <= 0);

/*
if (k1 >= 1)  // edge(g1k1)
then k = 1; 
else if (k2 >= 2) // edge(g2k1)
     then k = 2; 
     else if (k1 <= 0)  // edge(g1k0)
          then k = 0; 
          else if (k2 <= 0)  // edge(g2k0)
               then k = 0; 
               else k = pre(k); 
               end if;
          end if;
      end if;
end if;
*/




if (not (k1 == pre(k1)))  
then k = k1; 
else if (not (k2 == pre(k2))) 
     then k = k2; 
     else k = pre(k); 
     end if;
end if;


end Store;




