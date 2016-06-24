model ClosedSystem
    parameter Real wait_time = 0.01; // tempo di regime
    parameter Real alpha = 0.2;
    Plant p;
    Controller c;
    Boolean err;
initial equation
    err = false;
equation
    c.r = ad(p.y, -20, 20, 0.001);
    p.u = c.w;
    when p.y > 5 + alpha or p.y < 5 - alpha then
        if time > wait_time then
            err = true;
        else
            err = pre(err);
        end if;
    end when;
end ClosedSystem;

