
class Monitor

parameter Real T = 1;

parameter Boolean y0 = false;

Real x;
Boolean y;

initial equation
y = y0;

equation


when sample(0, T) then

if (pre(y) or ((abs(x)) > 0.1 and (time > 1))) 
then y = true; 
else y = false;
end if;

end when;



end Environment;