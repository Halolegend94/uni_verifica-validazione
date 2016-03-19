model FullAdder "A model of a full adder"
	parameter Boolean x1;
	parameter Boolean x2;
	parameter Boolean c;
	Boolean y;
	Boolean co;

	equation
		(y, co) = FullAdderFunction(x1, x2, c);
	 
end FullAdder;
