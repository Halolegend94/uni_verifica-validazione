model MoonLanding
  parameter Real force1              = 36350;
  parameter Real force2              =  1308;
  parameter Real thrustEndTime       =   210;
  parameter Real thrustDecreaseTime  =    43.2;
  parameter Real startApolloMass     =  1038.358;
  parameter Real startApolloAltitude = 59404;
  parameter Real startApolloVelocity = -2003;
  Rocket apollo(name = "apollo13",
				mass(start = startApolloMass),
				altitude(start = startApolloAltitude),
				velocity(start = startApolloVelocity));
  CelestialBody moon(mass = 7.382e22, radius = 1.738e6, name = "moon");
  Boolean success(start = false);
equation
  apollo.gravity = moon.g * moon.mass / (apollo.altitude + moon.radius) ^ 2;
  success = apollo.altitude <= 0 and apollo.velocity >= (-10);
  /* Autopilot */
  when sample(0,0.5) then
    //apollo.thrust = Autopilot1(time, thrustDecreaseTime, thrustEndTime, force1, force2);
    apollo.thrust = Autopilot2(apollo.altitude, apollo.velocity);
  end when;
  /* Simulation end */
  when apollo.altitude < 0 then
    terminate(if apollo.velocity >= (-10) then "Landed." else "Crashed.");
  end when;
  when terminal() then
    assert(apollo.altitude <= 0, "Still flying.", level = AssertionLevel.warning);
  end when;
  annotation(experiment(StartTime = 0, StopTime = 500, Tolerance = 1e-06, Interval = 0.1));
end MoonLanding;
