#!/bin/bash
xrandr --verbose | grep Brightness | cut -f2 -d " " > /home/krystian/skrypty/.brightness.txt
