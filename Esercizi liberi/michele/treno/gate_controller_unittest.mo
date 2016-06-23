class GateControllerTest
    Controller c;
    Gate g;
    Boolean app;
    Boolean exit;
    Integer count;
initial equation
    app = false;
    exit = false;
    count = 0;
equation
    g.lower = c.lower;
    g.raise = c.raise;
    c.app = app;
    c.exit = exit;
    when sample(0, 17) then
        if pre(count) == 2 then
            count = 0;
            app = false;
            exit = false;
        elseif pre(count) == 1 then
            count = 2;
            app = false;
            exit = true;
        else
            count = 1;
            app = true;
            exit = false;
        end if;
    end when;
end GateControllerTest;


