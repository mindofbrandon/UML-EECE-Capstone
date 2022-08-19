#!usr/bin/python

# UML EECE Visual Timer Capstone Group 22-004 (Summer)
# Authors: Russell Soto, Sarvesh Handa, Brandon Zuniga

from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
from tkinter import messagebox
from pathlib import Path
import pygame
import os
from pygame.locals import *
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

pygame.mixer.init()
# pygame.mixer.music.load('/home/admin/Downloads/UML-EECE-Capstone-guifix/alarm.mp3')

stop_sound = False # states to manage the sound
sound = False #
quit_delay = 0
cont = None

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class CircularProgressbar(object):
    def __init__(self, canvas, x0, y0, x1, y1, width=2, start_ang=0, full_extent=360.):
        self.custom_font = tkFont.Font(family="Helvetica", size=30, weight='bold')
        self.canvas = canvas

        self.x0, self.y0, self.x1, self.y1 = x0 + width, y0 + width, x1 - width, y1 - width  # Coordinates for the circles
        self.tx, self.ty = (x1 - x0) / 2 + 150, (y1 - y0) / 2  # Coordinates for Text in middle of circles (Timer)
        self.width = width
        self.start_ang, self.full_extent = start_ang, full_extent  # Start angle =0 and full extent = 360 to complete a full circle
        self.message=False
        # draw static bar outline
        w2 = width / 2
        self.oval_id1 = self.canvas.create_oval(self.x0 - w2, self.y0 - w2,
                                                self.x1 + w2, self.y1 + w2, fill="red")  # Big cicrle ("outside"
        self.oval_id2 = self.canvas.create_oval(self.x0 + w2, self.y0 + w2,
                                                self.x1 - w2, self.y1 - w2,
                                                fill="light steel blue")  # small Circle, inside
        self.running = False  ## Timer is not yet running

    def start(self, interval, time):  #
        global timer  # Set timer = time and make it global so step function can access it
        self.interval = interval  # Msec delay between updates. 1000 Msec =1second
        self.increment = self.full_extent / time  # Create increments to progress the arc by dividing 360 degrees by the time entered.
        self.extent = 0  # Circe starts at 0
        self.arc_id = self.canvas.create_arc(self.x0, self.y0, self.x1, self.y1,
                                             start=self.start_ang, extent=self.extent,
                                             width=self.width, style='arc',
                                             outline="SeaGreen1")  # Create arc to fill in progressbar
        timer = time

        # 262, 50, 762, 550
        self.label_id = self.canvas.create_text(512.0, 300.0, text=timer,
                                                font=self.custom_font) # Create the timer text
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
                VisualTimer.button_icon_shutdown["state"] = ACTIVE
                VisualTimer.button_start["state"] = ACTIVE
                
                self.reset()
                
            self.canvas.itemconfigure(self.label_id, text=time)  # update time of
        self.canvas.after(self.interval, self.step, delta)



    def toggle_pause(self):  # toggle pause by switching state to opposite state. this allows the same button to pause and unpause
        
        self.running = not self.running

    def stop(self):
        self.running = False
        # stops the progress bar from running
        
    def reset(self):
        self.running = False
        self.extent = 0
        VisualTimer.createWidgets() # reset the canvas
    
    def stop_mp3(self): # Stop the alarm sound
        global stop_sound
        stop_sound = True

    def play(self): #Play the alarm
        while (True):
            pygame.mixer.music.play()
            if stop_sound:
                break


