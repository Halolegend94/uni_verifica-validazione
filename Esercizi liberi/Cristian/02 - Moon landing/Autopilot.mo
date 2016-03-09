function Autopilot
	input Real altitude;
	input Real velocity;
	input Real gravity;
	input Real mass;

	output Real thrust;
algorithm
if altitude > 10000 and velocity < -200 then
	thrust:= 3400;
else
	thrust := mass * gravity;
end if;
end Autopilot;
