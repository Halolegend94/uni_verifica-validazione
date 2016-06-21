
class System

input Real A;
input Real B;
input Real C1;
input Real C2;

Process p1(pid=1,v=-0.2,c=C1,a=A,b=B);
Process p2(pid=2,v=0.1,c=C2,a=A,b=B);
Store M;
Monitor P;

equation

M.k1 = p1.kw;
M.k2 = p2.kw;
M.k = p1.kr;
M.k = p2.kr;
P.m1 = p1.m;
P.m2 = p2.m;



end System;