class Monitor
    input Real h;
    input Real v;
    output Boolean landed;
    output Boolean err;
    output Boolean controller_err;
initial equation
    err = false;
equation
    landed = h <= 0.0;
    when landed then
        if abs(v) > 10.0 then
            err = true;
        else
            err = pre(err);
        end if;
    end when;
    controller_err = err or not landed;
end Monitor;

