model Validazione
    Rocket r;
    Monitor m;
equation
    r.u = 2.0 * r.m_start * r.g;
    m.h = r.h;
    m.v = r.v;
end Validazione;

