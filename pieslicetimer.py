import tkinter
from tkinter import *
import tkinter as Tkinter
from math import cos, sin
from time import sleep, gmtime
from tkinter.ttk import Progressbar
from tkinter import messagebox
from tkinter import Canvas

# DIGITAL TIME DISPLAY (hh:mm:ss) with START button
# creating Tk window
win = Tk()

# setting geometry of tk window
win.geometry("1024x600")

# Using title() to display a message in
# the dialogue box of the message in the
# title bar.
win.title("Time Counter")

canvas=Canvas (win)
canvas.pack()
# Declaration of variables
hour = StringVar()
minute = StringVar()
second = StringVar()

# setting the default value as 0
hour.set("0")
minute.set("0")
second.set("0")

# Use of Entry class to take input from the user
hourEntry = Entry(win, width=3, font=("Arial", 18, ""),
                  textvariable=hour)
hourEntry.place(x=80, y=20)

minuteEntry = Entry(win, width=3, font=("Arial", 18, ""),
                    textvariable=minute)
minuteEntry.place(x=130, y=20)

secondEntry = Entry(win, width=3, font=("Arial", 18, ""),
                    textvariable=second)
secondEntry.place(x=180, y=20)

running = False
wait = True



def submit():

    try:
        # the input provided by the user is
        # stored in here :temp
        totaltemp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
        temp=totaltemp




    except:
        print("Please input the right value")
    while temp > -1:
        if running:
            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins, secs = divmod(temp, 60)
            HORLOGE1(250, 250, 200, temp,totaltemp)

            # Converting the input entered in mins or secs to hours,
            # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
            # 50min: 0sec)
            hours = 0
            if mins > 60:
                # divmod(firstvalue = temp//60, secondvalue
                # = temp%60)
                hours, mins = divmod(mins, 60)

            # using format () method to store the value up to
            # two decimal places
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))

            # updating the GUI window after decrementing the
            # temp value every time
            win.update()
            sleep(1)

            # when temp value = 0; then a messagebox pop's up
            # with a message:"Time's up"
            if (temp == 0):
                messagebox.showinfo("Time Countdown", "Time's up ")

            # after every one sec the value of temp will be decremented
            # by one

            temp -= 1

        else:
            btn.wait_variable(wait)


def start():
    global running, wait
    running = True
    wait = True

    submit()


def stop():
    global running
    running = False
    submit()


btn = Button(win, text='Start', bd='5', command=start)
btn.place(x=70, y=120)
btn2 = Button(win, text='Stop', bd='5', command=stop)
btn2.place(x=70, y=90)


# ANALOG CLOCK
def drawcircle(Alpha, Beta, Rayon, Couleur, can):  # draw a circle base on center coord radius and color
    x1, y1, x2, y2 = Alpha - Rayon, Beta - Rayon, Alpha + Rayon, Beta + Rayon
    clk=can.create_oval(x1, y1, x2, y2, fill=Couleur)
    can.tag_lower(clk)




def fondhorloge(CoordA, CoordZ, Taille, can1,temp,temp2):  # function drawing the backgroud of the clock
    Pi = 3.141592
    increment=temp2/36
    global chunk
    chunk=temp2-increment

    if temp<chunk:
        arc=can1.create_arc(50, 50, 450, 450,extent=-10,start=90, fill="red")
        can1.tag_raise(arc)
    if temp<(chunk-increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-20,start=90,fill="red")
    if temp<(chunk-2*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-30,start=90,fill="red")
    if temp<(chunk-3*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-40,start=90,fill="red")
    if temp<(chunk-4*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-50,start=90,fill="red")
    if temp<(chunk-5*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-60,start=90,fill="red")
    if temp<(chunk-6*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-70,start=90,fill="red")
    if temp<(chunk-7*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-80,start=90,fill="red")
    if temp<(chunk-8*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-90,start=90,fill="red")
    if temp<(chunk-9*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-100,start=90,fill="red")
    if temp<(chunk-10*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-110,start=90,fill="red")
    if temp<(chunk-11*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-120,start=90,fill="red")
    if temp<(chunk-12*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-130,start=90,fill="red")
    if temp<(chunk-13*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-140,start=90,fill="red")
    if temp<(chunk-14*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-150,start=90,fill="red")
    if temp<(chunk-15*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-160,start=90,fill="red")
    if temp<(chunk-16*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-170,start=90,fill="red")
    if temp<(chunk-17*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-180,start=90,fill="red")
    if temp<(chunk-18*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-190,start=90,fill="red")
    if temp<(chunk-19*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-200,start=90,fill="red")
    if temp<(chunk-20*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-210,start=90,fill="red")
    if temp<(chunk-21*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-220,start=90,fill="red")
    if temp<(chunk-22*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-230,start=90,fill="red")
    if temp<(chunk-23*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-240,start=90,fill="red")
    if temp<(chunk-24*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-250,start=90,fill="red")
    if temp<(chunk-25*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-260,start=90,fill="red")
    if temp<(chunk-26*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-270,start=90,fill="red")
    if temp<(chunk-27*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-280,start=90,fill="red")
    if temp<(chunk-28*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-290,start=90,fill="red")
    if temp<(chunk-29*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-300,start=90,fill="red")
    if temp<(chunk-30*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-310,start=90,fill="red")
    if temp<(chunk-31*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-320,start=90,fill="red")
    if temp<(chunk-32*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-330,start=90,fill="red")
    if temp<(chunk-33*increment):
        arc=can1.create_arc(50, 50, 450, 450,extent=-340,start=90,fill="red")
    if temp < (chunk - 34 * increment):
        arc = can1.create_arc(50, 50, 450, 450, extent=-350, start=90, fill="red")
    if temp < (chunk - 35 * increment):
        arc = can1.create_arc(50, 50, 450, 450, extent=-360, start=90, fill="red")

    drawcircle(CoordA, CoordZ, Taille / 80, "white", can1)  # central point/needle articulation
    drawcircle(CoordA, 250, 200, "ivory3", can1)  # backgroud


# PRINCIPLE FUNCTION (here the problem starts)

def HORLOGE1(Gamma, Pi, Epsylon,temp,temp2):  # draw a clock with the center position x/x = gamma/pi and the radius = epsylon

    fondhorloge(Gamma, Pi, Epsylon, can1,temp,temp2)  # extracting time value
    patate = gmtime()
    seconde = patate[5]

    win.after(1000, lambda: HORLOGE1(250, 250, 200,temp,temp2))


can1 = Canvas(win, bg="burlywood1", height=500, width=500)
can1.pack()







win.mainloop()
win.destroy()