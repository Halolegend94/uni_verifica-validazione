model CadutaLibera "Un modello di caduta libera"
	/* per semplicità assumiamo sia un semplice moto accelerato costante*/
	constant Real g = 9.81;
	parameter Real v0 = 0; //velocità iniziale
	Real v; //velocità
	Real p; //spazio percorso
	equation
		v = g*time + v0;
		p = 0.5 * g * (time^2);

end CadutaLibera;
	
