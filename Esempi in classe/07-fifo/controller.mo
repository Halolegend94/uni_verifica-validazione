
class Controller

// 1L = 10^{-3} m3
// 1000L = 1 m3


Constants k;

parameter Real T = 1;

// ad conversion parameters
input Real Delta = 0.01;  // 1 KL 
input Real LoVal = 0;
input Real HiVal = 6;

input Real x;  // FIFO bits
output Integer u;  // u=0 dam gate (bulkhead) closed, u=1 bulkhead opened

Real sensor;

initial equation

u = 0;
pre(u) = 0;

equation

// Threshold = (k.Hmin + k.Hmax)/2;  // KL

when sample(0, T) then

sensor = ad(Delta, LoVal, HiVal, x);

if (sensor <= 3) 
then u = 1;
else if (sensor >= 4) 
      then u = 0;
      else u = pre(u);
      end if;
end if;

end when ;


end Controller;




