class Scheduler "This is the Scheduler of the system"

   Integer turn;
   parameter Integer turn0 = 1;
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
      if(oldturn == 1 and //to avoid starvation
         state1 == ProcessState.outside and state2 == ProcessState.waiting) then
         newTurn := 2;
      elseif(oldturn == 2 and state2 == ProcessState.outside and
         state1 == ProcessState.waiting) then
         newTurn := 1;
      end if;

   end computeTurn;

initial equation
   turn = turn0;

equation
   when sample(0, T) then
      turn = computeTurn(pre(turn), state1, state2);
   end when;

end Scheduler;
