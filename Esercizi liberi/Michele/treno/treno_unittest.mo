class TrenoTest
    Treno t;
    Real speed;
initial equation
    speed = 30.0;
equation
    t.speed = speed;
    der(speed) = 0.0;
    when sample(0, 17) then
        if pre(speed) <= 30.0 then
            reinit(speed, 50.0);
        else
            reinit(speed, 30.0);
        end if;
    end when;
end TrenoTest;

