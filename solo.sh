#!/usr/bin/bash
#try replacing GTA5.exe with rdo binary filename. May or may not work.
gta=`ps -ef | grep GTA5.exe | grep -v grep | awk '{print $2}'`
kill -STOP $gta
python3 timeout.py
kill -CONT $gta
