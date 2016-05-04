
class Turn

parameter Integer x0 = 0;

Integer turn;
Integer x1;
Integer x2;
Integer k;

function next
input Integer turn;
input Integer x1;
input Integer x2;
turn Integer k;
output State y;

algorithm

if (k == 3)
then
    if (turn == 1) and (x1 == 0) and (x2 == 1) then y := 2; end if;

    if (turn == 2) and (x2 == 0) and (x1 == 1) then y := 1; end if;

else
     y := x;
end if;

end next;


initial equation

x = x0;

equation

when sample(0, T) then


turn = next(pre(turn), , x1, x2, k);


end when;


end System;
