class Rocket "rocket class"
    parameter String name;
    Real mass(start=1038.358);
    Real altitude(start= 59404);
    Real velocity(start= -2003);
    Real acceleration;
    Real thrust; // Thrust force on rocket
    Real gravity; // Gravity forcefield
    parameter Real massLossRate=0.000277;
equation
    (thrust-mass*gravity)/mass = acceleration;
    der(mass) = -massLossRate * abs(thrust);
    der(altitude) = velocity;
    der(velocity) = acceleration;
end Rocket;


class CelestialBody
    constant Real g = 6.672e-11;
    parameter Real radius;
    parameter String name;
    parameter Real mass;
end CelestialBody;


class MoonLanding
    parameter Real force1 = 36350;
    parameter Real force2 = 1308;
protected
    parameter Real thrustEndTime = 210;
    parameter Real thrustDecreaseTime = 43.2;
public
    Rocket apollo(name="apollo13");
    CelestialBody moon(name="moon",mass=7.382e22,radius=1.738e6);
    
function autopilot3
    input Real h, v, f1, f2;
    output Real y;
algorithm
    if (h >= 50000) then
	y := 0;
    else
	if (v <= -100) then y := f1;
	elseif (y <= -10) then y := f2;
	else y := 0;
	end if;
    end if;
end autopilot3;

equation
    when sample(0,1) then
	apollo.thrust = autopilot3(apollo.altitude, apollo.velocity, force1, force2);
    end when;
    
    /*
    apollo.thrust = if (time < thrustDecreaseTime) then force1
		    else if (time < thrustEndTime) then force2
		    else 0;
    */

    apollo.gravity=moon.g*moon.mass/(apollo.altitude+moon.radius)^2;
    when apollo.altitude < 0 then
	terminate("Touch!");
    end when;
end MoonLanding;
