function AD
    input Real analog_value;
    input Real min;
    input Real max;
    input Real resolution;
    output Real digital_value;
algorithm
    if (analog_value >= max) then
        digital_value := max;
    elseif (analog_value <= min) then
        digital_value := min;
    else
        digital_value := resolution * floor((analog_value / resolution) + 0.5);
    end if;
end AD;

