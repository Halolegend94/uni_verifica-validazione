/*define process states*/
type ProcessState = enumeration(outsideCS, request, waiting, insideCS);
class Process

   parameter Real T = 1.2;         //timestep
   parameter Integer ID = 1;
   parameter Integer a = 9, b = 3, c = 8; //c = tempo di permanenza nello stato 1 e 4
   Real ptime;
   Integer kr;
   Integer kw;
   Real drift;
   ProcessState myState;
   Boolean ga, gb, gc;
initial equation
   myState = ProcessState.outsideCS;
   ptime = 0;
   kw = 0;

equation
   der(ptime) = 1 + drift;
   gc = ptime > c;
   ga = ptime > a;
   gb = ptime > b;
   when sample(0, T) then
      if pre(myState) == ProcessState.outsideCS and pre(kr) == 0 and gc then
         reinit(ptime, 0);
         myState = ProcessState.request;
         kw = pre(kw);
      elseif (pre(myState) == ProcessState.request and ga) then
         kw = ID;
         reinit(ptime, 0);
         myState = ProcessState.waiting;
      elseif (pre(myState) == ProcessState.waiting and gb) then
         if (pre(kr) == ID) then
            kw = pre(kw);
            myState = ProcessState.insideCS;
            reinit(ptime, 0);
         else
            kw = pre(kw);
            reinit(ptime, 0);
            myState = ProcessState.outsideCS;
         end if;
      elseif(pre(myState) == ProcessState.insideCS and gc) then
         myState = ProcessState.outsideCS;
         reinit(ptime, 0);
         kw = 0;
      else
         myState = pre(myState);
         kw = pre(kw);
      end if;
   end when;

end Process;
