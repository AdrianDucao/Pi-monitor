#!/usr/bin/env python3

import time
import curses
import re, subprocess


def check_CPU_temp():
    temp = None
    err, msg = subprocess.getstatusoutput('vcgencmd measure_temp')
    if not err:
        m = re.search(r'-?\d\.?\d*', msg)   # a solution with a  regex
        try:
            temp = float(m.group())
        except ValueError: # catch only error needed
            pass
    return temp, msg

def main(stdscr):
    h, w = stdscr.getmaxyx()
    temp = check_CPU_temp()
    msg = "CPU Temp is"+str(temp)  

    stdscr.addstr(0,0, msg)
    stdscr.refresh()    
    time.sleep(3)
curses.wrapper(main)
