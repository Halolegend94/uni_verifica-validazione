class Monitor

   input ProcessState state1;
   input ProcessState state2;
   Boolean y, z;

initial equation
   pre(y) = false;
   pre(z) = false;
equation
   z = (state1 == ProcessState.insideCS and state2 == ProcessState.insideCS);
   if edge(z) then
      y = true;
   else
      y = pre(y);
   end if;

end Monitor;
