/* disturbance */
record Disturbance
    Boolean transition1;
    Boolean transition2;
    Real drift1;
    Real drift2;
end Disturbance;

/* state */
record State
    Boolean adm;
    Integer count;
end State;

class Environment

    /* constants */
    constant Real Tau;
    constant Integer length;

    /* init parameters */
    parameter Boolean adm_start = true;
    parameter Integer count_start = 0;
    parameter Boolean transition1_start = false;
    parameter Boolean transition2_start = false;
    parameter Real drift1_start = 0.0;
    parameter Real drift2_start = 0.0;

    Disturbance d;
    State s;

initial equation
    s.adm = adm_start;
    s.count = count_start;
    d.transition1 = transition1_start;
    d.transition2 = transition2_start;
    d.drift1 = drift1_start;
    d.drift2 = drift2_start;
equation
    when sample(Tau/2, Tau) then
        s.adm = pre(s.adm) and s.count <= length;
        s.count = pre(s.count) + 1;
        d.transition1 = pre(d.transition1);
        d.transition2 = pre(d.transition2);
        d.drift1 = pre(d.drift1);
        d.drift2 = pre(d.drift2);
    end when;
end Environment;

