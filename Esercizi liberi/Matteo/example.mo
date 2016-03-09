class example
    Real x(start=2);
    Real y(start=3);
equation
    der(x) = 2*x*y-3*x;
    der(y) = 5*y-7*x*y;
end example;
