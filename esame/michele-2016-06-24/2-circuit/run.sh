#!/bin/bash

echo "Esempio esecuzione"
sleep 1
echo "jm_python.sh 1/verify.py"
cd "1"
jm_python.sh verify.py
rm *.fmu
rm *.txt
cd ".."
sleep 1
echo

echo "2.4: Validazione Plant con u = 0"
sleep 1
echo "jm_python.sh 4/verify.py"
cd "4"
jm_python.sh verify.py
rm *.fmu
rm *.txt
cd ".."
sleep 1
echo

echo "2.5: Validazione Plant con u = 1"
sleep 1
echo "jm_python.sh 5/verify.py"
cd "5"
jm_python.sh verify.py
rm *.fmu
rm *.txt
cd ".."
sleep 1
echo

echo "2.6: Verifica software di controllo nello stato iniziale"
sleep 1
echo "jm_python.sh 6/verify.py"
cd "6"
jm_python.sh verify.py
rm *.fmu
rm *.txt
cd ".."
sleep 1
echo

echo "2.7: Verifica software di controllo"
sleep 1
echo "jm_python.sh 7/verify.py"
cd "7"
jm_python.sh verify.py
rm *.fmu
rm *.txt
cd ".."
sleep 1
echo

