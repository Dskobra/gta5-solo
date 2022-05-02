#!/usr/bin/bash
gta=`ps -ef | grep GTA5.exe | grep -v grep | awk '{print $2}'`
kill -STOP $gta
python3 timeout.py
kill -CONT $gta
