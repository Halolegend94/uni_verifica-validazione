#!/bin/bash
###################################################################################################
#
# Author: Cristian Di Pietrantonio (https://github.com/Halolegend94)
# Version: 1.0
# Description: Easly install the last version of JModelica.
# ATTENTION: set manually the requested variables in "manual setting" section before launching this
# Script.
#
# USAGE:
# installJModelica.sh [install | update] [all | jmodelica_latest | jmodelica_stable ]
#
# You can install/update only jmodelica if you have previously installed Ipopt, but you cannot install
# only Ipopt (not the purpose of this script) nor update to a newer version without reinstalling jmodelica
# because the newer version could not be supported.
#
###################################################################################################

###################################################################################################
#
#                                  !! MANUAL SETTINGS !!
#
# Set path containing HSL download. You can download it at (must be absolute). I suggest to save these
# libraries permanently on disk as the access to these is limited. Choose a place to save them and
# set the HSLDir to that folder.
# http://www.hsl.rl.ac.uk/download/coinhsl-archive-linux-x86_64/2014.01.17/
#
    HSLDir="/home/master/Software/coinhsl-archive-linux-c86_64-2014.01.17"
#
# Set the instalation path (must be absolute)
# !!! IMPORTANT !!!: Leave this path only for jmodelica. In case of update command, this folder will
# be deleted and created again.
#
    InstallLocation="/home/master/Sviluppo/JModelica"
#
# Set the link to the last stable version of JModelica (subversion repo)
#
    StableJModelica="https://svn.jmodelica.org/tags/1.17/"
#
# IMPORTANT!
# Oracle's JavaJVM must be installed (not openjdk)! Use the following commands to install Java
# on your machine.
#
# sudo add-apt-repository ppa:webupd8team/java
# sudo apt-get update
# sudo apt-get install oracle-java8-installer -y
#
# Now set the enviroment var JAVA_HOME to be the path to the jvm (it looks like: /usr/lin/jvm/<folder>)
# in your shell config file (like .bashrc).
# export JAVA_HOME="/usr/lib/jvm/<java-folder-here>"

###################################################################################################
#                                   SCRIPT STARTS HERE
###################################################################################################

#check script parameters
if (( $# < 2  )); then
    echo "Missing some parameter! Usage [install | update] [all | jmodelica_latest | jmodelica_stable ]"
    exit 1

elif [ "$1" != "install" ] && [ "$1" != "update" ]; then
    echo "The fist parameter is not a known command. Usage [install | update] [all | jmodelica_latest | jmodelica_stable ]"
    exit 1

elif [ "$2" != "all" ] && [ "$2" != "jmodelica_latest" ] && [ "$2" != "jmodelica_stable" ]; then
    echo "The second parameter is not a known option. Usage [install | update] [all | jmodelica_latest | jmodelica_stable ]"
    exit 1
fi

isUpdate=false
if [ "$1" == "update" ]; then
    isUpdate=true
fi

isAll=false
if [ "$2" == "all" ]; then
    isAll=true
fi

# install dependencies (or update)
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

if [ $isUpdate == true ]; then
    if [ $isAll == true ]; then
        #clean the directory
        echo "!! IMPORTANT !!"
        echo "I'm going to delete the installation folder and create it again from scratch. Proceed? [y/n]"
        read confirmation
        if [ "$confirmation" != "y" ]; then
            echo "Aborting update"
            exit 1
        else
            rm -rf $InstallLocation
        fi
    else
        #remove all but CoinIpoptBuild folder
        if ! [ -d $InstallLocation/CoinIpoptBuild ]; then
            echo "Ipopt directory does not exists! Run the script in install mode or update all"
            exit 1
        fi
        cp -r $InstallLocation/CoinIpoptBuild $InstallLocation/../_tmpCoinIpoptBuild
        if [ $? != 0 ]; then
            echo "Error while creating a temporary copy of IPOPT installation"
            exit 1
        fi
        rm -rf $InstallLocation
        #the folder will be copied later
    fi
fi
# create necessary folders
if ! [ -d $InstallLocation/tmpBuild ]; then
   mkdir $InstallLocation/tmpBuild -p
fi

if [ $isUpdate == true ] && ! [ $isAll == true ]; then
    #recopy CoinIpoptBuild folder
    cp -r $InstallLocation/../_tmpCoinIpoptBuild $InstallLocation/CoinIpoptBuild
    if [ $? != 0 ]; then
        echo "Error while recovering the temporary copy of IPOPT installation"
        exit 1
    fi
    rm -rf $InstallLocation/../_tmpCoinIpoptBuild
fi

cd $InstallLocation/tmpBuild

###################################################################################################
##
##                                       IPOPT
##
###################################################################################################
if [ $isAll == true ]; then
    #now get the last version of Ipopt (math libraries) from internet, by parsing its official page
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
fi

###################################################################################################
##
##                                    JMODELICA
##
###################################################################################################
latestVersion="https://svn.jmodelica.org/trunk"
chosenVersion=""
if [ "$2" == "jmodelica_latest" ]; then
    chosenVersion=$latestVersion
else
    chosenVersion=$StableJModelica
fi

svn co $chosenVersion JMSrc #copy repository
if [[ $? != 0 ]]; then
   echo "Error downloading Jmodelica repo!"
   exit 1
fi

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
chmod -R 0775 .
echo "Script finished its execution!"
