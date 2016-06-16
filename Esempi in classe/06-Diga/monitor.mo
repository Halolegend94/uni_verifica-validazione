
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

z = (x >= k.Hmax) or (x <= k.Hmin);

if edge(z) 
then y = true;
else y = pre(y);
end if;



end Monitor;