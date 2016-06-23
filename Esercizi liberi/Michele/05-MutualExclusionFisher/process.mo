/* process model */
type ProcessState = enumeration(DontCare, DidTest, DidSet, InsideCS);

class Process
    constant Real Tau;

    constant Integer id;

    constant Real test_time(min=0.0);
    constant Real set_time(min=0.0);

    constant Real min_drift(min=0.0);
    constant Real max_drift(min=0.0);

    parameter ProcessState state_start = ProcessState.DontCare;
    parameter Real process_time_start  = 0.0;

    output ProcessState state;
    Real process_time;
    input Integer turn;
    output Integer new_turn;
    input Real process_drift(min=-min_drift, max=max_drift);
    input Boolean fire_transition;

initial equation
    state = state_start;
    process_time = process_time_start;
equation
    when sample(0, Tau) then
        if pre(state) == ProcessState.DontCare then
            if not (true) or (pre(fire_transition) and turn == 0) then
                state    = ProcessState.DidTest;
                new_turn = pre(new_turn);
                reinit(process_time, 0.0);
            else
                state    = pre(state);
                new_turn = pre(new_turn);
            end if;
        elseif pre(state) == ProcessState.DidTest then
            if (pre(process_time) > test_time) or (pre(fire_transition) and true) then
                state    = ProcessState.DidSet;
                new_turn = id;
                reinit(process_time, 0.0);
            else
                state    = pre(state);
                new_turn = pre(new_turn);
            end if;
        elseif pre(state) == ProcessState.DidSet then
            if not (true) or (pre(fire_transition) and pre(process_time) >= set_time and pre(turn) == id) then
                state    = ProcessState.InsideCS;
                new_turn = pre(new_turn);
            elseif not (true) or (pre(fire_transition) and pre(process_time) >= set_time and pre(turn) <> id) then
                state    = ProcessState.DontCare;
                new_turn = -1;
            else
                state    = pre(state);
                new_turn = pre(new_turn);
            end if;
        else
            if not (true) or (pre(fire_transition) and true) then
                state    = ProcessState.DontCare;
                new_turn = 0;
            else
                state    = pre(state);
                new_turn = pre(new_turn);
            end if;
        end if;
    end when;
    der(process_time) = 1.0 + process_drift;
end Process;
