from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
from tkinter import messagebox
import pygame
from pygame.locals import *
from playsound import playsound

pygame.mixer.init()
pygame.mixer.music.load('alarm.mp3')

stop_sound = False
sound = False

class CircularProgressbar(object):
    def __init__(self, canvas, x0, y0, x1, y1, width=2, start_ang=0, full_extent=360.):
        self.custom_font = tkFont.Font(family="Helvetica", size=18, weight='bold')
        self.canvas = canvas
        self.x0, self.y0, self.x1, self.y1 = x0 + width, y0 + width, x1 - width, y1 - width  # Coordinates for the circles
        self.tx, self.ty = (x1 - x0) / 2 + 150, (y1 - y0) / 2  # Coordinates for Text in middle of circles (Timer)
        self.width = width
        self.start_ang, self.full_extent = start_ang, full_extent  # Start angle =0 and full extent = 360 to complete a full circle
        self.message=False
        # draw static bar outline
        w2 = width / 2
        self.oval_id1 = self.canvas.create_oval(self.x0 - w2, self.y0 - w2,
                                                self.x1 + w2, self.y1 + w2, fill="white")  # Big cicrle ("outside"
        self.oval_id2 = self.canvas.create_oval(self.x0 + w2, self.y0 + w2,
                                                self.x1 - w2, self.y1 - w2,
                                                fill="light steel blue")  # small Circle, inside
        self.label_id = self.canvas.create_text(self.tx, self.ty, text = 0,
                                                font=self.custom_font) # Create the timer text
        self.arc_id = self.canvas.create_arc(self.x0, self.y0, self.x1, self.y1,
                                             start=self.start_ang, extent=0,
                                             width=self.width, style='arc',
                                             outline="SeaGreen1")  # Create arc to fill in progressbar
        self.running = False  ## Timer is not yet running

    def start(self, interval, time):  
        global timer  # Set timer = time and make it global so step function can access it
        self.interval = interval  # Msec delay between updates. 1000 Msec =1second
        self.increment = self.full_extent / time  # Create increments to progress the arc by dividing 360 degrees by the time entered.
        self.extent = 0  # Circe starts at 0

        timer = time
        self.running = True  # turn on the circle progreess bar
        self.canvas.after(interval, self.step,
                          self.increment)  # after loop to update canvas after step[ing in progress bar

    def step(self, delta):
        # Increment extent and update arc and label displaying how much completed
        if self.running:  # only step is progress bar is running

            self.extent = (self.extent + delta) % 360  # Delta is increment
            self.canvas.itemconfigure(self.arc_id, extent=self.extent)

            percent = (
                          self.extent) / self.full_extent  # get position of arc and divide it by 360 to get a percentage of the time passed
            time = '{:.0f}'.format(timer - (
                        timer * percent))  # take the percentage and multiply by globl var timer to calculate the present time.

            if (self.extent) == 0:  # if arc reaches the starting point ( 0 which is also the end point 360 )
                time = str(0)  # set time to 0 manually after the circle is complete
                self.canvas.itemconfigure(self.arc_id,
                                          extent=359.99)  # it fills up the bar completely when timer is done, 359.99 becuasse 360 us essentially
                self.stop()  # stop the progress bar from perputually running

                if sound: ## If sound is on, play alarm if 0
                    pygame.mixer.music.play()
                    self.message=True
                VisualTimer.startButton["state"] = ACTIVE  
                self.reset()

            self.canvas.itemconfigure(self.label_id, text=time)  # update time of
    
        self.canvas.after(self.interval, self.step, delta)

    def toggle_pause(
            self):  # toggle pause by switching state to opposite state. this allows the same button to pause and unpause
        self.running = not self.running

    def stop(self):
        self.running = False
        # stops the progress bar from running

    def reset(self):
        self.extent = 0

    def stop_mp3(self): # Stop the alarm
        global stop_sound
        stop_sound = True

    def play(self): #Play the alarm
        while (True):
            playsound('alarm.mp3')
            if stop_sound:
                break

