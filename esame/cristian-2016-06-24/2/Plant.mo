class Plant

   Real i_L, v_O, v_D, i_D, v_C, i_C, i_u, v_u, i_R, v_L, y;
   input Integer u;
   parameter Real V_i = 15.0;
   parameter Real L = 200e-6;
   parameter Real C = 50e-6;
   parameter Real R = 5.0;
   parameter Real R_off = 1e7;
   parameter Real R_on = 1e-7;
   parameter Real r_L = 0.1;
   parameter Real r_C = 0.1;


equation
   i_D = i_L - i_u;
   v_D = v_u - V_i;
   -v_D = v_L + r_L*i_L + v_O;
   v_L = L * der(i_L);
   i_C = C * der(v_C);
   v_C + r_C * i_C = v_O;
   i_R * R = v_O;
   i_L = i_C + i_R;
   y = v_O;

   if u == 1 then
      v_u = R_on * i_u;
   else
      v_u = R_off * i_u;
   end if;

   if i_D >= 0 then
      v_D = 0;
   else
      v_D = R_off * i_D;
   end if;

end Plant;
