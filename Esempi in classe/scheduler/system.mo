
/* critical section turn giver */
class TurnAssigner
    constant Real T;

    parameter Integer id;

    parameter Integer turn_start = 1;

    Integer turn;
    input ProcessState state1;
    input ProcessState state2;
    input Integer scheduler;
initial equation
    turn = turn_start;
equation
    when sample(T/2, T) then
        turn = TurnNext(pre(turn), pre(scheduler), id, pre(state1), pre(state2));
    end when;
end TurnAssigner;

/* turn assigner transition function */
function TurnNext
    input Integer turn;
    input Integer scheduler;
    input Integer id;
    input ProcessState state1;
    input ProcessState state2;
    output Integer new_turn;
algorithm
    new_turn := turn;
    if scheduler == id then
        if turn == 1 and state1 == ProcessState.DontCare and state2 == ProcessState.OutsideCS then
            new_turn := 2;
        elseif turn == 2 and state2 == ProcessState.DontCare and state1 == ProcessState.OutsideCS then
            new_turn := 1;
        end if;
    end if;
end TurnNext;

/* process model */
type ProcessState = enumeration(DontCare, OutsideCS, InsideCS);

class Process
    constant Real T;

    parameter Integer id;

    parameter ProcessState state_start = ProcessState.DontCare;

    output ProcessState state;
    input ProcessState other_state;
    input Integer scheduler;
    input Integer turn;
initial equation
    state = state_start;
algorithm
    when sample(T/2, T) then
        state := ProcessNext(id, pre(scheduler), pre(turn), pre(state), pre(other_state));
    end when;
end Process;

/* process transition function */
function ProcessNext
    input Integer id;
    input Integer scheduler;
    input Integer turn;
    input ProcessState state;
    input ProcessState other_state;
    output ProcessState new_state;
algorithm
    if scheduler == id then
        if state == ProcessState.DontCare then
            new_state := ProcessState.OutsideCS;
        elseif state == ProcessState.OutsideCS and other_state == ProcessState.DontCare then
            new_state := ProcessState.InsideCS;
        elseif state == ProcessState.OutsideCS and other_state == ProcessState.OutsideCS and turn == id then
            new_state := ProcessState.InsideCS;
        elseif state == ProcessState.InsideCS then
            new_state := ProcessState.DontCare;
        else
            new_state := state;
        end if;
    else
        new_state := state;
    end if;
end ProcessNext;

