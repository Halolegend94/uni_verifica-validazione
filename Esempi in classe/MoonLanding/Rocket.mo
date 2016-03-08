model Rocket "generic rocket class"
  extends Body;
  parameter Real massLossRate=0.000277;
  Real altitude(start= 59404);
  Real velocity(start= -2003);
  Real acceleration;
  Real thrust(max=36350, min=0);
  Real gravity;
equation
  thrust - mass*gravity = mass*acceleration;
  der(mass)     = -massLossRate*abs(thrust);
  der(altitude) = velocity;
  der(velocity) = acceleration;
end Rocket;

