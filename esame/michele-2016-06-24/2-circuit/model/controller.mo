class Controller
    parameter Real Tau = 1.0e-06; // sampling time

    Integer z;
    input Real r;
    output Integer w;
equation
    when sample(0, Tau) then
        z = F(pre(z), pre(r));
        w = F(pre(z), pre(r));
    end when;
end Controller;

function F
    input Integer z;
    input Real r;
    output Integer y;
algorithm
    if r >= 5.01 then
        y := 0;
    elseif r <= 4.99 then
        y := 1;
    else
        y := z;
    end if;
end F;

