function AD

  input Real Delta;
  input Real LoVal;
  input Real HiVal;
  input Real x;

  output Real y;

algorithm

  if (x <= LoVal) then
    y := LoVal;
  elseif (x >= HiVal) then
    y := HiVal;
  else
    y := Delta*floor((x/Delta) + 0.5);
  end if;

end AD;
