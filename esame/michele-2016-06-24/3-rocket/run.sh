#!/bin/bash

echo "3.1: Monitor specifica"
sleep 1
echo "jm_python.sh 1/verify.py"
cd "1"
jm_python.sh verify.py
rm *.fmu
rm *.txt
cd ".."
sleep 1
echo

echo "3.2: Validazione plant (u = 0)"
sleep 1
echo "jm_python.sh 2/verify.py"
cd "2"
jm_python.sh verify.py
rm *.fmu
rm *.txt
cd ".."
sleep 1
echo

echo "3.3: Validazione plant (u = 2 * m * g)"
sleep 1
echo "jm_python.sh 3/verify.py"
cd "3"
jm_python.sh verify.py
rm *.fmu
rm *.txt
cd ".."
sleep 1
echo

echo "3.4: Progettazione software di controllo"
sleep 1
echo "jm_python.sh 4/verify.py"
cd "4"
jm_python.sh verify.py
rm *.fmu
rm *.txt
cd ".."
sleep 1
echo

echo "3.5: Verifica software di controllo"
sleep 1
echo "jm_python.sh 5/verify.py"
cd "5"
jm_python.sh verify.py
rm *.fmu
rm *.txt
cd ".."
sleep 1
echo

