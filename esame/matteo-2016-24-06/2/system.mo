class System
  parameter Integer u0 = 1;
  Controller controller;
  Plant plant;
initial equation
  controller.w0 = u0;
  plant.u = u0;
equation
  controller.y = plant.y;
  controller.u = plant.u;


end System;
