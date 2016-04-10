class ClosedSystem
    Monitor     monitor;
    System      sys;
    Environment env;
    output Boolean admissible;
    output Boolean error;
equation
    monitor.x = sys.x;         // connect monitor to SUV
    sys.noise = env.d.noise;   // connect environment to SUV
    /* connect output bool variables */
    error = monitor.y;
    admissible = env.x.adm;
end ClosedSystem;

