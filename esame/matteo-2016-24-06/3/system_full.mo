class System
  Rocket rocket;
  Monitor monitor;
  ECU ecu;
equation
  monitor.v = rocket.velocity;
  monitor.h = rocket.altitude;
  ecu.h = rocket.altitude;
  rocket.thrust = ecu.thrust;
end System;
