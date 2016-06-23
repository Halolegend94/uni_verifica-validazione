/*global definition*/
type ProcessState = enumeration(outside, waiting, inside);

model Process

   parameter Integer ID = 0;
   parameter ProcessState myState0 = ProcessState.outside;
   parameter Real T = 1;
   ProcessState myState;
   input ProcessState otherProcessState;
   input Integer turn;

   function nextState
      input ProcessState currentState;
      input ProcessState otherProcState;
      input Integer ID;
      input Integer turn;
      output ProcessState newState;

   algorithm
      if(currentState ==  ProcessState.outside) then
         newState :=  ProcessState.waiting;
      elseif (currentState ==  ProcessState.waiting and otherProcState == ProcessState.outside) or
         (currentState ==  ProcessState.waiting and turn == ID) then
         newState :=  ProcessState.inside;
      elseif(currentState ==  ProcessState.inside) then
         newState :=  ProcessState.outside;
      else
         newState := currentState;
      end if;

   end nextState;

initial equation
   myState =  myState0;

equation
   when sample(0, T) then
      myState = nextState(pre(myState), pre(otherProcessState), ID, pre(turn));
   end when;

end Process;
