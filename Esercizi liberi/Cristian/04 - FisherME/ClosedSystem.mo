class ClosedSystem

   SharedMemory mem;
   Process proc1(ID = 1);
   Process proc2(ID = 2);

equation
   mem.kw1 = proc1.kw;
   mem.kw2 = proc2.kw;
   /*mem.reset1 = proc1.reset;
   mem.reset2 = proc2.reset;*/
   proc1.kr = mem.kr;
   proc2.kr = mem.kr;

end ClosedSystem;
