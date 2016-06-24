class Rocket "rocket class"


  parameter Real initialmass = 2000;
  parameter Real initial_altitude = 50000;
  parameter Real initial_velocity = -1000;

  constant Real massLossRate = 0.000277;
  constant Real gravity = 9.81;

  Real mass;
  Real altitude;
  Real velocity;
  Real acceleration;
  input Real thrust;

initial equation

  mass = initialmass;
  altitude = initial_altitude;
  velocity = initial_velocity;

equation

  thrust-mass*gravity = acceleration * mass;

  der(mass)  = -massLossRate * abs(thrust);

  der(altitude) = velocity;
  der(velocity) = acceleration;

end  Rocket;
