
class Monitor

parameter Real T = 1;

parameter Integer x0 = 0

  Integer x1, x2;

initial equation

  x = x0;

equation

when sample(0, T) then

  if (pre(x) == 1) or ((x1 == 2) and (x2 == 2)) 
		     then x = 1;
  else x = 0;
end if;



end when;


end Monitor;
