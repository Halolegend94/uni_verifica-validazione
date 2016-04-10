
class Monitor
    parameter Boolean y0 = false;
    Real x;
    Boolean y;
    Boolean properties[1];
initial equation
    y = y0;
equation
    properties[1] = abs(x) <= 0.1 or time <= .4;
    when not properties then
        y = true;
    end when;
end Environment;
