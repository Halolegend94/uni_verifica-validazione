#!/bin/bash
###################################################################################################
#
# Author: Cristian Di Pietrantonio (https://github.com/Halolegend94)
#
# Description: Install easly the last version of JModelica.
# ATTENTION: set manually the requested variables in "manual setting" section before launching this
# Script.
#
###################################################################################################

###################################################################################################
#
#                                  !! MANUAL SETTINGS !!
# Set path containing HSL download. You can download it at
# http://www.hsl.rl.ac.uk/download/coinhsl-archive-linux-x86_64/2014.01.17/
HSLDir="/home/cristian/Software/coinhsl-archive-linux-c86_64-2014.01.17" #must be absolute
# Set the instalation path
InstallLocation="/home/cristian/Sviluppo/JModelica" #must be absolute

#IMPORTANTE!
#Bisogna installare java di oracle e settare la variabile java_path in maniera appropriata
#INSTALL JAVA
#sudo add-apt-repository ppa:webupd8team/java
#sudo apt-get update
#sudo apt-get install oracle-java8-installer -y

###################################################################################################
#                                   SCRIPT STARTS HERE
###################################################################################################

###install dependencies
sudo apt-get -y install g++
sudo apt-get -y install subversion
sudo apt-get -y install gfortran
sudo apt-get -y install ipython
sudo apt-get -y install cmake
sudo apt-get -y install swig
sudo apt-get -y install ant
sudo apt-get -y install python-dev
sudo apt-get -y install python-numpy
sudo apt-get -y install python-scipy
sudo apt-get -y install python-matplotlib
sudo apt-get -y install cython
sudo apt-get -y install python-lxml
sudo apt-get -y install python-nose
sudo apt-get -y install python-jpype
sudo apt-get -y install zlib1g-dev
#
if ! [ -d $InstallLocation ]; then
   mkdir $InstallLocation
fi
if ! [ -d $InstallLocation/tmpBuild ]; then
   mkdir $InstallLocation/tmpBuild
fi
cd $InstallLocation/tmpBuild

########################################################################
##
##                       IPOPT
##
########################################################################

#now get the last version of Ipopt from internet, by parsing its official page
`curl http://www.coin-or.org/Ipopt/documentation/node12.html | grep -oE 'svn co.*?CoinIpopt'`

#get external dependencies
cd CoinIpopt/ThirdParty/Blas
./get.Blas
cd ../Lapack
./get.Lapack
cd ../ASL
./get.ASL
cd ..
#Copy HSL
cp $HSLDir HSL/coinhsl -r
cd ..
#Fist step, build IPOPT
mkdir build
cd build
../configure --prefix=$InstallLocation/CoinIpoptBuild
if [[ $? != 0 ]]; then
   echo "Error configure Ipopt!"
   exit 1
fi
make
if [[ $? != 0 ]]; then
   echo "Error make ipopt!"
   exit 1
fi

make install
if [[ $? != 0 ]]; then
   echo "Error make install ipopt!"
   exit 1
fi
cd ../..

#OK, now install JMODELICA
svn co https://svn.jmodelica.org/truck JMSrc #get last version of jmodelica
cd JMSrc
mkdir build
cd build
../configure --prefix=$InstallLocation --with-ipopt=$InstallLocation/CoinIpoptBuild
make
if [[ $? != 0 ]]; then
   echo "Error make jmodelica!"
   exit 1
fi
make install
if [[ $? != 0 ]]; then
   echo "Error make install jmodelica!"
   exit 1
fi
cd ../../..
rm -rf tmpBuild
