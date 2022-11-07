#!/bin/bash
xrandr --verbose | grep Brightness | cut -f2 -d " " > /home/krystian/brightness-manager/.brightness.txt
