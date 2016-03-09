function CalculateTimeAndForce

	input Real height;                       //altezza di partenza
	input Real v0;                           //velocità iniziale
	input Real g;                            //accelerazione di gravità
	input Real mass;                         //massa del corpo
	input Real max_thrust;                   //massima forza applicabile
	protected Real a, b, c, tc, vf, delta_t; //usate all'interno dell'algoritmo
	output Real f;                             //istante t al quale una forza f

	initial equation

	algorithm
		a = (1/2)*g;
		delta := v0^2 +4*a*height;
		c := sqrt(delta);
		tc := (-v0 + c)/(2*a); //tempo di arrivo in caduta libera
		vf := tc * g + v0; //velocità al punto di impatto
		f := m*((vf-v0)/tc);
		return;
end CalcultateTimeAndForce;
		
		 
	
