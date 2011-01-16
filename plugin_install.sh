#!/bin/bash

cp export.py ~/.gimp-2.6/plug-ins/
chmod +x ~/.gimp-2.6/plug-ins/export.py
killall -9 gimp
gimp&