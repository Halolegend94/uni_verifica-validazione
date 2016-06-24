class Monitor
  input Real v, h;
  Boolean crash(start = false);
equation
  when (h <= 0) then
    if (abs(v) > 10) then
      crash = true;
    else
      crash = pre(crash);
    end if;
  end when;
end Monitor;
