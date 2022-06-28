
from tkinter import *   
import tkinter as Tkinter
from math import cos, sin
from time import sleep, gmtime
from tkinter.ttk import Progressbar
from tkinter import messagebox

# DIGITAL TIME DISPLAY (hh:mm:ss) with START button
# creating Tk window
win = Tk()
  
# setting geometry of tk window
win.geometry("1024x600")
  
# Using title() to display a message in
# the dialogue box of the message in the
# title bar.
win.title("Time Counter")
  
# Declaration of variables
hour=StringVar()
minute=StringVar()
second=StringVar()
  
# setting the default value as 0
hour.set("0")
minute.set("0")
second.set("0")
  
# Use of Entry class to take input from the user
hourEntry= Entry(win, width=3, font=("Arial",18,""),
                 textvariable=hour)
hourEntry.place(x=80,y=20)
  
minuteEntry= Entry(win, width=3, font=("Arial",18,""),
                   textvariable=minute)
minuteEntry.place(x=130,y=20)
  
secondEntry= Entry(win, width=3, font=("Arial",18,""),
                   textvariable=second)
secondEntry.place(x=180,y=20)
  
running = False
wait = True
def submit():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp > -1:

        if running:
            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins,secs = divmod(temp,60)
    
            # Converting the input entered in mins or secs to hours,
            # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
            # 50min: 0sec)
            hours=0
            if mins >60:
                
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

btn = Button(win, text='Start', bd='5', command= start)
btn.place(x = 70,y = 120)
btn2 = Button(win, text='Stop', bd='5', command = stop)
btn2.place(x = 70, y=90)


# ANALOG CLOCK
def drawcircle(Alpha,Beta,Rayon,Couleur,can): #draw a circle base on center coord radius and color
    x1,y1,x2,y2=Alpha-Rayon, Beta-Rayon, Alpha+Rayon, Beta+Rayon
    can.create_oval(x1,y1,x2,y2,fill=Couleur)

def drawSecAig(CoordA, CoordZ, Taille, Omega, can): #function to draw the hour hand
    Pi = 3.14159 # controls size of "jump" of hand in each interval
    Omega = (Omega-15) * 6
    can.create_line(CoordA + (Taille/1.5) * cos(Pi*(Omega/180)), CoordZ + (Taille/1.5) * sin(Pi*(Omega/180)), CoordA - (Taille/6) * cos(Pi*(Omega/180)), CoordZ - (Taille/6) * sin(Pi*(Omega/180)), fill = "red")

def fondhorloge(CoordA, CoordZ, Taille, can1):  #function drawing the backgroud of the clock
    Pi = 3.141592

    drawcircle(CoordA, CoordZ, Taille, "ivory3",can1)#backgroud
    drawcircle(CoordA, CoordZ, Taille/80, "ivory3",can1)#central point/needle articulation
    can1.create_line(CoordA + (Taille - (Taille/15)), CoordZ, CoordA + (Taille - (Taille/5)), CoordZ) #drawing the N/S/E/W decorativ hour position
    can1.create_line(CoordA, CoordZ + (Taille - (Taille/15)), CoordA, CoordZ + (Taille - (Taille/5)))
    can1.create_line(CoordA - (Taille - (Taille/15)), CoordZ, CoordA - (Taille - (Taille/5)), CoordZ)
    can1.create_line(CoordA, CoordZ - (Taille - (Taille/15)), CoordA, CoordZ - (Taille - (Taille/5)))

    #here, this 4*2 line defined the position of the 8 intermediate line between the N/S/E/W decorativ line.
    can1.create_line(CoordA + (Taille/1.05) * cos(Pi*(30/180)), CoordZ + (Taille/1.05) * sin(Pi*(30/180)), CoordA + (Taille/1.20) * cos(Pi*(30/180)), CoordZ + (Taille/1.20) * sin(Pi*(30/180)))
    can1.create_line(CoordA + (Taille/1.05) * cos(Pi*(60/180)), CoordZ + (Taille/1.05) * sin(Pi*(60/180)), CoordA + (Taille/1.20) * cos(Pi*(60/180)), CoordZ + (Taille/1.20) * sin(Pi*(60/180)))

    can1.create_line(CoordA - (Taille/1.05) * cos(Pi*(30/180)), CoordZ - (Taille/1.05) * sin(Pi*(30/180)), CoordA - (Taille/1.20) * cos(Pi*(30/180)), CoordZ - (Taille/1.20) * sin(Pi*(30/180)))
    can1.create_line(CoordA - (Taille/1.05) * cos(Pi*(60/180)), CoordZ - (Taille/1.05) * sin(Pi*(60/180)), CoordA - (Taille/1.20) * cos(Pi*(60/180)), CoordZ - (Taille/1.20) * sin(Pi*(60/180)))

    can1.create_line(CoordA + (Taille/1.05) * cos(Pi*(30/180)), CoordZ - (Taille/1.05) * sin(Pi*(30/180)), CoordA + (Taille/1.20) * cos(Pi*(30/180)), CoordZ - (Taille/1.20) * sin(Pi*(30/180)))
    can1.create_line(CoordA + (Taille/1.05) * cos(Pi*(60/180)), CoordZ - (Taille/1.05) * sin(Pi*(60/180)), CoordA + (Taille/1.20) * cos(Pi*(60/180)), CoordZ - (Taille/1.20) * sin(Pi*(60/180)))

    can1.create_line(CoordA - (Taille/1.05) * cos(Pi*(30/180)), CoordZ + (Taille/1.05) * sin(Pi*(30/180)), CoordA - (Taille/1.20) * cos(Pi*(30/180)), CoordZ + (Taille/1.20) * sin(Pi*(30/180)))
    can1.create_line(CoordA - (Taille/1.05) * cos(Pi*(60/180)), CoordZ + (Taille/1.05) * sin(Pi*(60/180)), CoordA - (Taille/1.20) * cos(Pi*(60/180)), CoordZ + (Taille/1.20) * sin(Pi*(60/180)))

#PRINCIPLE FUNCTION (here the problem starts)

def HORLOGE1(Gamma, Pi, Epsylon):# draw a clock with the center position x/x = gamma/pi and the radius = epsylon
    fondhorloge(Gamma, Pi, Epsylon, can1)# extracting time value
    patate = gmtime()
    seconde = patate[5]

    drawSecAig(Gamma, Pi, Epsylon, seconde, can1)
    win.after(1000, lambda: HORLOGE1(250, 250, 200))

can1 = Canvas(win, bg="burlywood1", height=500, width=500)
can1.pack()

HORLOGE1(250, 250, 200)

pb2 = Progressbar(
    win,
    orient = HORIZONTAL,
    length = 75,
    mode = 'indeterminate'
    )

pb2.place(x=20, y=550)
pb2.start(3)

win.mainloop()
win.destroy()