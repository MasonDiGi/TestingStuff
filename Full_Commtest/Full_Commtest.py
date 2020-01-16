import serial

ser = serial.Serial(
    port='/dev/AMA0', # Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
    baudrate = 9600,
    timeout = 1
)

ser.write(toSend)
while True:
    print(ser.readline());
ser.close()