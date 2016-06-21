
class Monitor

Real x;  // lake water
Boolean z, y;

Constants k;


initial equation
y = false;
z = false;
pre(z) = false;
pre(y) = false;

equation

z = (x >= 5) or (x <= 0);

if edge(z) 
then y = true;
else y = pre(y);
end if;



end Monitor;