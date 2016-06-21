
class Monitor

parameter Real T = 1;

parameter Boolean y0 = false;

Integer m1, m2;
Boolean z, y;

initial equation
y = y0;
z = false;
pre(z) = false;
pre(y) = y0;

equation

z = ((m1 == 4) and (m2 == 4));

if edge(z) 
then y = true;
else y = pre(y);
end if;



end Monitor;