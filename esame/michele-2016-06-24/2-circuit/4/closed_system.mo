model ClosedSystem
    Plant p;
    Boolean err;
initial equation
    err = false;
    p.u = 0;
equation
    p.u = 0;
    when p.y > 0.0 or p.y < 0.0 then
        err = true;
    end when;
end ClosedSystem;

