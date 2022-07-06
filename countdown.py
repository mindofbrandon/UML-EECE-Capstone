from tkinter import *   
import tkinter as Tkinter
from math import cos, sin
from time import sleep, gmtime
from tkinter.ttk import Progressbar
from tkinter import messagebox
from playsound import playsound
import multiprocessing

win = Tk()
win.geometry("1024x600")
win.title("Time Counter")

p = multiprocessing.Process(target=playsound, args=('alarm.mp3'))

stop_sound = False
sound = False

def stop_mp3():
    global stop_sound
    stop_sound = True

def play():
    while(True):
        playsound('alarm.mp3')
        if stop_sound:
            break

def sound_ON():
    global sound
    sound = True

def sound_OFF():
    global sound
    sound = False

sound_button = Button(win, text='Sound ON', bd='5', command = sound_ON)
sound_button.place(x = 70, y = 300)
sound_button2 = Button(win, text='Sound OFF', bd='5', command = sound_OFF)
sound_button2.place(x = 70, y = 350)

def sound_trigger():
    turn_sound = Button(win, text='Stop Sound', bd='7' , command = p.terminate())
    turn_sound.place(x = 70, y = 400)

hour=StringVar()
minute=StringVar()
second=StringVar()
  
hour.set("0")
minute.set("0")
second.set("0")

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
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp > -1:

        if running:
            mins,secs = divmod(temp,60)
            hours=0
            if mins >60:
                hours, mins = divmod(mins, 60)
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))
            win.update()
            sleep(1)
            if (temp == 0):
                if (sound):
                    p.start()
                    sound_trigger()
                messagebox.showinfo("Time Countdown", "Time's up ")
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

def drawcircle(Alpha,Beta,Rayon,Couleur,can):
    x1,y1,x2,y2=Alpha-Rayon, Beta-Rayon, Alpha+Rayon, Beta+Rayon
    can.create_oval(x1,y1,x2,y2,fill=Couleur)

def drawSecAig(CoordA, CoordZ, Taille, Omega, can):
    Pi = 3.14159 
    Omega = (Omega-15) * 6
    can.create_line(CoordA + (Taille/1.5) * cos(Pi*(Omega/180)), CoordZ + (Taille/1.5) * sin(Pi*(Omega/180)), CoordA - (Taille/6) * cos(Pi*(Omega/180)), CoordZ - (Taille/6) * sin(Pi*(Omega/180)), fill = "red")

def fondhorloge(CoordA, CoordZ, Taille, can1):
    Pi = 3.141592

    drawcircle(CoordA, CoordZ, Taille, "ivory3",can1)
    drawcircle(CoordA, CoordZ, Taille/80, "ivory3",can1)
    can1.create_line(CoordA + (Taille - (Taille/15)), CoordZ, CoordA + (Taille - (Taille/5)), CoordZ) 
    can1.create_line(CoordA, CoordZ + (Taille - (Taille/15)), CoordA, CoordZ + (Taille - (Taille/5)))
    can1.create_line(CoordA - (Taille - (Taille/15)), CoordZ, CoordA - (Taille - (Taille/5)), CoordZ)
    can1.create_line(CoordA, CoordZ - (Taille - (Taille/15)), CoordA, CoordZ - (Taille - (Taille/5)))

    can1.create_line(CoordA + (Taille/1.05) * cos(Pi*(30/180)), CoordZ + (Taille/1.05) * sin(Pi*(30/180)), CoordA + (Taille/1.20) * cos(Pi*(30/180)), CoordZ + (Taille/1.20) * sin(Pi*(30/180)))
    can1.create_line(CoordA + (Taille/1.05) * cos(Pi*(60/180)), CoordZ + (Taille/1.05) * sin(Pi*(60/180)), CoordA + (Taille/1.20) * cos(Pi*(60/180)), CoordZ + (Taille/1.20) * sin(Pi*(60/180)))

    can1.create_line(CoordA - (Taille/1.05) * cos(Pi*(30/180)), CoordZ - (Taille/1.05) * sin(Pi*(30/180)), CoordA - (Taille/1.20) * cos(Pi*(30/180)), CoordZ - (Taille/1.20) * sin(Pi*(30/180)))
    can1.create_line(CoordA - (Taille/1.05) * cos(Pi*(60/180)), CoordZ - (Taille/1.05) * sin(Pi*(60/180)), CoordA - (Taille/1.20) * cos(Pi*(60/180)), CoordZ - (Taille/1.20) * sin(Pi*(60/180)))

    can1.create_line(CoordA + (Taille/1.05) * cos(Pi*(30/180)), CoordZ - (Taille/1.05) * sin(Pi*(30/180)), CoordA + (Taille/1.20) * cos(Pi*(30/180)), CoordZ - (Taille/1.20) * sin(Pi*(30/180)))
    can1.create_line(CoordA + (Taille/1.05) * cos(Pi*(60/180)), CoordZ - (Taille/1.05) * sin(Pi*(60/180)), CoordA + (Taille/1.20) * cos(Pi*(60/180)), CoordZ - (Taille/1.20) * sin(Pi*(60/180)))

    can1.create_line(CoordA - (Taille/1.05) * cos(Pi*(30/180)), CoordZ + (Taille/1.05) * sin(Pi*(30/180)), CoordA - (Taille/1.20) * cos(Pi*(30/180)), CoordZ + (Taille/1.20) * sin(Pi*(30/180)))
    can1.create_line(CoordA - (Taille/1.05) * cos(Pi*(60/180)), CoordZ + (Taille/1.05) * sin(Pi*(60/180)), CoordA - (Taille/1.20) * cos(Pi*(60/180)), CoordZ + (Taille/1.20) * sin(Pi*(60/180)))

def HORLOGE1(Gamma, Pi, Epsylon):
    fondhorloge(Gamma, Pi, Epsylon, can1)
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