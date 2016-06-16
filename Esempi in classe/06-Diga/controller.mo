
class Controller

// 1L = 10^{-3} m3
// 1000L = 1 m3


Constants k;

parameter Real T = 50;

parameter Real Threshold = (k.Hmin + k.Hmax)/2;  // KL

// ad conversion parameters
input Real Delta = 1;  // 1 KL 
input Real LoVal = 0;
input Real HiVal = 2*k.Hmax;

input Real x;  // water volume
output Integer u;  // u=0 dam gate (bulkhead) closed, u=1 bulkhead opened

Real sensor;

// Real Threshold;  // KL

// Constants k;

initial equation

// Threshold = (k.Hmin + k.Hmax)/2;  // KL

u = 0;
pre(u) = 0;

equation

// Threshold = (k.Hmin + k.Hmax)/2;  // KL

when sample(0, T) then

/*
if (ad(Delta, LoVal, HiVal, x) <= Threshold) 
then u = 0;
else u = 1;
end if;
*/

sensor = ad(Delta, LoVal, HiVal, x);

if (sensor <= 540) 
then u = 0;
else if (sensor >= 560) 
      then u = 1;
      else u = pre(u);
      end if;
end if;

end when ;


end Controller;




