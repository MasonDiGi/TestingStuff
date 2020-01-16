import serial

inText = ''


ser = serial.Serial(
    port='/dev/ttyACM0', # Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
    baudrate = 9600,
    timeout = 1
)

toSend = input("Plz give one or zero ")
ser.write(toSend.encode('utf-8'))
while True:
    inText = ser.readline()
    if inText != b'':
        print(inText.strip('a'))
        print("Hey")
        break

ser.close()