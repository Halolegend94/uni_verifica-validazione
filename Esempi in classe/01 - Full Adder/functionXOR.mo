function functionXOR

input Boolean x;
input Boolean y;
output Boolean z;

algorithm

z := (not(x) and y) or (x and not(y));

end functionXOR;