class Timer(tk.Frame):  # This class creates and manages all the widgets such as button, entry boxes, and the progressbar

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.canvas = tk.Canvas(self, width=500, height=500, bg='light steel blue')
        self.canvas.grid(row=0, column=0, columnspan=3)

        self.hour = 0  # initialize variables for time that will be inputted throught the entry boxes

        self.minute = 0
        self.sec = 0
        self.hrup = tk.Button(self, text='Hour up', bd='5',
                                     command=self.hourup)
        self.hrup.place(x=40,y=300)  ## Used .place instead of grid because grid would allow boxes only at the very bottom of page.
        self.hrdown = tk.Button(self, text='Hour down', bd='5',
                              command=self.hourdown)
        self.hrdown.place(x=40,y=370)
        self.minup = tk.Button(self, text='Mins up', bd='5',
                             command=self.minsup)
        self.minup.place(x=240,y=300)
        self.mindown = tk.Button(self, text='Mins down', bd='5',
                                command=self.minsdown)
        self.mindown.place(x=240, y=370)
        self.secup = tk.Button(self, text='Sec up', bd='5',
                               command=self.secsup)
        self.secup.place(x=440,y=300)
        self.secdown = tk.Button(self, text='Secs up', bd='5',
                                 command=self.secsdown)
        self.secdown.place(x=440, y=370)

        self.progressbar = CircularProgressbar(self.canvas, 150, 0, 350, 200,20)  # this will create an empty progress bar that will not start until start is pressed.
        self.soundlabel = self.canvas.create_text(250,450,text="Sound is OFF",font='Helevetica 15 bold',fill='red')


        self.hourtime = self.canvas.create_text(70, 340, text=self.hour, font='Helevetica 15 bold', fill='red')
        self.mintime = self.canvas.create_text(270, 340, text=self.minute, font='Helevetica 15 bold', fill='red')
        self.sectime = self.canvas.create_text(470, 340, text=self.sec, font='Helevetica 15 bold', fill='red')

        self.startButton = tk.Button(self, text='Start', bd='5',
                                     command=self.start)  # Create start, pause, and quit button.
        self.startButton.grid(row=0, column=0)
        self.pauseButton = tk.Button(self, text='Pause/Resume', command=self.pause)
        self.pauseButton.grid(row=0, column=1)
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid(row=0, column=2)

        self.soundOnButton = tk.Button(self, text='Sound ON', bd='5',
                                     command=self.sound_ON)  # Create start, pause, and quit button.
        self.soundOnButton.place(x=150,y=400)
        self.soundOffButton = tk.Button(self, text='Sound OFF', command=self.sound_OFF)
        self.soundOffButton.place(x=300,y=400)

    def hourup(self):

        self.hour= self.hour+1
        self.canvas.delete(self.hourtime)
        self.hourtime = self.canvas.create_text(70, 340, text=self.hour, font='Helevetica 15 bold', fill='green')

    def hourdown(self):
        if self.hour>0:
            self.hour= self.hour-1
            self.canvas.delete(self.hourtime)
            self.hourtime = self.canvas.create_text(70, 340, text=self.hour, font='Helevetica 15 bold', fill='green')
    def minsup(self):

        self.minute= self.minute+1
        self.canvas.delete(self.mintime)
        self.mintime = self.canvas.create_text(270, 340, text=self.minute, font='Helevetica 15 bold', fill='green')
    def minsdown(self):
        if self.minute>0:
            self.minute= self.minute-1
            self.canvas.delete(self.mintime)
            self.mintime = self.canvas.create_text(270, 340, text=self.minute, font='Helevetica 15 bold', fill='green')

    def secsup(self):

        self.sec= self.sec+1
        self.canvas.delete(self.sectime)
        self.sectime = self.canvas.create_text(470, 340, text=self.sec, font='Helevetica 15 bold', fill='green')
    def secsdown(self):
        if self.sec>0:
            self.sec= self.sec-1
            self.canvas.delete(self.sectime)
            self.sectime = self.canvas.create_text(470, 340, text=self.sec, font='Helevetica 15 bold', fill='green')

    def start(self):  # Start button pressed, so start the countdown

        if self.progressbar.running == False:  # This checks that the timer is not running which is should not be until time is inputted and start is pressed
            totaltime = int(self.hour) * 3600 + int(self.minute) * 60 + int(
                self.sec)  # Get the total time which is going to be sent to the progressbar.start function
            interval = 1000  # 3 interval is 1 second, or 1000 Msec,
            self.progressbar.start(interval,
                                   totaltime)  # this will be sent to progressbar/start which will decrement the total time by 1 every  second.
            
            if self.progressbar.running == True:  # once the start button is pressed, disable it until?...
                self.startButton["state"] = DISABLED

            self.mainloop()

    def sound_ON(self): #Button to turn sound on
        global sound
        sound = True
        self.canvas.delete(self.soundlabel)
        self.soundlabel = self.canvas.create_text(250, 450, text="Sound is ON", font='Helevetica 15 bold', fill='green')

    def sound_OFF(self):# Button to turn off sound
        global sound
        sound = False
        self.canvas.delete(self.soundlabel)
        self.soundlabel = self.canvas.create_text(250, 450, text="Sound is OFF", font='Helevetica 15 bold', fill='red')

    def pause(self):  # toggle pause if pause button pressed
        self.progressbar.toggle_pause()

    def stop(self):  # Stop function if stop is pressed.
        self.progressbar.stop()

    def alarmoff(self):
        self.progressbar.stop_mp3()

    def play(self):
        self.progressbar.play()

if __name__ == '__main__':
    VisualTimer = Timer()
    VisualTimer.master.title('Countdown!')

    VisualTimer.mainloop()
