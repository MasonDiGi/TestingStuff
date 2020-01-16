import serial

ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/ttyACM0'
ser.open()


while True:
    ser.write(input("Enter Command: ").encode())
    line = ser.readline()
    while line == "":
        line = ser.readline()
    print(line.decode('utf-8'), end="")

