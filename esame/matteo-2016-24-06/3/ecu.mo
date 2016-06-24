class ECU
  parameter Real T = 0.1;
  constant Real kp = 1000, kd = 0, ki = 0;
  constant Real max_thrust = 2000*9.81*3;

  input Real h;
  Real h_last;
  output Real thrust(start = 0);

  Real error(start=0);
  Real error_i(start=0);

  /*output Real debug1, debug2;*/

function autopilot
  input Real ep, ed, ei;
  output Real t;
algorithm
  t := ep * kp + ed * kd + ei * ki;
  if (t < 0) then
    t := 0;
  elseif (t > max_thrust) then
    t := max_thrust;
  end if;
end autopilot;
function calculate_error
  input Real h;
  input Real v;
  output Real e;
algorithm
  if (h > 20000) then
    e := -500;
  elseif (h > 5000) then
    e := -100;
  elseif (h > 10) then
    e := -5;
  else
    e := 0;
  end if;
  e := e - v;
end calculate_error;

initial equation
  h_last = h;
equation
  when sample(0, T) then
    error = calculate_error(h, (h-pre(h_last))/T);
    error_i = pre(error_i)+error;
    thrust = autopilot(error, (error-pre(error))/T, error_i);
    /*debug1 = h-pre(h_last);
    debug2 = error;*/
    h_last = h;
  end when;

end ECU;
