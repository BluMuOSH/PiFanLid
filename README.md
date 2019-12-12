# PiFanLid
Welcome to the Pi Fan LID (LID = Layer Incorporating Devices.) A PCB with a fan to keep your Raspberry Pi cool

It is intended to sit on top of a Raspberry Pi 4B, but will work on a 3B or 3B+ too.

An NPN transistor is included to allow PWM control of the fan speed through any of eight different GPIO pins. GPIO18 allows hardware PWM, but software PWM works well enough in this application and is available on any of the GPIO pins.

The three files: PiFanLidR1.pro, PiFanLidR1.sch, and PiFanLidR1.kicad_pcb constitute a KiCAD project. (KiCAD is an open source schematic capture and PCB layout program.) You can download KiCAD to open the project and possibly make changes, or send PiFanLidR1.kicad_pcb to https://oshpark.com/ to have a PCB made. They should charge around $25 or $30 for three boards.

Or... drop me an email. If I have any boards left over, I might send you one by USPS.

Required materials:

1. PCB
2. 5V, 30x30mm fan (available from adafruit)
3. PN2222 transistor
4. base current limiting resistor (1k works well)
5. freewheeling diode (1N4001 for example)
6. 2x20 pin header socket (available from adafruit. The extra tall version is recommended.)
7. standoffs to support the PCB. 4 is best. 2 is OK. You can get away with none if you handle carefully.

fan-ctrl.py is a python script that will control the speed of the fan depending on the temperature of the CPU.
fan-ctrl.sh is a shell script that can be used to start fan-ctrl.py at boot up. See Pi Lid Assembly and Installation.pdf for instructions.

Aerandir14 wrote an excellent description of the circuit. It can be found at
https://www.instructables.com/id/PWM-Regulated-Fan-Based-on-CPU-Temperature-for-Ras/

My python code is based loosely on his.
