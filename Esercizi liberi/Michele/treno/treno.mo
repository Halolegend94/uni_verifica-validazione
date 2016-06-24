class Treno
    parameter Real past = 100.0;
    parameter Real near = -1000.0;
    parameter Real pos_start = -2000.0;

    Real pos;
    input Real speed;
    output Boolean app;
    output Boolean exit;
initial equation
    pos = pos_start;
    app = false;
    exit = false;
equation
    der(pos) = speed;
    exit = pos >= past;
    app = (pos >= near) and (pos < 0.0);
    when pos >= 600.0 then
        reinit(pos, pos_start);
    end when;
end Treno;

