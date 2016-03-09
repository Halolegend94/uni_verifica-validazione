model MoonLanding
	parameter Real startApolloMass    = 1038.358;
	parameter Real startApolloAltitude = 59404;
	parameter Real startApolloVelocity = -2003;
	Rocket apollo(name="Apollo13", mass(start=startApolloMass),
			altitude(start=startApolloAltitude),
				velocity(start = startApolloVelocity));
	CelestialBody moon(mass = 7.382e22, name = "moon", radius = 1.738e6, gravity=6.672e-11);
	Boolean success(start=false);
	equation
		apollo.gravity = moon.gravity * moon.mass / (apollo.altitude + moon.radius)^2;
		success = apollo.altitude <= 0 and apollo.velocity >= (-10);
		
		when sample(0, 0.5) then
			apollo.thrust = CalculateThrust(apollo.altitude, apollo.velocity, apollo.gravity, startApolloMass);
		end when;
		when apollo.altitude <= 0 then
			terminate(if apollo.velocity>=(-10) then "landend" else "crashed");
		end when;
		annotation(experiment(StartTime=0, StopTime=500, Tolerance=1e-06, Interval=0.1));
end MoonLanding;
