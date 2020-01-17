import serial
import time

var1 = b'\x49'
var2 = b'\x4A'


ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/ttyAMA0' #AMA0
ser.open()

#Continually write to the due
while True:
    time.sleep(.5)
    ser.write(b'\x02')
    ser.write(var1)
    ser.write(var2)
    ser.write(b'\x03')