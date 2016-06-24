class Missile
   parameter Real m0 = 2000;
   parameter Real h0 = 51415.0;
   parameter Real v0 = -1100;

   constant Real loss = 0.000277;
   constant Real g = 9.8;

   Real h, v, a, m;
   input Real u;

initial equation
    h = h0;
    v = v0;
    m = m0;

equation
    u - m*g = a*m;
    der(m) = -loss * abs(u);
    der(h) = if h > 0 then v else 0;
    der(v) = if h > 0 then a else 0;

end Missile;
