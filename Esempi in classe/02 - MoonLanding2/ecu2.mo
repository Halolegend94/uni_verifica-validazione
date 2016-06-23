class ECU "Electrocni Control Unit"

parameter Real T = 0.3;
parameter Integer altitude_sampling = 25;

Real initial_altitude;
Real initial_velocity;

Real measured_altitude;

Integer counter;

Real altitude;
Real velocity;
Real acceleration;
Real f1, f2;
Real thrust;
Real history;

Real astep;
Real vstep;



function autopilot1
  input Real x;
  input Real decreasetime;
  input Real endtime;
  input Real f1;
  input Real f2;
  output Real y;
algorithm
if (x < decreasetime)
then y := f1;
else if (x < endtime)
     then y := f2;
     else y := 0.0;
     end if;
end if;
end autopilot1;

function autopilot2
  input Real h;
  input Real v;
  input Real f1;
  input Real f2;
   output Real y;
algorithm
if (v <= -10)
then y := f1;
else if (v <= -1)
     then y := f2;
     else y := 0.0;
     end if;
end if;
end autopilot2;

function autopilot3
  input Real h;
  input Real v;
  input Real f1;
  input Real f2;
   output Real y;
algorithm

if (h >= 55000)
then y := 0;
else
if (v <= -10)
then y := f1;
else if (v <= -1)
     then y := f2;
     else y := 0.0;
     end if;
end if;
end if;

end autopilot3;

function autopilot4
  input Real h;
  input Real v;
  input Real f1;
  input Real f2;
   output Real y;
algorithm

if ( (h >= 0) and (v > 0) )
then y := 0;
else if (h <= 0)
     then y := f2;
     else y := f1;
     end if;
end if;

end autopilot4;


function autopilot5
  input Real h;
  input Real v;
  input Real f1;
  input Real f2;
   output Real y;
algorithm

if (h >= 10000)
then if (v < -100)
     then y := f1;
     else y := 0;
     end if;
end if;


if ((h < 10000) and (h >= 0))
then if (v < -10)
     then y := f2;
     else y := 0;
     end if;
end if;


end autopilot5;


function autopilot7
  input Real h;
  input Real v;
  input Real f1;
  input Real f2;
  input Real oldval;
  output Real y;
  protected Real error;
algorithm


if (h >= 60000)
then y := 0;
end if;

if ((h <= 60000) and (h >= 10000))
then // target velocity: -500
     if (v <= -501)
     then y := f1;
     else
	  if (v >= -499)
     	  then y:= 0;
     	  else y:= oldval;
          end if;
     end if;
end if;

if ((h <= 10000) and (h >= 5000))
then // target velocity: -300
     if (v <= -301)
     then y := f1;
     else
	  if (v >= -299)
     	  then y:= 0;
     	  else y:= oldval;
          end if;
     end if;
end if;

if ((h <= 5000) and (h >= 1000))
then // target velocity: -200
     if (v <= -201)
     then y := f1;
     else
	  if (v >= -199)
     	  then y:= 0;
     	  else y:= oldval;
          end if;
     end if;
end if;

if ((h <= 1000) and (h >= 100))
then // target velocity: -100
     if (v <= -101)
     then y := f1;
     else
	  if (v >= -99)
     	  then y:= 0;
     	  else y:= oldval;
          end if;
     end if;
end if;

if ((h <= 100) and (h >= 3))
then // target velocity: -10
     if (v <= -11)
     then y := f2;
     else
	  if (v >= -9)
     	  then y:= 0;
     	  else y:= oldval;
          end if;
     end if;
end if;

if ((h <= 3) and (h >= 1))
then // target velocity: -0.5
     if (v <= -0.7)
     then y := f2;
     else
	  if (v >= -0.3)
     	  then y:= 0;
     	  else y:= oldval;
          end if;
     end if;
end if;

if ((h <=1) and (h >= -1))
then // target velocity: -0.5
y:= 0;
end if;


if ((h <= -1) and (h >= -6))
then // target velocity: 0.5
     if (v <= 0.4)
     then y := f2;
     else
	  if (v >= 0.8)
     	  then y:= 0;
     	  else y:= oldval;
          end if;
     end if;
end if;

if (h < -6)
then y := f1;
end if;

end autopilot7;


function ad
input Real x;
output Real y;
protected Real Delta = 0.8;
protected Real HiVal = 100;
protected Real LoVal = -100;

algorithm

if (x <= LoVal)
then  y := LoVal;
else  if (x >= HiVal)
      then y := HiVal;
      else y := Delta*floor((x/Delta) + 0.5);
      end if;
end if;

end ad;


initial equation

velocity = initial_velocity;
altitude = initial_altitude;
counter = 0;

equation



when sample(0, T) then

counter = if (pre(counter) == altitude_sampling) then 0 else (pre(counter) + 1);

vstep = T*velocity;
astep = ad(acceleration);

// estimate altitude from acceleration and adjust using low frequency actual measurement
altitude =
if (pre(counter) == 0)
then measured_altitude
else (pre(altitude) + T*velocity);

// estimate velocity from acceleration and adjust using low frequency actual measurement
velocity =
if (pre(counter) == 0)
then
  (measured_altitude - delay(measured_altitude, altitude_sampling*T))/(altitude_sampling*T)
else
  (pre(velocity)  + T*astep);



history = pre(thrust);
thrust = autopilot7(altitude, velocity, f1, f2, history);

end when;


end ECU;
