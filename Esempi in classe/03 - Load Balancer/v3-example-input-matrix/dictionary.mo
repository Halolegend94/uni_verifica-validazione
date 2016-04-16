
record Dictionary

 constant Integer sznoise (start=3);
 constant Integer szfail (start=2);

 constant Real noise[3] (start = {-0.5, 0.0, 0.5});
 constant Integer failures[2] (start = {0, 1});

end Dictionary;


record Disturbance
     Integer noise;
     Integer failures;
end Disturbance;
