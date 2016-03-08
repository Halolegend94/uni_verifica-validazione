function Autopilot2
  input Real altitude;
  input Real velocity;
  output Real thrust;
algorithm
  if altitude > 10000 then
	if velocity < -200 then
	  thrust := 36350;
	else
	  thrust := 0;
	end if;
  elseif altitude > 1000 then
	if velocity < -50 then
	  thrust := 6000;
	else
	  thrust := 0;
	end if;
  else
	if velocity < -10 then
	  thrust := 3000;
	else
	  thrust := 0;
	end if;
  end if;
end Autopilot2;

