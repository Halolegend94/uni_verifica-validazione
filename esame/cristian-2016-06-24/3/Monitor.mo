class Monitor

   input Real h;
   input Real v;
   Boolean temp;
   output Boolean b;
   input Real m;
   output Boolean landed;
initial equation
   pre(b) = false;
   pre(landed) = false;
equation
   landed = if pre(landed) == true then true else h <= 0;
    temp = (h <= 0 and abs(v) > 10) or (m < 0);
    if(edge(temp)) then
      b = true;
   else
      b = pre(b);

   end if;

end Monitor;
