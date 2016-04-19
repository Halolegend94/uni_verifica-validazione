
class Process

parameter Integer id = 1;
parameter Integer x0 = 0;

Integer x;
Integer u;
Integer k;
Integer turn;

function next
input Integer id;
input Integer x;
input Integer u;
input Integer turn;
input Integer k;
output State y;

algorithm

if (k == id)

then 
    if (x == 0) then y := 1 end if;

    if (x == 1) and (u == 0) then y := 2; end if;

    if (x == 1) and (u == 1) and (turn == id) then y := 2; end if;

    if (x == 2) then y := 0; end if;


else
     y := x;
end if;


end next;


initial equation

x = x0;

equation

when sample(0, T) then


x = next(id, pre(x), u, d, turn, k);


end when;


end Process;