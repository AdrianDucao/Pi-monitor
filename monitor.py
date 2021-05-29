#!/usr/bin/env python3

import curses
import re, subprocess
import time

def check_CPU_temp():
    temp = "is for Raspberry Pi only"
    err, msg = subprocess.getstatusoutput('vcgencmd measure_temp')
    if not err:
        m = re.search(r'-?\d\.?\d*', msg) 
        try:
            temp = float(m.group())
        except ValueError: 
            pass
    return temp

def main(stdscr):
    stdscr.refresh()
    h, w = stdscr.getmaxyx()
    temp_val = check_CPU_temp()
    value = "CPU temperature "+str(temp_val)  
    
    while(value !=  "CPU temperature is for Raaspberry Pi only"):
        reload(value)
	stdscr.addstr(0,0, value)
        stdscr.refresh()            
    
    print("Pi-monitor is for Arm7 CPU's only")
    stdscr.refresh()
    time.sleep(5)

curses.wrapper(main)
