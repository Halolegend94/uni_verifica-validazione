function FullAdderFunction "Full adder function"

	input Boolean x1;
	input Boolean x2;
	input Boolean c;
	output Boolean y;
	output Boolean c2;

	algorithm
		y := XOR(XOR(x1, x2), c);
		c2 := OR(AND(x1, x2), AND(OR(x1, x2), c));
end FullAdderFunction;
