model Gate
	parameter Real g0 = 0;
	output Real g;
	output Real gv;
	Boolean open;
 	Boolean close;
initial equation
	g = g0;
equation
	der(g) = gv;
	if (close == true) then
		gv = -9;
	elseif (open == true) then
		gv = 9;
	else
		gv = 0;
	end if;

/*
	when (g < 0) then
		g = 0;
	end when;
*/
	// g [0,90]
	// sample T = 1 -> g < 0
end Gate;
