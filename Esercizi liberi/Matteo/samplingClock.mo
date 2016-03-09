model SamplingClock
    Integer i;
    discrete Real r;
equation
    when sample(2,0.5) then
	i = i+1;
	r = pre(r)+0.3;
    end when;
end SamplingClock;
