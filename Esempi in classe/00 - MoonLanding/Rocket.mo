model Rocket "generic rocket class"
  extends Body;
  parameter Real massLossRate=0.000277;
  Real altitude;
  Real velocity;
  Real acceleration;
  Real thrust(max=36350, min=0);
  Real gravity;
equation
  thrust - mass*gravity = mass*acceleration;
  der(mass)     = -massLossRate*abs(thrust);
  der(altitude) = velocity;
  der(velocity) = acceleration;
end Rocket;

