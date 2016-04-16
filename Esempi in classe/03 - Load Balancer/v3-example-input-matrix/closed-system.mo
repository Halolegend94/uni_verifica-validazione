
class ClosedSystem

// Environment env;

Monitor monitor;
System sys;
Environment env;

input Real failures;
input Real noise;

equation

monitor.x = sys.x;         // connect monitor to system
// sys.noise = env.d.noise;   // connect environment to system under verification (SUV)

sys.failures = failures; 
sys.noise = noise; 

// sys.noise = sin(2*3.14*time);    // just for testing 



end ClosedSystem;