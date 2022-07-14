import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
from tkinter import messagebox



class CircularProgressbar(object):
    def __init__(self, canvas, x0, y0, x1, y1, width=2, start_ang=0, full_extent=360.):
        self.custom_font = tkFont.Font(family="Helvetica", size=12, weight='bold')
        self.canvas = canvas
        self.x0, self.y0, self.x1, self.y1 = x0+width, y0+width, x1-width, y1-width # Coordinates for the circles 
        self.tx, self.ty = (x1-x0)/2 +150 , (y1-y0) / 2 # Coordinates for Text in middle of circles (Timer)
        self.width = width
        self.start_ang, self.full_extent = start_ang, full_extent # Start angle =0 and full extent = 360 to complete a full circle 
        
        # draw static bar outline
        w2 = width / 2
        self.oval_id1 = self.canvas.create_oval(self.x0-w2, self.y0-w2,
                                                self.x1+w2, self.y1+w2,fill="white") # Big cicrle ("outside"
        self.oval_id2 = self.canvas.create_oval(self.x0+w2, self.y0+w2,
                                                self.x1-w2, self.y1-w2,fill="light steel blue")# small Circle, inside
        self.running = False ## Timer is not yet running


    def start(self,interval,time): #
        global timer # Set timer = time and make it global so step function can access it
        self.interval = interval  # Msec delay between updates. 1000 Msec =1second
        self.increment = self.full_extent/time # Create increments to progress the arc by dividing 360 degrees by the time entered.
        self.extent = 0 # Circe starts at 0
        self.arc_id = self.canvas.create_arc(self.x0, self.y0, self.x1, self.y1,
                                             start=self.start_ang, extent=self.extent,
                                             width=self.width, style='arc',outline="SeaGreen1") # Create arc to fill in progressbar

        timer=time


        self.label_id = self.canvas.create_text(self.tx, self.ty, text=timer,
                                                font=self.custom_font) # Create the timer text
        self.running = True # turn on the circle progreess bar
        self.canvas.after(interval, self.step, self.increment) # after loop to update canvas after step[ing in progress bar

    def step(self, delta):
        #Increment extent and update arc and label displaying how much completed
        if self.running: # only step is progress bar is running

            self.extent = (self.extent + delta) % 360 #Delta is increment
            self.canvas.itemconfigure(self.arc_id, extent=self.extent)



            percent = (self.extent) / self.full_extent # get position of arc and divide it by 360 to get a percentage of the time passed
            time='{:.0f}'.format( timer-(timer*percent)) # take the percentage and multiply by globl var timer to calculate the present time.

            if (self.extent)==0: # if arc reaches the starting point ( 0 which is also the end point 360 )
                time = str(0) # set time to 0 manually after the circle is complete
                self.canvas.itemconfigure(self.arc_id,extent=359.99) # it fills up the bar completely when timer is done, 359.99 becuasse 360 us essentially
                self.stop() # stop the progress bar from perputually running

            self.canvas.itemconfigure(self.label_id, text=time) # update time of
        self.canvas.after(self.interval, self.step, delta)


    def toggle_pause(self): # toggle pause by switching state to opposite state. this allows the same button to pause and unpause
        self.running = not self.running

    def stop(self):
        self.running = False
        #stops the progress bar from running


class Timer(tk.Frame): # This class creates and manages all the widgets such as button, entry boxes, and the progressbar

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.canvas = tk.Canvas(self, width=500, height=500, bg='light steel blue')
        self.canvas.grid(row=0, column=0, columnspan=3)

        self.hour = tk.StringVar() # initialize variables for time that will be inputted throught the entry boxes
        self.minute = tk.StringVar()
        self.sec = tk.StringVar()
        self.hour.set("0")
        self.minute.set("0")
        self.sec.set("0")

        self.hour = tk.Entry(self, width=3, font=("Arial", 18, ""), # time entry boxes
                             textvariable=self.hour)
        self.hour.place(x=65,y=300) ## Used .place instead of grid because grid would allow boxes only at the very bottom of page.
        self.minute = tk.Entry(self, width=3, font=("Arial", 18, ""),
                               textvariable=self.minute)
        self.minute.place(x=230,y=300)

        self.sec = tk.Entry(self, width=3, font=("Arial", 18, ""),
                            textvariable=self.sec)
        self.sec.place(x=400,y=300)

        self.progressbar = CircularProgressbar(self.canvas, 150, 0, 350, 200, 20) # this will create an empty progress bar that will not start until start is pressed.

        self.startButton = tk.Button(self, text='Start', bd='5', command=self.start) # Create start, pause, and quit button.
        self.startButton.grid(row=0, column=0)
        self.pauseButton = tk.Button(self, text='Pause', command=self.pause)
        self.pauseButton.grid(row=0, column=1)
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid(row=0, column=2)



    def start(self):    # Start button pressed, so start the countdown

        if self.progressbar.running==False: # This checks that the timer is not running which is should not be until time is inputted and start is pressed
            totaltime = int(self.hour.get()) * 3600 + int(self.minute.get()) * 60 + int(self.sec.get()) # Get the total time which is going to be sent to the progressbar.start function
            interval=1000 #3 interval is 1 second, or 1000 Msec,
            self.progressbar.start(interval,totaltime) #this will be sent to progressbar/start which will decrement the total time by 1 every  second.
            if self.progressbar.running==True: # once the start button is pressed, disable it until?...
                tk.Button.grid_remove(self.startButton)



            self.mainloop()

    def pause(self): # toggle pause if pause button pressed
        self.progressbar.toggle_pause()


    def stop(self): # Stop function if stop is pressed.
        self.progressbar.stop()


if __name__ == '__main__':
    VisualTimer = Timer()
    VisualTimer.master.title('Countdown!')

    VisualTimer.mainloop()
