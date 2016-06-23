class Gate
    parameter Real angle_start = 90;
    parameter Real speed_start = 0;
    parameter Real mode_start = 0;
    /* modes:
     * 0: open
     * 1: lowering
     * 2: raising
     * 3: closed
     **/
    Real angle(min = 0, max = 90);
    Real speed;
    Integer mode;
    input Boolean lower;
    input Boolean raise;
initial equation
    angle = angle_start;
    speed = speed_start;
    mode = mode_start;
equation
    der(angle) = speed;

    if (mode == 0) or (mode == 3) then
        speed = 0;
    elseif (mode == 1) then
        speed = -9;
    else
        speed = 9;
    end if;

    when lower then
        if pre(mode) <> 3 then
            mode = 1;
        else
            mode = pre(mode);
        end if;
    elsewhen raise then
        if pre(mode) <> 0 then
            mode = 2;
        else
            mode = pre(mode);
        end if;
    elsewhen angle >= 90.0 then
        reinit(angle, 90.0);
        mode = 0;
    elsewhen angle <= 0.0 then
        reinit(angle, 0.0);
        mode = 3;
    end when;

end Gate;

