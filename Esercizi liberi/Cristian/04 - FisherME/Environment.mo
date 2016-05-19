record Disturbance
   Real drift1;
   Real drift2;
end Disturbance;

record EnvironmentState
   Integer depth;
   Boolean adm;
end EnvironmentState;

class Environment

   EnvironmentState current, prec;
   Disturbance d;

   parameter Real T = 0.5;
   parameter Real drift1_0 = 0;
   parameter Real drift2_0 = 0;
   parameter Boolean adm0 = true;
   parameter Integer depth0 = 0;

   constant Real maxDrift1 = 4/5;
   constant Real maxDrift2 = 11/10;
   constant Integer maxDepth = 10;

   function nextState
      input EnvironmentState currentState;
      input Disturbance d;
      output EnvironmentState nextState;

   algorithm
      nextState.depth := currentState.depth + 1;
      if(currentState.adm and nextState.depth <= maxDepth and
         abs(d.drift1) <= maxDrift1 and abs(d.drift2) <= maxDrift2) then
         nextState.adm := true;
      else
         nextState.adm := false;
      end if;
end nextState;

initial equation
   current.depth = depth0;
   current.adm = adm0;
   d.drift1 = drift1_0;
   d.drift2 = drift2_0;

equation
   when sample(0, T) then
      d.drift1 = pre(d.drift1);
      d.drift2 = pre(d.drift2);
      prec.depth = pre(current.depth);
      prec.adm = pre(current.adm);
      current = nextState(prec, d);
   end when;
end Environment;
