model Gate
	parameter Real g0 = 0;
	parameter Real barVelocity = 10;

	output Real g;
	output Real gv;
	Boolean open;
 	Boolean close;
initial equation
	g = g0;
equation
	gv = der(g);
	if (close == true ) then
		der(g) = -barVelocity;
	elseif (open == true) then
		der(g) = barVelocity;
	else
		der(g) = 0;
	end if;

	when g >= 90 then
		reinit(g, 90);
	elsewhen g <= 0 then
		reinit(g, 0);
	end when;

end Gate;
