class Plant
  parameter Real iL0, vO0;
  Real iL, vO, vD, iD, vC, iC, iU, vU, iR, vL;
  input Integer u;
  output Real y;
  constant Real Vi = 15.0,
                L = 200e-6,
                C = 50e-6,
                R = 5.0,
                Roff =1e14,
                Ron = 1e-14,
                rL = 0.1,
                rC = 0.1;
initial equation
  iL = iL0;
  vO = vO0;
equation
  iD = iL - iU;
  vD = vU - Vi;
  -vD = vL +rL*iL+vO;
  vL = L*der(iL);
  iC = C*der(vC);
  vC+rC*iC = vO;
  iR * R = vO;
  iL = iC + iR;
  y = vO;
  if (u == 1) then
    vU = iU * Ron;
  else
    vU = iU * Roff;
  end if;

  if (iD >= 0.0) then
    vD = 0.0;
  else
    vD = Roff * iD;
  end if;
end Plant;
