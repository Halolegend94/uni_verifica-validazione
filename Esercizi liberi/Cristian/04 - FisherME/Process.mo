/*define process states*/
type ProcessState = enumeration(outsideCS, request, waiting, insideCS);
class Process

   parameter Integer T = 1;         //timestep
   parameter Integer ID = 1;
   parameter Integer a = 4, b = 7;
   Real timer;
   Integer kr;
   Integer kw;
   Real drift;
   ProcessState myState;

initial equation
   myState = ProcessState.outsideCS;
   timer = 0;
   kw = 0;

equation
   der(timer) = 1 + drift;

   when sample(0, T) then
      if pre(myState) == ProcessState.outsideCS and pre(kr) == 0 then
         myState = ProcessState.request;
         kw = pre(kw);
         reinit(timer, 0.0);
      elseif (pre(myState) == ProcessState.request and pre(timer) > a) then
         kw = ID;
         myState = ProcessState.waiting;
         reinit(timer, 0.0);
      elseif (pre(myState) == ProcessState.waiting and pre(timer) > b) then
         if (pre(kr) == ID) then
            kw = pre(kw);
            myState = ProcessState.insideCS;
         else
            kw = pre(kw);
            myState = ProcessState.outsideCS;
         end if;
      elseif(pre(myState) == ProcessState.insideCS) then
         myState = ProcessState.outsideCS;
         kw = 0;
      else
         myState = pre(myState);
         kw = pre(kw);
      end if;
   end when;

end Process;
