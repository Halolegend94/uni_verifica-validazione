class ClosedSystem

   SharedMemory mem;
   Process proc1(ID = 1);
   Process proc2(ID = 2);
   Environment e(drift1_0 = 0, drift2_0 = 0.6);

equation
   mem.kw1 = proc1.kw;
   mem.kw2 = proc2.kw;
   proc1.drift = e.d.drift1;
   proc2.drift = e.d.drift2;
   proc1.kr = mem.kr;
   proc2.kr = mem.kr;

end ClosedSystem;
