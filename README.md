# Pi-monitor
```
Pi-monitor v1.0


[CPU temperature] 40.0
[Clock speed:] frequency(48)=6001171840
[RAM Usage:]
              total        used        free      shared  buff/cache   available
Mem:           3838         177        3075          60         585        3465
[Uptime:] up 1 day, 15 hours, 39 minutes

```
a console user interface to monitor in real-time your headless Raspberry Pi's system while on ssh or plugged in as regular desktop use.

### Features
note: only works with Arm Processors
* CPU temperature
* CPU clock speed
* RAM allocation
* Uptime information

### Setup
```
$ ssh user@<ipaddress>

$ git clone https://github.com/AdrianDucao/Pi-monitor.git
$ cd Pi-monitor
$ ./monitor.py

```
