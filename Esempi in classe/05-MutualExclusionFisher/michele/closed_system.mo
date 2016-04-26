
model FisherMutualExclusion
    constant Real time_step = 0.05;
    constant Real length_sec = 5;
    constant Integer length_steps = integer(length_sec / time_step);

    constant Real test_time = 0.2;
    constant Real set_time = 0.1;

    Process p1(id = 1, Tau = time_step, min_drift = 0.2, max_drift = 0.0, test_time = test_time, set_time = set_time);
    Process p2(id = 2, Tau = time_step, min_drift = 0.0, max_drift = 0.1, test_time = test_time, set_time = set_time);

    CSVariable cs(Tau = time_step);

    Environment env(Tau = time_step, length = length_steps);
    Monitor m;

    output Boolean admissible;
    output Boolean error;

equation
    // process 1
    p1.turn = cs.turn;
    p1.new_turn = cs.turn1;
    p1.fire_transition = env.d.transition1;
    p1.process_drift = env.d.drift1;
    // process 2
    p2.turn = cs.turn;
    p2.new_turn = cs.turn2;
    p2.fire_transition = env.d.transition2;
    p2.process_drift = env.d.drift2;
    // monitor
    m.state1 = p1.state;
    m.state2 = p2.state;
    // output variables
    admissible = env.s.adm;
    error = m.error;
end FisherMutualExclusion;

