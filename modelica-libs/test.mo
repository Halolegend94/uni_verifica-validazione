class Test
    Real x;
    Real y;
equation
    der(x) = sin(time);
    when sample(0, 0.5) then
        y = ad(x, 0.0, 1.5, 0.1);
    end when;
end Test;

