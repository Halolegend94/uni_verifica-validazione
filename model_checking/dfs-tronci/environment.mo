
class Environment

constant Integer H = 4;

parameter Real T = 0.25;

parameter Real avg0 = 0;
parameter Boolean adm0  = true;
parameter Integer n0  = 0;
parameter Integer depth0  = 0;

parameter Integer noise0 = -1;
parameter Integer failures0  = 0;

Disturbance d;
State x,y;

function next
input State x;
input Disturbance d;
output State y;

algorithm

y.n := (x.n + 1);

y.avg := (x.n*x.avg + d.noise)/(x.n + 1);

y.depth := x.depth + 1;

if (x.adm and (y.avg >= -0.5) and (y.avg < 0.5) and (y.depth <= H))
   then y.adm := true;
   else y.adm := false;
end if;

end next;


initial equation

x.adm = adm0; 
x.avg = avg0;
x.n = n0;
x.depth = depth0;

d.noise = noise0;
d.failures = failures0;


equation




when sample(0, T) then

d.noise = pre(d.noise);
d.failures = pre(d.failures);

y.n = pre(x.n);
y.avg = pre(x.avg);
y.adm = pre(x.adm);
y.depth = pre(x.depth);

x = next(y, d);


end when;


end Environment;
