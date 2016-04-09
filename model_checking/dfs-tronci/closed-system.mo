
class ClosedSystem

// Environment env;

Monitor monitor;
System sys;
Environment env;

equation

monitor.x = sys.x;         // connect monitor to system
sys.noise = env.d.noise;   // connect environment to system under verification (SUV)

// sys.noise = sin(2*3.14*time);    // just for testing 



end ClosedSystem;