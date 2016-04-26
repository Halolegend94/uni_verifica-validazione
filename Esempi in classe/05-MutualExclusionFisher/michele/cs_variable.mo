class CSVariable
    constant Real Tau;

    parameter Integer turn_start = 0;

    input Integer turn1;
    input Integer turn2;

    output Integer turn;
initial equation
    turn = turn_start;
equation
    when sample(Tau/2, Tau) then
        if pre(turn1) > pre(turn2) then
            turn = pre(turn1);
        elseif pre(turn2) > 0 then
            turn = pre(turn2);
        else
            turn = 0;
        end if;
    end when;
end CSVariable;

