function Autopilot1
  input Real x;
  input Real time1;
  input Real time2;
  input Real force1;
  input Real force2;
  output Real y;
algorithm
  if (x < time1) then
	y := force1;
  elseif (x < time2) then
	y := force2;
  else
	y := 0;
  end if;
end Autopilot1;

