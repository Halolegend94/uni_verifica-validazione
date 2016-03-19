function functionFA
input Boolean x;
input Boolean y;
input Boolean c;
output Boolean z;
output Boolean r;
algorithm
z := functionXOR(functionXOR(x,y),x);
r := functionOR(functionOR(functionAND(x,y),functionAND(y,c)),functionAND(x,c));
end functionFA;
