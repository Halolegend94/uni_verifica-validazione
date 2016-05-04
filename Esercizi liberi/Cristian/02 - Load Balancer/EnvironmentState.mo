record EnvironmentState "This record represents a state of the environment"

   Real avg;    //mean of the load
   Boolean adm; //this is true if and only the state is admissible
   Integer n;   //used to compute the average value of noise
   Integer depth; //used to give an upper bound to the length of execution path.
end EnvironmentState;
