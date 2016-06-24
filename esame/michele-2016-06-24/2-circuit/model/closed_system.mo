model ClosedSystem
    Plant p;
    Controller c;
equation
    c.r = ad(p.y, -20, 20, 0.001);
    p.u = c.w;
end ClosedSystem;

