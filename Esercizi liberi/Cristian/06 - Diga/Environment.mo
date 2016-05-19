record EnvironmentState
   Boolean adm;
   Integer depth;
end EnvironmentState;

record Disturbance
   Real riverLoad;
end Disturbance;

model Environment

   parameter Real T = 1; //timestep
   constant Integer MaxDepth = 20;
   constant Real MaxLoad = 10;
   constant Real MinLoad = 1;
   parameter Boolean adm0 = true;
   parameter Integer depth0 = 0;
   parameter Real riverLoad0 = 5; //Kl/s
   EnvironmentState prec, current;
   Disturbance d;

   function next
      input EnvironmentState x;
      input Disturbance d;
      output EnvironmentState y;

   algorithm

      y.depth := x.depth + 1;
      if(x.adm and y.depth <= MaxDepth and d.riverLoad >= MinLoad and d.riverLoad <= MaxLoad) then
         y.adm := true;
      else
         y.adm := false;
      end if;
   end next;

initial equation
   d.riverLoad = riverLoad0;
   current.adm = adm0;
   current.depth = depth0;

equation
   when sample(0, T) then
      prec.adm = pre(current.adm);
      prec.depth = pre(current.depth);
      d.riverLoad = pre(d.riverLoad);
      current = next(prec, d);
   end when;

end Environment;
