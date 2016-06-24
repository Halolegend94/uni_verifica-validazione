class Plant
    parameter Real i_L_start = 0;
    parameter Real v_O_start = 0;

    parameter Real V_i = 15.0;
    parameter Real L = 200.0e-06;
    parameter Real C = 50.0e-06;
    parameter Real R = 5.0;
    parameter Real R_off = 1.0e07;
    parameter Real R_on = 0.0;
    parameter Real r_L = 0.1;
    parameter Real r_C = 0.1;

    Real i_L;
    Real v_O;
    Real v_D;
    Real i_D;
    Real v_C;
    Real i_C;
    Real i_u;
    Real v_u;
    Real i_R;
    Real v_L;

    output Real y;
    input Integer u;
initial equation
    i_L = i_L_start;
    v_O = v_O_start;
equation
    i_D = i_L - i_u;              // 1
    v_D = v_u - V_i;              // 2
    -v_D = v_L + r_L * i_L + v_O; // 3
    v_L = L * der(i_L);           // 4
    i_C = C * der(v_C);           // 5
    v_C + r_C * i_C = v_O;        // 6
    i_R * R = v_O;                // 7
    i_L = i_C + i_R;              // 8
    y = v_O;                      // 9
    if u == 1 then               // 10
        v_u = R_on * i_u;
    else
        v_u = R_off * i_u;
    end if;
    if i_D >= 0.0 then            // 11
        v_D = 0.0;
    else
        v_D = R_off * i_D;
    end if;
end Plant;

