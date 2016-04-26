/* process model */
type ProcessState = enumeration(DontCare, DidTest, DidSet, InsideCS);

class Process
    constant Real Tau;

    parameter Integer id;

    parameter Real test_time(min=0.0);
    parameter Real set_time(min=0.0);

    parameter Real min_drift(min=0.0);
    parameter Real max_drift(min=0.0);

    parameter ProcessState state_start = ProcessState.DontCare;
    parameter Real process_time_start  = 0.0;

    output ProcessState state;
    Real process_time;
    discrete Real new_time;
    input Integer turn;
    output Integer new_turn;
    input Real process_drift(min=-min_drift, max=max_drift);
    input Boolean fire_transition;

    /* process transition function */
    function ProcessNext
        input Integer id;
        input Integer turn;
        input ProcessState state;
        input Real timer;
        input Boolean fire_transition;
        output ProcessState new_state;
        output Real new_timer;
        output Integer new_turn;
    algorithm
        new_state := state;
        new_timer := timer;
        new_turn := turn;
        if state == ProcessState.DontCare then
            if not (true) or (fire_transition and turn == 0) then
                new_state := ProcessState.DidTest;
                new_timer := 0;
            end if;
        elseif state == ProcessState.DidTest then
            if not (timer <= test_time) or (fire_transition and true) then
                new_state := ProcessState.DidSet;
                new_timer := 0;
                new_turn  := id;
            end if;
        elseif state == ProcessState.DidSet then
            if not (true) or (fire_transition and timer >= set_time and turn == id) then
                new_state := ProcessState.InsideCS;
            elseif not (true) or (fire_transition and timer >= set_time and turn <> id) then
                new_state := ProcessState.DontCare;
            end if;
        else
            if not (true) or (fire_transition and true) then
                new_state := ProcessState.DontCare;
                new_turn  := 0;
            end if;
        end if;
    end ProcessNext;

initial equation
    state = state_start;
    process_time = process_time_start;
equation
    when sample(Tau/2, Tau) then
        (state, new_time, new_turn) = ProcessNext(id, pre(turn), pre(state), pre(process_time), pre(fire_transition));
        reinit(process_time, new_time);
    end when;
    der(process_time) = 1.0 + process_drift;
end Process;


