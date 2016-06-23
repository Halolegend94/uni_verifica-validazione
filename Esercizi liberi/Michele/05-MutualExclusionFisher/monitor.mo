
class Monitor
    parameter Boolean error_start = false;

    Boolean error;

    input ProcessState state1;
    input ProcessState state2;
initial equation
    error = error_start;
equation
    when state1 == ProcessState.InsideCS and state2 == ProcessState.InsideCS then
        error = true;
    end when;
end Monitor;

