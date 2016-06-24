model Rocket
    constant Real mu = 0.000277; // mass loss rate
    constant Real g = 9.8; // gravity

    parameter Real h_start = 50000;
    parameter Real v_start = -1000;
    parameter Real m_start = 2000;

    Real m; // mass
    Real h; // height
    Real v; // speed
    Real a; // acceleration

    input Real u; // thrust
initial equation
    v = v_start;
    h = h_start;
    m = m_start;
equation
    der(m) = - mu * abs(u);
    u - m * g = a * m;
    der(v) = if h > 0.0 then a else 0.0;
    der(h) = if h > 0.0 then v else 0.0;
end Rocket;

