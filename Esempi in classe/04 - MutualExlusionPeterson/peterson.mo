
class Peterson

Integer k;

Monitor m;
Environment sck;
Process state1(id=1);
Process state2(id=2);
Turn q;



initial equation


equation

sck.d.sck = k;

state1.u = state2.x;
state1.turn = q.turn;
state1.k = k

state2.u = state1.x;
state2.turn = q.turn;
state2.k = k;

q.x1 =state1.x;
q.x2 = state2.x;
q.k = k;

m.x1 = state1.x;
m.x2 = state2.x;


end Peterson;