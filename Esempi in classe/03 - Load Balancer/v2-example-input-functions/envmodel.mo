
class Environment


parameter Real T = 2;

parameter Real avg0 = 0;
parameter Boolean adm0  = true;
parameter Integer n0  = 0;
parameter Integer depth0  = 0;
parameter Boolean monitor0  = false;

parameter Integer noise0 = 0;
parameter Integer failures0  = 0;

Disturbance d;
State x,y;

constant Integer H = 5;


function next
input State x;
input Disturbance d;
output State y;

algorithm

y.n := (x.n + 1);

y.avg := (x.n*x.avg + d.noise)/(x.n + 1);

y.depth := x.depth + 1;

if (x.adm and (y.avg >= -0.7) and (y.avg < 0.7) and (y.depth <= H))
   then y.adm := true;
   else y.adm := false;
end if;

y.monitor := false;

end next;


initial equation

x.adm = adm0; 
x.avg = avg0;
x.n = n0;
x.depth = depth0;
x.monitor = monitor0;

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
y.monitor = pre(x.monitor);

x = next(y, d);


end when;


end Environment;