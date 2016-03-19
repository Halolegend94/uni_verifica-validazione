###############################################################################
#
# loadParams
# Autore: Cristian Di Pietrantonio
#
# Descrizione: Legge da un file di testo i valori da passare al modello come paramentri
# i valori attesi per le variabili di interesse alla fine della simulazione.
# Ogni riga ha il seguente formato:
# param1=val1, param2=val2, ..paramN=valN | output1=exp1, output2=exp2, ...,outputM=expM
# Gli spazi tra i delimitatori non sono considerati
#
###############################################################################

def loadParams(filename):
	in_file = open(filename, "r")
	params = list()    #contiene una lista di liste di coppie, ossia [ [ [a, b],.. ]... ]
	expected = list()  #contiene una lista di liste di coppie

	while 1:
		line = in_file.readline()
		if(line == ""):
			break
		line_params = list()
		line_expected = list()

		#parse the line. each line has the form param1=val1, ..,paramN=valN | output1=expected1,..., oputputM=expectedM
		first_split = line.split("|")
		#get the starting params
		Pcouples = first_split[0].split(",")
		for coup in Pcouples:
			rr = coup.split("=")
			rr[0] = rr[0].strip() #eliminiamo gli spazi bianchi
            		rr[1] = rr[1].strip()
			line_params.append(rr)
		#save the line params list
		params.append(line_params)

		#now get the expected output var and associated values
		Ecouples = first_split[1].split(",")
		for ecoup in Ecouples:
			rr=ecoup.split("=")
			rr[0] = rr[0].strip()
			rr[1] = rr[1].strip()
			line_expected.append(rr)

		#save the line expected value list
		expected.append(line_expected)
	return [params, expected]
