class GateTest
    Gate g;
    Boolean signal;
initial equation
    signal = false;
equation
    g.lower = signal;
    g.raise = not signal;
    when sample(0, 16) then
        signal = not pre(signal);
    end when;
end GateTest;

