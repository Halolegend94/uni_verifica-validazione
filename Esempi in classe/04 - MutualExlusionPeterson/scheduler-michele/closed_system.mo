
model SchedulerSystem
    constant Real time_step = 1.0;
    Process p1(id = 1, T = time_step);
    Process p2(id = 2, T = time_step);
    TurnAssigner t(id = 3, T = time_step);
    Environment env(T = time_step);
    Monitor m;
    output Boolean admissible;
    output Boolean error;
equation
    // process 1
    p1.turn = t.turn;
    p1.other_state = p2.state;
    p1.scheduler = env.s.turn;
    // process 2
    p2.turn = t.turn;
    p2.other_state = p1.state;
    p2.scheduler = env.s.turn;
    // turn assigner
    t.state1 = p1.state;
    t.state2 = p2.state;
    t.scheduler  = env.s.turn;
    // monitor
    m.state1 = p1.state;
    m.state2 = p2.state;
    // output variables
    admissible = env.s.adm;
    error = m.error;
end SchedulerSystem;

