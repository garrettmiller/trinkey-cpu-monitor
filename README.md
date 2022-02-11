# trinkey-cpu-monitor
## CPU/process monitoring features leveraging the Adafruit Neo Trinkey (https://www.adafruit.com/product/4870) as a state display.

### Requirements:
Requires CircuitPython (https://circuitpython.org/board/neopixel_trinkey_m0/)

Ensure the following libraries are included in the lib/ folder on the Trinkey: `neopixel, board, color, supervisor, time`

Host side requires `serial, psutil`

### Usage:

Load `serial_control.py` as `code.py` on the Trinkey, then run `trinkey_cpu_monitor.py` on your host system.  Be sure to define serial device and a process name of interest to monitor (if desired) 

Originally based on scripts by Dave Parker (https://github.com/daveparker/neotrinkey)