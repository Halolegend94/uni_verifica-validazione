function OR "A function that performs the or"
	input Boolean x1;
	input Boolean x2;
	output Boolean y;

	algorithm
		y := x1 or x2;
end OR;

function AND "A function that performa the and"
	input Boolean x1;
	input Boolean x2;
	output Boolean y;

	algorithm
		y := x1 and x2;
end AND;

function XOR "A function that performs the xor"
	input Boolean x1;
	input Boolean x2;
	output Boolean y;

	algorithm
		y:= OR(AND(not(x1), x2), AND(x1, not(x2)));
end XOR;
