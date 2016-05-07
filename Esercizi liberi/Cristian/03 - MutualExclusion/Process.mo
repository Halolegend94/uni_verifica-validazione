/*global definition*/
type ProcessState = enumeration(outside, waiting, inside);

class Process
   parameter Integer ID = 0;
   parameter Real T = 1;
   ProcessState myState;
   ProcessState otherProcessState;
   Integer turn;

   function nextState
      input ProcessState currentState;
      input ProcessState otherProcState;
      input Integer ID;
      input Integer turn;
      output ProcessState newState;

   algorithm
      if(currentState ==  ProcessState.outside) then
         newState :=  ProcessState.waiting;
      elseif(currentState ==  ProcessState.waiting and turn == ID) then
         newState :=  ProcessState.inside;
      elseif(currentState ==  ProcessState.inside) then
         newState :=  ProcessState.outside;
      else
         newState := currentState;
      end if;

   end nextState;

initial equation
   myState =  ProcessState.outside;

equation
   when sample(0, T) then
      myState = nextState(pre(myState), pre(otherProcessState), ID, pre(turn));
   end when;

end Process;
