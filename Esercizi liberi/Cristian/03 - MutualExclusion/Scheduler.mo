class Scheduler "This is the Scheduler of the system"

   Integer turn;
   ProcessState state1;
   ProcessState state2;
   parameter Integer T = 1;

   function computeTurn

      input Integer oldturn;
      input ProcessState state1;
      input ProcessState state2;
      output Integer newTurn;

   algorithm
      newTurn:= oldturn;
      if(oldturn == 1 and state1 ==  ProcessState.outside) then
         newTurn := 2;
      elseif(oldturn == 2 and state2 ==  ProcessState.outside) then
         newTurn := 1;
      end if;

   end computeTurn;

initial equation
   turn = 1;

equation
   when sample(0, T) then
      turn = computeTurn(pre(turn), state1, state2);
   end when;

end Scheduler;
