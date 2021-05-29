#!/usr/bin/env python3

import curses
import re, subprocess
import time

def check_CPU_temp():
    temp = "Arm7 and up only"
    err, msg = subprocess.getstatusoutput('vcgencmd measure_temp')
    if not err:
        m = re.search(r'-?\d\.?\d*', msg) 
        try:
            temp = float(m.group())
        except ValueError: 
            pass
    time.sleep(1)
    return temp

def check_Clock_speed():
    clock = "Arm7 and up only"
    err, msg = subprocess.getstatusoutput('vcgencmd measure_clock arm')
    if not err:
        m = re.search(r'-?\d\.?\d*', msg)
        try:
            clock = float(m.group())
        except ValueError:
            pass

    time.sleep(1)
    return clock


def main(stdscr):
    stdscr.addstr(0, 0, "Pi-monitor v1.0 \n")
    stdscr.refresh()
    h, w = stdscr.getmaxyx()
    temp_val = check_CPU_temp()
    clock_speed = check_Clock_speed()
    value = "CPU temperature: "+str(temp_val)    
    clock_msg = "Clock Speed: "+str(clock_speed)

    while(value !=  "CPU temperature Arm7 and up only"):
        temp_val_refresh = check_CPU_temp()
        value = "CPU temperature "+str(temp_val_refresh)
        stdscr.addstr(0, 0, "Pi-monitor v1.0 \n")
        stdscr.addstr(3,0, value)
        stdscr.addstr(4,0, clock_msg)
        stdscr.refresh()            

    print("Pi-monitor is for Arm7 CPU's only")
    stdscr.refresh()
    time.sleep(5)

curses.wrapper(main)


