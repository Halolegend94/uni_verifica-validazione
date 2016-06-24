model TestSpecifica
    Rocket r;
    Monitor m;
equation
    r.u = 0.0;
    m.h = r.h;
    m.v = r.v;
end TestSpecifica;

