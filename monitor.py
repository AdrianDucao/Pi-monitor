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
        val = msg
        try:
            clock = val
        except ValueError:
            pass

    time.sleep(1)
    return clock

def memory_usage():
    mem = "for Arm7 processors only"
    err, msg = subprocess.getstatusoutput('vcgencmd get_mem arm')

    if not err:
        mem_val = msg
        try:
            mem = mem_val
        except ValueError:
            pass

    time.sleep(1)
    return mem


def main(stdscr):
    stdscr.addstr(0, 0, "Pi-monitor v1.0 \n")
    stdscr.refresh()
    h, w = stdscr.getmaxyx()
    temp_val = check_CPU_temp()
    clock_speed = check_Clock_speed()
    mem_val = memory_usage()
    value = "CPU temperature: "+str(temp_val)    
    clock_msg = "Clock Speed: "+str(clock_speed)
    mem_allocation = "RAM usage: "+str(mem_val)    

    while(value !=  "CPU temperature Arm7 and up only"):
        temp_val_refresh = check_CPU_temp()
        value = "CPU temperature "+str(temp_val_refresh)
        clock_speed_refresh = check_Clock_speed()
        clock_msg = "Clock speed: "+str(clock_speed_refresh)
        mem_val = memory_usage()
        mem_allocation = "RAM usage: "+str(mem_val)        

        stdscr.addstr(0, 0, "Pi-monitor v1.0 \n")
        stdscr.addstr(3,0, value)
        stdscr.addstr(4,0, clock_msg)
        stdscr.addstr(5,0, mem_allocation)
        stdscr.refresh()            

    print("\n Pi-monitor is for Arm7 CPU's only ")
    stdscr.refresh()
    time.sleep(5)

curses.wrapper(main)


