class System
  parameter Integer u0 = 0;
  Plant plant;
  Boolean low_check, high_check;
initial equation
  plant.u = u0;
  low_check = false;
  high_check = false;
equation
  plant.u = u0;
  when (plant.y > 0.00001) then
    low_check = true;
  end when;
  when (plant.y < plant.Vi-0.4 and time > 0.01) then
    high_check = true;
  end when;
end System;
