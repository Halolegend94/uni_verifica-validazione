
class System

Controller ctr;
Lake lake;
Monitor monitor;

input Real p;

equation

lake.p = p;
lake.x = ctr.x;
lake.u = ctr.u;
monitor.x = lake.x;

end System;