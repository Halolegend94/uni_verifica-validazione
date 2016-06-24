class Controller
  constant Real T = 1e-6;
  input Integer w0 = 0;

  parameter Real alpha = 0.35;

  Real y;
  Real r;
  Integer u;
  Integer w;

  Boolean intoAlpha;
initial equation
  intoAlpha = true;
  w = w0;
  /*pre(w) = w0;*/
equation
  when time > 0.01 and (y < 5-alpha or y > 5+alpha) then
    intoAlpha = false;
  end when;
  when sample(0,T) then
    r = AD(0.001, -20, 20, y);
    if (r >= 5.01) then
      w = 0;
    elseif (r <= 4.99) then
      w = 1;
    else
      w = pre(w);
    end if;
    u = w;
  end when;
end Controller;
