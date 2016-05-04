class Environment


parameter Real T = 1;

parameter Boolean adm0  = true;
parameter Integer n0  = 0;
parameter Integer depth0  = 0;
parameter Integer noise0 = 0;

Disturbance d;
State x,y;

constant Integer H = 5;


function next
input State x;
input Disturbance d;
output State y;

algorithm

y.n := x.n;

y.depth := x.depth + 1;

if (x.adm and (d.sck >= 1) and (d.sck <= 3) and (y.depth <= H))
then y.adm := true;
else y.adm := false;
end if;


end next;


initial equation

x.adm = adm0;
x.n = n0;
x.depth = depth0;
d.noise = noise0;



equation


when sample(0, T) then

d.noise = pre(d.noise);
d.failures = pre(d.failures);

y.n = pre(x.n);
y.adm = pre(x.adm);
y.depth = pre(x.depth);

x = next(y, d);


end when;


end Environment;
