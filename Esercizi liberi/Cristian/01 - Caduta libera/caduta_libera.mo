model CadutaLibera "Un modello di caduta libera"
	constant Real g = 9.81;
	parameter Real h0 = 1000; //altezza iniziale
	parameter Real v0 = 0;    //velocità iniziale
	Real v; //velocità
	Real p; //spazio percorso
	equation
		v = g*time + v0;
		p = (-0.5 * g * (time^2)) + v0*time + h0;

end CadutaLibera;
	
