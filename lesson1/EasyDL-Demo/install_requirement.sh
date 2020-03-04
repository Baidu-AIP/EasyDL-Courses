#!/bin/bash
which pip3
if [ $? == 0 ];
then
    pip3 install numpy
    pip3 install cython
    pip3 install -r requirements.txt -i https://pypi.douban.com/simple/ 
    exit 0
fi

which pip
if [ $? == 0 ];
then
    pip install numpy
    pip install cython
    pip install -r requirements.txt -i https://pypi.douban.com/simple/ 
    exit 0
fi

echo "please install pip first"