class Timer(tk.Tk):  # This class creates and manages all the widgets such as button, entry boxes, and the progressbar

    cont = None
    def __init__(self, master=None):
        tk.Tk.__init__(self, master)
        self.createWidgets()

    def createWidgets(self):
        
        global quit_delay
        quit_delay = 0
        
        self.canvas = Canvas(
            self,
            bg="light steel blue",
            height=600,
            width=1024,
        )

        # create start button
        self.canvas.place(x=0, y=0)
        self.button_image_start = PhotoImage(
            file=relative_to_assets("start.png"))
        self.button_start = Button(
            image=self.button_image_start,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.start(),
            relief="flat"
        )
        self.button_start.place(
            x=17.0,
            y=109.0,
            width=190.0,
            height=40.0
        )

        # create stop button
        self.button_image_stop = PhotoImage(
            file=relative_to_assets("stop.png"))
        button_stop = Button(
            image=self.button_image_stop,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.progressbar.reset(),
            relief="flat"
        )
        button_stop.place(
            x=17.0,
            y=178.0,
            width=190.0,
            height=40.0
        )

        # create pause button
        self.button_image_pause = PhotoImage(
            file=relative_to_assets("pause.png"))
        button_pause = Button(
            image=self.button_image_pause,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.pause(),
            relief="flat"
        )
        button_pause.place(
            x=17.0,
            y=247.0,
            width=190.0,
            height=40.0
        )

        # create sound on button
        self.button_image_sound_on = PhotoImage(
            file=relative_to_assets("sound_on.png"))
        button_sound_on = Button(
            image=self.button_image_sound_on,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.sound_ON(),
            relief="flat"
        )
        button_sound_on.place(
            x=818.0,
            y=109.0,
            width=190.0,
            height=40.0
        )

        # sound off button
        self.button_image_sound_off = PhotoImage(
            file=relative_to_assets("sound_off.png"))
        button_sound_off = Button(
            image=self.button_image_sound_off,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.sound_OFF(),
            relief="flat"
        )
        button_sound_off.place(
            x=818.0,
            y=178.0,
            width=190.0,
            height=40.0
        )


        # create speaker icon
        self.image_image_icon_speaker = PhotoImage(
            file=relative_to_assets("icon_speaker.png"))
        image_icon_speaker = self.canvas.create_image(
            912.0,
            50.0,
            image=self.image_image_icon_speaker
        )

        # mins increment button
        self.button_image_increment = PhotoImage(
            file=relative_to_assets("increment.png"))
        self.button_increment = Button(
            image=self.button_image_increment,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.button_increment.bind('<Button-1>', lambda event: self.minsup())
        self.button_increment.bind('<ButtonRelease>', lambda event: self.stop_press())
        self.button_increment.place(
            x=888.0,
            y=264.0,
            width=50.0,
            height=47.0
        )

        # minutes entry
        self.image_minutes = PhotoImage(
            file=relative_to_assets("minutes.png"))
        image_img_minutes = self.canvas.create_image(
            913.0,
            341.0,
            image=self.image_minutes
        )

        # mins decrement button
        self.button_image_decrement = PhotoImage(
            file=relative_to_assets("decrement.png"))
        self.button_decrement = Button(
            image=self.button_image_decrement,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.button_decrement.bind('<Button-1>', lambda event: self.minsdown())
        self.button_decrement.bind('<ButtonRelease>', lambda event: self.stop_press())
        self.button_decrement.place(
            x=888.0,
            y=366.0,
            width=50.0,
            height=47.0
        )

        # secs increment button
        self.button_image_increment_sec = PhotoImage(
            file=relative_to_assets("increment.png"))
        self.button_increment_sec = Button(
            image=self.button_image_increment_sec,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.button_increment_sec.bind('<Button-1>', lambda event: self.secsup())
        self.button_increment_sec.bind('<ButtonRelease>', lambda event: self.stop_press())
        self.button_increment_sec.place(
            x=888.0,
            y=430.0,
            width=50.0,
            height=47.0
        )

        # seconds entry
        self.image_seconds = PhotoImage(
            file=relative_to_assets("seconds.png"))
        image_img_sec = self.canvas.create_image(
            913.0,
            507.0,
            image=self.image_seconds
        )

        # secs decrement button
        self.button_image_decrement_sec = PhotoImage(
            file=relative_to_assets("decrement.png"))
        self.button_decrement_sec = Button(
            image=self.button_image_decrement_sec,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.button_decrement_sec.bind('<Button-1>', lambda event: self.secsdown())
        self.button_decrement_sec.bind('<ButtonRelease>', lambda event: self.stop_press())
        self.button_decrement_sec.place(
            x=888.0,
            y=532.0,
            width=50.0,
            height=47.0
        )

        # turn off pi 
        self.button_image_icon_shutdown = PhotoImage(
            file=relative_to_assets("icon_shutdown.png"))
        self.button_icon_shutdown = Button(
            image=self.button_image_icon_shutdown,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.shutdown(),
            relief="flat",
            bg="light steel blue"
        )
        self.button_icon_shutdown.place(
            x=17.0,
            y=500.0,
            width=90.0,
            height=100.0
        )

        self.hour = 0  # initialize variables for time that will be inputted throught the entry boxes
        self.minute = 0
        self.sec = 0

        self.progressbar = CircularProgressbar(self.canvas, 262, 50, 762, 550,20)  # this will create an empty progress bar that will not start until start is pressed.
        self.soundlabel = self.canvas.create_text(920.0, 162.0, text="Sound is OFF",font='Helevetica 18 bold',fill='red')
        self.mintime = self.canvas.create_text(845.0, 340.0, text=self.minute, font='Helevetica 26 bold', fill='red')
        self.sectime = self.canvas.create_text(845.0, 508.0, text=self.sec, font='Helevetica 26 bold', fill='red')


    def shutdown(self): # shutdown the pi safely after 3 consecutive button presses
        # if shutdown icon button is pressed, the quit counter will reset to 0
        
        global quit_delay
        quit_delay += 1

        if (quit_delay > 2):
            print("quit")
            os.system("sudo shutdown -h now")

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
        global cont
        self.minute= self.minute+1
        self.canvas.delete(self.mintime)
        self.mintime = self.canvas.create_text(845.0, 340.0, text=self.minute, font='Helevetica 26 bold', fill='green')
        cont = self.after(300, self.minsup)
    
    def minsdown(self):
        global cont
        if self.minute>0:
            self.minute= self.minute-1
            self.canvas.delete(self.mintime)
            self.mintime = self.canvas.create_text(845.0, 340.0, text=self.minute, font='Helevetica 26 bold', fill='green')
            cont = self.after(300, self.minsdown)

    def secsup(self):
        global cont
        self.sec= self.sec+1
        self.canvas.delete(self.sectime)
        self.sectime = self.canvas.create_text(845.0, 508.0, text=self.sec, font='Helevetica 26 bold', fill='green')
        cont = self.after(300, self.secsup)

    def secsdown(self):
        global cont
        if self.sec>0:
            self.sec= self.sec-1
            self.canvas.delete(self.sectime)
            self.sectime = self.canvas.create_text(845.0, 508.0, text=self.sec, font='Helevetica 26 bold', fill='green')
            cont = self.after(300, self.secsdown)
    
    def stop_press(self):
        global cont
        self.after_cancel(cont)

    def start(self):  # Start button pressed, so start the countdown

        if self.progressbar.running == False:  # This checks that the timer is not running which is should not be until time is inputted and start is pressed
            totaltime = int(self.hour) * 3600 + int(self.minute) * 60 + int(
                self.sec)  # Get the total time which is going to be sent to the progressbar.start function
            interval = 1000  # 3 interval is 1 second, or 1000 Msec,
            self.progressbar.start(interval,
                                   totaltime)  # this will be sent to progressbar/start which will decrement the total time by 1 every  second.
            
            if self.progressbar.running == True:  # once the start button is pressed, disable it until?...
                
                # disable the start and shutdown button if timer is running
                self.button_icon_shutdown["state"] = DISABLED
                self.button_start["state"] = DISABLED
                
            self.mainloop()

    def sound_ON(self): #Button to turn sound on
        global sound
        sound = True
        self.canvas.delete(self.soundlabel)
        self.soundlabel = self.canvas.create_text(920.0, 162.0, text="Sound is ON", font='Helevetica 18 bold', fill='green')

    def sound_OFF(self):# Button to turn off sound
        global sound
        sound = False
        self.canvas.delete(self.soundlabel)
        self.soundlabel = self.canvas.create_text(920.0, 162.0, text="Sound is OFF", font='Helevetica 18 bold', fill='red')

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
    VisualTimer.title('Countdown!')
    VisualTimer.geometry("1024x600")

    # Remove border of the splash Window and window buttons
    VisualTimer.overrideredirect(True)

    # do not allow window to be resizeable
    VisualTimer.resizable(False, False)
    VisualTimer.mainloop()