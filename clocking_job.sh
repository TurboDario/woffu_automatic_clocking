#!/bin/sh
sudo pkill -9 firefox
python3.8 /home/opc/woffu_automatic_clocking/clocking.py &> log
