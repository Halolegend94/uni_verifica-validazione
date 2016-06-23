class ClosedSystem

   SharedMemory mem;
   Process proc1(ID = 1, c=8);
   Process proc2(ID = 2, c=11);
   Monitor m;
   Environment e(drift1_0 = -0.2, drift2_0 = 0.1);
   input Real drift1;
   input Real drift2;

equation
   mem.kw1 = proc1.kw;
   m.state1 = proc1.myState;
   m.state2 = proc2.myState;
   mem.kw2 = proc2.kw;
   proc1.drift = drift1;
   proc2.drift = drift2;
   /*
   proc1.drift = e.d.drift1;
   proc2.drift = e.d.drift2;*/
   proc1.kr = mem.kr;
   proc2.kr = mem.kr;

end ClosedSystem;
