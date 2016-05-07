record EnvironmentState
   Boolean admissible;
   Integer depth;
end EnvironmentState;

class Environment

   EnvironmentState prec;
   EnvironmentState current;

   parameter Boolean adm0 = true;
   parameter Integer depth0 = 0;
   constant Integer MaxDepth = 5;
   parameter Integer T = 1;

   function nextState
      input EnvironmentState x;

      output EnvironmentState y;

   algorithm
      y.depth := x.depth + 1;
      if(x.admissible and y.depth <= MaxDepth) then
         y.admissible := true;
      else
         y.admissible := false;
      end if;
   end nextState;

initial equation
   current.admissible = adm0;
   current.depth = depth0;

equation
   when sample(0, T) then
      prec.depth = pre(current.depth);
      prec.admissible = pre(current.admissible);
      current = nextState(prec);
   end when;
end Environment;
