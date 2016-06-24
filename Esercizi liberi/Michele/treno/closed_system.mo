model ClosedSystem
    Treno t;
    Gate g;
    Controller c;
    Real speed;
initial equation
    speed = 30.0;
equation
    c.app = t.app;
    c.exit = t.exit;
    g.lower = c.lower;
    g.raise = c.raise;
    t.speed = speed;
    der(speed) = 0.0;
    when sample(0, 17) then
        if pre(speed) <= 40.0 then
            reinit(speed, 50.0);
        else
            reinit(speed, 30.0);
        end if;
    end when;
end ClosedSystem;

