#!/bin/env bash 

if [ $EUID != 0 ];then
        echo "Please run script as root"
        exit -1
fi
pip3 install lxml
pip3 install bs4
pip3 install wget
pip3 install requests
pip3 install inscriptis
pip3 install urlextract
pip3 install colored
