#!/bin/bash

if [ $EUID != 0 ];then
        echo "please run as root"
        exit
fi
pip3 install lxml
pip3 install bs4
pip3 install wget
pip3 install requests
pip3 install inscriptis
pip3 install urlextract
pip3 install colored
pip3 install pyfiglet
