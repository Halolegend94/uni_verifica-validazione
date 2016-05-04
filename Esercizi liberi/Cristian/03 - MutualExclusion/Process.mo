class Process

   Integer state;
   Integer otherProcessState;
   Integer turn;
   parameter Integer ID = 0;
   parameter Integer initState = 0;
   parameter Integer T = 1;

   /*compute next state of the process. Would be nice to have this task outside of the process!*/
   function nextState
      input Integer myID;
      input Integer currentState;
      input Integer otherProcessState;
      input Integer turn;
      output Integer newState;

   algorithm
      if(currentState == 0) then newState := 1; //go waiting
      else if(currentState == 1 and turn == myID
          and otherProcessState != 2) then newState := 2; //go critical section
      else if(currentState == 2) then newState := 0; //go outside the critical section
      else newState := currentState; //else don't move
      end if;
   end nextState;

initial equation
   state = initState;

equation
   when sample(0, T) then
      state = nextState(ID, pre(state), otherProcessState, turn);
   end when;

end Process;
