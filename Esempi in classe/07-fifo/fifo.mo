
class FIFO

// 1KL = 1 m3


parameter Real x0 = 3.5;  // MB in FIFO

input Real p_out;  // output MB/sec
Real p_in;  //  input MB/sec
input Integer u;

// water volume x = S*z, where: S lake average surface, z water level

Real x;   // FIFO  MB


initial equation
x = x0;

//p_in = 1.5;

equation

p_in = 1.5 + 0.5*sin(2*3.14*10*time);

der(x) = u*p_in - p_out;


end FIFO;




