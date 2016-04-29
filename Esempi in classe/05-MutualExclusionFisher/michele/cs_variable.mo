class CSVariable
    constant Real Tau;

    parameter Integer turn_start = 0;

    input Integer turn1;
    input Integer turn2;
    Boolean turn1_exit;
    Boolean turn1_enter;
    Boolean turn2_exit;
    Boolean turn2_enter;

    output Integer turn;
initial equation
    turn = turn_start;
equation
    turn1_exit  = (turn1 == 0);
    turn1_enter = (turn1 == 1);
    turn2_exit  = (turn2 == 0);
    turn2_enter = (turn2 == 2);
    when edge(turn1_exit) or edge(turn1_enter) then
        turn = turn1;
    elsewhen edge(turn2_exit) or edge(turn2_enter) then
        turn = turn2;
    end when;
end CSVariable;

