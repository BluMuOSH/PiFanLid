# PiFanLid
A PCB with a fan to keep your Raspberry Pi cool

Welcome to the Pi Fan Lid (Lid = Layer Incorporating Devices.)

It is intended to sit on top of a Raspberry Pi 4B, but will work on a 3B or 3B+ too.

An NPN transistor is included to allow PWM control of the fan speed through any of eight different GPIO pins. GPIO18 allows hardware PWM, but software PWM works well enough in this application and is available on any of the GPIO pins.

Required materials:

1. PCB
2. 5V, 30x30mm fan (available from adafruit)
3. PN2222 transistor
4. base current limiting resistor (1k works well)
5. freewheeling diode (1N4001 for example)
6. 2x20 pin header socket (available from adafruit. The extra tall version is recommended.)
7. standoffs to support the PCB. You can get away with two, but four is better.

Aerandir14 wrote an excellent description of the circuit along with working python code. It can be found at
https://www.instructables.com/id/PWM-Regulated-Fan-Based-on-CPU-Temperature-for-Ras/
