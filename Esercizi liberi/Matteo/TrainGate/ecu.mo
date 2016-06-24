model ECU

	parameter Real T = 0.1;
 	input Real x; //posizione treno
 	input Real g; //inclinazione sbarra del passaggio
	Integer m; //modo

	Boolean open, close;

	parameter Real far = -1000;
	parameter Real past = 100;

	parameter Real far_vmax = 50;
	parameter Real far_min = 40;
	parameter Real near_vmax = 50;
	parameter Real near_vmin = 30;
	parameter Real past_vmax = 50;
	parameter Real past_vmin = 30;

equation
	when sample(0, T) then
		if(x <= far) then
			m = 0;
    	elseif (x > 100) then
      	m = 2;
    	else
      	m = 1;
    	end if;

		if (m == 1 and pre(m) == 0 and g < 90) then
			open = true;
			close = false; //mutualmente eslusivi
		elseif (m == 2 and pre(m) == 1 and g > 0) then
			close = true;
			open = false;
		elseif(g >= 90 and pre(open) == true) then
			open = false;
			close = pre(close);
		elseif(g < 0 and pre(close) == true) then
			close = false;
			open = pre(open);
		else
			open = pre(open);
			close = pre(close);
		end if;

	end when;

end ECU;
