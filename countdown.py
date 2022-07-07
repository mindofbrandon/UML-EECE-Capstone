from tkinter import *   
import pygame
from pygame.locals import *
import tkinter as Tkinter
from math import cos, sin
from time import sleep, gmtime
from tkinter.ttk import Progressbar
from tkinter import messagebox
from playsound import playsound

win = Tk()
win.geometry("1024x600")
win.title("Time Counter")

pygame.mixer.init()
pygame.mixer.music.load('alarm.mp3')

stop_sound = False
sound = False

label1 = Label(win, text = "Sound Alarm is OFF")
label1.place(x=70,y=400)

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
    label1 = Label(win, text = "Sound Alarm is ON")
    label1.place(x=70,y=400)

def sound_OFF():
    global sound
    sound = False
    label1 = Label(win, text = "Sound Alarm is OFF")
    label1.place(x=70,y=400)

sound_button = Button(win, text='Sound ON', bd='5', command = sound_ON)
sound_button.place(x = 70, y = 300)
sound_button2 = Button(win, text='Sound OFF', bd='5', command = sound_OFF)
sound_button2.place(x = 70, y = 350)

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

progress = Progressbar(win, orient = HORIZONTAL, length = 900, mode = 'determinate')

progress.pack(pady = 10)
progress.place(x = 70, y = 250)

progress['value'] = 0
win.update_idletasks()

def submit():
    import time
    try:
        global temp
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")

    increment = 100 / temp

    while temp > -1:

        if running:
            mins,secs = divmod(temp,60)
            hours=0
            if mins > 60:
                hours, mins = divmod(mins, 60)
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))

            win.update()
            sleep(1)

            if (temp == 0):
                if (sound):
                    pygame.mixer.music.play()
                messagebox.showinfo("Time is Up!", "Time's up ")
                progress['value'] = 0
            else:
                progress['value'] += increment
                win.update_idletasks()
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
btn2['state'] = Tkinter.NORMAL

win.mainloop()
win.destroy()