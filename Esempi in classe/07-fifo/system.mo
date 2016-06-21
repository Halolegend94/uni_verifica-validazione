
class System

Controller ctr;
FIFO fifo;
Monitor monitor;

input Real p;

equation


fifo.p_out = p;
fifo.x = ctr.x;
fifo.u = ctr.u;
monitor.x = fifo.x;

end System;