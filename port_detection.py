import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
for p in ports:
    if "Generic" in p[1]:
        print p[0]
