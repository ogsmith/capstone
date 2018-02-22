import serial # you need to install the pySerial :pyserial.sourceforge.net
import time
# your Serial port should be different!
arduino = serial.Serial('/dev/cu.usbmodem1421', 9600)

def onOffFunction():
	command = raw_input("Type something..: ");
	if command =="1":
		print "The LED is on..."
		arduino.write('1')
		onOffFunction()
	elif command =="2":
		print "2 is on..."
		arduino.write('2')
		onOffFunction()
	elif command =="3":
		print "3 is on..."
		arduino.write('3')
		onOffFunction()
	elif command =="4":
		print "4 is on..."
		arduino.write('4')
		onOffFunction()
	elif command =="5":
		print "5 is on..."
		arduino.write('5')
		onOffFunction()
	elif command =="6":
		print "6 is on..."
		arduino.write('6')
		onOffFunction()
	elif command =="7":
		print "7 is on..."
		arduino.write('7')
		onOffFunction()
	elif command =="8":
		print "8 is on..."
		arduino.write('8')
		onOffFunction()
	elif command =="9":
		print "9 is on..."
		arduino.write('9')
		onOffFunction()
	elif command =="t":
		print "10 is on..."
		arduino.write('t')
		onOffFunction()
	elif command =="e":
		print "11 is on..."
		arduino.write('e')
		onOffFunction()
	elif command =="w":
		print "12 is on..."
		arduino.write('w')
		onOffFunction()
	if command =="1 off":
		print "The LED 1 is off..."
		arduino.write('!')
		onOffFunction()
	elif command =="2 off":
		print "2 is off..."
		arduino.write('@')
		onOffFunction()
	elif command == "3 off":
		print "3 is off..."
		arduino.write('#')
		onOffFunction()
	elif command =="4 off":
		print "4 is off..."
		arduino.write('$')
		onOffFunction()
	elif command =="5 off":
		print "5 is off..."
		arduino.write('%')
		onOffFunction()
	elif command =="6 off":
		print "6 is off..."
		arduino.write('^')
		onOffFunction()
	elif command =="7 off":
		print "7 is off..."
		arduino.write('&')
		onOffFunction()
	elif command =="8 off":
		print "8 is off..."
		arduino.write('*')
		onOffFunction()
	elif command =="9 off":
		print "9 is off..."
		arduino.write('(')
		onOffFunction()
	elif command =="10 off":
		print "10 is off..."
		arduino.write('T')
		onOffFunction()
	elif command =="11 off":
		print "11 is off..."
		arduino.write('E')
		onOffFunction()
	elif command =="12 off":
		print "12 is off..."
		arduino.write('W')
		onOffFunction()
	elif command =="bye":
		print "See You!..."
		arduino.close()
	else:
		print "Sorry..type another thing..!"
		onOffFunction()


onOffFunction()
