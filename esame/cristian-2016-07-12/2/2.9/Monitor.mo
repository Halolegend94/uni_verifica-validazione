class Monitor

   input Real y;
   constant Real alpha = 0.2;
   output Boolean error;
   Boolean temp;

initial equation
   pre(error) = false;

equation

   temp = (5 - alpha <= y and y <= 5 + alpha and time > 0.1);

   if edge(temp) then
      error = true;
   else
      error = pre(error);
   end if;


end Monitor;
