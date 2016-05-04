class Environment "This is a the environment of the system."
   /*The environment can produce noise and cause failures*/

   parameter Real avg0 = 0;
   parameter Boolean adm0 = true;
   parameter Integer n0 = 0;
   parameter Integer depth0 = 0;
   parameter Real T = 0.25;
   constant Real omega = 10 * 3.14;
   parameter Real noise0 = -1;
   parameter Real failures0 = -1;
   parameter Real H = 5;

   EnvironmentState prec, current; //relevant states of the environment
   Disturb d; //disturb from the environment

   /*constants*/
   constant Real treshold = 0.5; //represents the admissibility of a disturb state 

   // ===============================================================
   // next
   // ===============================================================
   function next "Compute the next state of the environment"
      input EnvironmentState x;
      input Disturb d;
      output EnvironmentState y;

   algorithm
      y.n := x.n + 1; //increment counter
      y.avg := ((x.avg * x.n) + d.noise) / y.n; //compute new noise average
      y.depth := x.depth + 1;
      if(x.adm and abs(y.avg) < treshold and y.depth <= H) then
         y.adm := true;
      else
         y.adm := false;
      end if;

   end next;

initial equation
   prec.avg = avg0;
   prec.depth = depth0;
   prec.adm = adm0;
   prec.n = n0;
   d.noise = noise0;
   d.failures = failures0;

equation //dynamic of the environment
   when sample(0, T) then
      d.noise = sin(omega * time);
      d.failures = cos(omega * time);
      prec.avg = pre(current.avg);
      prec.depth = pre(current.depth);
      prec.adm = pre(current.adm);
      prec.n = pre(current.n);

      current = next(prec, d);
   end when;

end Environment;
