class fifo


   parameter Real x0 = 5;  // MB in FIFO

   input Real v_read;             // output MB/sec
   input Real v_write;            //  input MB/sec

   input Integer u;              // controllo
   Real x;                       //quantità di byte contenuti nella fifo


initial equation
   x = x0;

equation

   der(x) = v_write*u - v_read ;

end fifo;
