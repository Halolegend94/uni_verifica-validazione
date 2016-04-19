/* disturbance */
record Disturbance
    Integer turn;
end Disturbance;

/* state */
record State
    Boolean adm;
    Integer turn;
    Integer count;
end State;

class Environment

    function Next
        input State x;
        input Disturbance d;
        output State y;
    algorithm
        y.count := x.count + 1;
        y.turn := d.turn;
        y.adm := d.turn >= 1 and d.turn <= 3 and y.count <= length and x.adm;
    end Next;

    /* constants */
    constant Real T;
    constant Integer length = 5;

    /* init parameters */
    parameter Boolean adm_start = true;
    parameter Integer turn_start = 1;
    parameter Integer count_start = 0;
    parameter Integer disturbance_start = 1;

    Disturbance d;
    State s;

    State pre_s;

initial equation
    s.adm = adm_start;
    s.turn = turn_start;
    s.count = count_start;
    d.turn = disturbance_start;
equation
    when sample(T/2, T) then
        pre_s.adm = pre(s.adm);
        pre_s.turn = pre(s.turn);
        pre_s.count = pre(s.count);
        s = Next(pre_s, d);
        d.turn = pre(d.turn);
    end when;
end Environment;

