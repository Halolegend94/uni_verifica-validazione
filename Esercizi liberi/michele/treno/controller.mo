class Controller
    parameter Real Tau = 1;

    parameter Real wait_time = 2.0;

    parameter Integer mode_start = 0;
    parameter Real timer_start = 0.0;
    /*
     * 0: idle
     * 1: about to lower
     * 2: about to raise
     */
    Integer mode;
    Real timer;
    Boolean pre_app;
    Boolean pre_exit;
    input Boolean app;
    input Boolean exit;
    output Boolean lower;
    output Boolean raise;
initial equation
    mode = mode_start;
    timer = timer_start;
    pre_app = false;
    pre_exit = false;
equation
    if (mode == 1) or (mode == 2) then
        der(timer) = 1;
    else
        der(timer) = 0;
    end if;

    when sample(0, Tau) then
        pre_app = pre(app);
        pre_exit = pre(exit);
        if app and (pre(pre_app) <> app) then
            reinit(timer, 0);
            mode = 1;
            lower = false;
            raise = false;
        elseif exit and (pre(pre_exit) <> exit) then
            reinit(timer, 0);
            mode = 2;
            lower = false;
            raise = false;
        elseif timer >= wait_time then
            reinit(timer, 0);
            mode = 0;
            if pre(mode) == 1 then
                lower = true;
                raise = false;
            elseif pre(mode) == 2 then
                lower = false;
                raise = true;
            else
                raise = false;
                lower = false;
            end if;
        else
            mode = pre(mode);
            lower = false;
            raise = false;
        end if;
    end when;
end Controller;

