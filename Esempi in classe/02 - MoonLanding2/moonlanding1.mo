class MoonLanding

// parameter Real T = 1;

parameter Real force1 = 36350;
parameter Real force2 = 1308;

protected 
parameter Real thrustEndTime = 210;
parameter Real thrustDecreaseTime = 43.2;


public
Rocket apollo(name "apollo13");
CelestialBody moon(name="moon",mass=7.382e22,radius=1.738e6);
ECU ctr;




equation

// plant
apollo.gravity = moon.g*moon.mass/(apollo.altitude+moon.radius)^2;

// controller 
ctr.initial_altitude = apollo.initial_altitude;
ctr.initial_velocity = apollo.initial_velocity;
ctr.acceleration = apollo.acceleration;
ctr.measured_altitude = apollo.altitude;
ctr.f1 = force1;
ctr.f2 = force2;
apollo.thrust = ctr.thrust;


// assert(not(abs(apollo.altitude) < 1000) or (abs(apollo.velocity) <= 0.001), "Apollo Crash", AssertionLevel.error);

end MoonLanding;
