class FA "Full adder"

parameter Boolean x;
parameter Boolean y;
parameter Boolean c;
Boolean z;
Boolean r;

//Boolean v;

//quando si decide di modellare un circuito elettrico o logico con equazioni isogna avere tanti oggetti quanto sono i gate(in questo caso) utilizzati, mantenendo così l'OO

//XOR xor1;
//XOR xor2;
//OR or1;
//AND and1;

equation
//in questo modo abbiamo connesso le entrate dei vari gate del circuito con i relativi pin
//xor1.in1 = x;
//xor1.in2 = y;
//xor1.out = v;

//xor2.in1 = v;
//xor2.in2 = c;
//xor2.out = v;
(z,r) = functionFA(x, y, c);

end FA;
