class Rocket "rocket class"

parameter String name;
parameter Real initialmass = 1038.358;
parameter Real massLossRate=0.000277;
parameter Real initial_altitude = 59404;
parameter Real initial_velocity = -2003;

Real mass;
Real altitude;
Real velocity;

Real acceleration;
Real thrust;  // Thrust force on rocket
Real gravity;  // Gravity forcefield

initial equation

mass = initialmass;
altitude = initial_altitude;
velocity = initial_velocity;

equation

(thrust-mass*gravity)/mass = acceleration;

der(mass)  = -massLossRate * abs(thrust);

der(altitude) = velocity;
der(velocity) = acceleration;

end  Rocket;