class Controller
    constant Real Tau = 0.125;

    parameter Real h_min = 0.0;
    parameter Real h_max = 999999999; // ??
    parameter Real h_res = 0.5;

    input Real h;
    Real pre_h_d;
    Real h_d;
    Real v_d;
    output Real u;

    constant Real h_1 = 1000;
    constant Real thrust_1 = 36000;
    constant Real v_1_max = 200;
    constant Real v_1_min = 10;

    constant Real h_2 = 100;
    constant Real thrust_2 = 36000;
    constant Real v_2_max = 10;
    constant Real v_2_min = 5;

    constant Real h_3 = 20;
    constant Real thrust_3 = 36000;
    constant Real v_3_max = 5;
    constant Real v_3_min = 1;

    function DecideThrust
        input Real h;
        input Real pre_h;
        input Real pre_thrust;
        output Real thrust;
    protected
        Real v;
    algorithm
        v := (pre_h - h) / Tau;
        if h >= h_1 then
            if v >= v_1_max then
                thrust := thrust_1;
            elseif v <= v_1_min then
                thrust := 0.0;
            else
                thrust := pre_thrust;
            end if;
        elseif h >= h_2 then
            if v >= v_2_max then
                thrust := thrust_2;
            elseif v <= v_2_min then
                thrust := 0.0;
            else
                thrust := pre_thrust;
            end if;
        else
            if v >= v_3_max then
                thrust := thrust_3;
            elseif v <= v_3_min then
                thrust := 0.0;
            else
                thrust := pre_thrust;
            end if;
        end if;
    end DecideThrust;

initial equation
    h_d = ad(h, h_min, h_max, h_res);
equation
    when sample(0, Tau) then
        h_d = ad(h, h_min, h_max, h_res);
        pre_h_d = pre(h_d);
        v_d = (h_d - pre_h_d) / Tau;
        u = DecideThrust(h_d, pre_h_d, pre(u));
    end when;
end Controller;

