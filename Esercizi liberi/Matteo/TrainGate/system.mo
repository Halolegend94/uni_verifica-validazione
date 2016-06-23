model System
  input Real v;

	Train train;
	Gate gate;
	ECU ecu;

equation
  train.v = v;
	ecu.x = train.x;
  ecu.g = gate.g;
	gate.open = ecu.open;
	gate.close = ecu.close;

end System;
