# todo:
# display options           DONE
# get touch data
# send touch data to due

import serial
from tkinter import *

test = True

if not test:
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = '/dev/ttyACM0'
    ser.open()


# Vars
boxH = 100
boxW = 100
v = 0

# Display Buttons
window = Tk()
window.title("Pi Left")

ctx = Canvas(window, width=1280, height=720, background="#222")
ctx.pack()


# Commands for the buttons
def handle_click(event):
    if (event.x >= boxW and event.x <= boxW*2 and event.y >= boxH and event.y <= boxH*2):
        #do_a()
        print(1)
        v = 0
    elif (event.x >= boxW*3 and event.x <= boxW*4 and event.y >= boxH and event.y <= boxH*2):
        #do_b()
        print(2)
        v = 1
    elif (event.x >= boxW*5 and event.x <= boxW*6 and event.y >= boxH and event.y <= boxH*2):
        #do_c()
        print(3)
        v = 2
    elif (event.x >= boxW*7 and event.x <= boxW*8 and event.y >= boxH and event.y <= boxH*2):
        #do_d()
        print(4)
        v = 3
        print(v)

    draw_text()

def draw_text():
    ctx.delete("text1")
    print(v)
    if (v == 0):
        midText = ctx.create_text(640, 360, anchor="center", font=("MS Comic Sans", 12), width = boxH-(boxH/4), tag = "text1", text="Hey")
    elif (v == 1):
        midText = ctx.create_text(640, 360, anchor="center", font=("MS Comic Sans", 12), width = boxH-(boxH/4), tag = "text1", text="Hoy")
    elif (v == 2):
        midText = ctx.create_text(640, 360, anchor="center", font=("MS Comic Sans", 12), width = boxH-(boxH/4), tag = "text1", text="Hiy")
    elif (v == 3):
        midText = ctx.create_text(640, 360, anchor="center", font=("MS Comic Sans", 12), width = boxH-(boxH/4), tag = "text1", text="Huy")



# Create boxes and texts
box1 = ctx.create_rectangle(boxW, boxH, boxW*2, boxH*2, outline="blue", fill="blue")
txt1 = ctx.create_text(boxW*1.5, boxH*1.5, anchor="center", font=("MS Comic Sans", 12), width = boxH-(boxH/4), text="A")

box2 = ctx.create_rectangle(boxW*3, boxH, boxW*4, boxH*2, outline="blue", fill="blue")
txt2 = ctx.create_text(boxW*3.5, boxH*1.5, anchor="center", font=("MS Comic Sans", 12), width = boxH-(boxH/4), text="B")

box3 = ctx.create_rectangle(boxW*5, boxH, boxW*6, boxH*2, outline="blue", fill="blue")
txt3 = ctx.create_text(boxW*5.5, boxH*1.5, anchor="center", font=("MS Comic Sans", 12), width = boxH-(boxH/4), text="C")

box3 = ctx.create_rectangle(boxW*7, boxH, boxW*8, boxH*2, outline="blue", fill="blue")
txt3 = ctx.create_text(boxW*7.5, boxH*1.5, anchor="center", font=("MS Comic Sans", 12), width = boxH-(boxH/4), text="D")

ctx.bind("<Button-1>", handle_click)


window.mainloop()
print("Program Ended Gracefully")