model ClosedSystem
    Controller c;
    Monitor m;
    Rocket r;
equation
    c.h = r.h;
    r.u = c.u;
    m.h = r.h;
    m.v = r.v;
end ClosedSystem;

