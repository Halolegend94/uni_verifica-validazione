class System
  Rocket rocket;
  Monitor monitor;
  parameter Real t0;
equation
  monitor.v = rocket.velocity;
  monitor.h = rocket.altitude;
  rocket.thrust = t0;
end System;
