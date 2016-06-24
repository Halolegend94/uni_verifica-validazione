model ClosedSystem
    Plant p;
    Boolean err;
initial equation
    err = false;
    p.u = 1;
equation
    p.u = 1;
    when p.y > p.V_i or p.y < p.V_i then
        if time > 0.01 then
            err = true;
        else
            err = pre(err);
        end if;
    end when;
end ClosedSystem;

