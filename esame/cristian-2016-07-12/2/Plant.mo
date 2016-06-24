class Plant

   input Real u;
   output Real y;
   Real i_L, v_O, v_D, i_D, v_C, i_C, i_s, v_s, i_R, v_L;
   Integer s;

   parameter Real V_i = 15.0;
   parameter Real L = 200e-6;
   parameter Real C = 50e-6;
   parameter Real R = 5.0;
   parameter Real R_off = 1e7;
   parameter Real R_on = 1e-3;
   parameter Real r_L = 0.1;
   parameter Real r_C = 0.1;
   parameter Real T = 1e-6;


equation
   i_D = i_L - i_s;
   v_D = v_s - V_i;
   -v_D = v_L + r_L * i_L + v_O;
   v_L = L * der(i_L);
   i_C = C * der(v_C);
   v_C + r_C * i_C = v_O;
   i_R * R = v_O;
   i_L = i_C + i_R;
   y = v_O;

   if s == 1 then
      v_s = R_on * i_s;
   else
      v_s = R_off * i_s;
   end if;

   if i_D >= 0 then
      v_D = 0;
   else
      v_D = R_off * i_D;
   end if;

   if mod(time, T)  < T * u then
      s = 1;
   else
      s = 0;
   end if;

end Plant;
