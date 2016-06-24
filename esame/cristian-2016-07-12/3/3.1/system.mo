
class System


Monitor m;
Boolean firstSecond;

initial equation
   m.z = 6;
equation
   m.w = 3;
   firstSecond = time > 1;
   when edge(firstSecond) then
      reinit(m.z, 9);
   end when;
end System;
