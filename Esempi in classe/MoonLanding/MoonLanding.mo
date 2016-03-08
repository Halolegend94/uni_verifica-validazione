model MoonLanding
  parameter Real force1 = 36350;
  parameter Real force2 = 1308;
  parameter Real thrustEndTime = 210;
  parameter Real thrustDecreaseTime = 43.2;
  Rocket apollo(name = "apollo13", mass(start = 1038.358));
  CelestialBody moon(mass = 7.382e22, radius = 1.738e6, name = "moon");
  Boolean success(start = false);
equation
  when sample(0,1) then
    //apollo.thrust = Autopilot1(time, thrustDecreaseTime, thrustEndTime, force1, force2);
    apollo.thrust = Autopilot2(apollo.altitude, apollo.velocity);
  end when;
  apollo.gravity = moon.g * moon.mass / (apollo.altitude + moon.radius) ^ 2;
  when apollo.altitude < 0 then
    terminate(if apollo.velocity >= (-10) and apollo.altitude <= 0 then "Landed." else if apollo.altitude > 0 then "Still flying." else "Crashed.");
  end when;
  when terminal() then
    success = apollo.altitude <= 0 and apollo.velocity >= (-10);
  end when;
  annotation(experiment(StartTime = 0, StopTime = 500, Tolerance = 1e-06, Interval = 0.1));
end MoonLanding;
