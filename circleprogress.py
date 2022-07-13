import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
from tkinter import messagebox



class CircularProgressbar(object):
    def __init__(self, canvas, x0, y0, x1, y1, width=2, start_ang=0, full_extent=360.):
        self.custom_font = tkFont.Font(family="Helvetica", size=12, weight='bold')
        self.canvas = canvas
        self.x0, self.y0, self.x1, self.y1 = x0+width, y0+width, x1-width, y1-width
        self.tx, self.ty = (x1-x0)/2 +150 , (y1-y0) / 2
        self.width = width
        self.start_ang, self.full_extent = start_ang, full_extent
        # draw static bar outline
        w2 = width / 2
        self.oval_id1 = self.canvas.create_oval(self.x0-w2, self.y0-w2,
                                                self.x1+w2, self.y1+w2,fill="white")
        self.oval_id2 = self.canvas.create_oval(self.x0+w2, self.y0+w2,
                                                self.x1-w2, self.y1-w2,fill="light steel blue")
        self.running = False


    def start(self,interval,time):
        global timer
        self.interval = interval  # Msec delay between updates.
        self.increment = self.full_extent/time
        self.extent = 0
        self.arc_id = self.canvas.create_arc(self.x0, self.y0, self.x1, self.y1,
                                             start=self.start_ang, extent=self.extent,
                                             width=self.width, style='arc',outline="SeaGreen1")

        timer=time
        if time<=0:
            self.running=False

        self.label_id = self.canvas.create_text(self.tx, self.ty, text=timer,
                                                font=self.custom_font)
        self.running = True
        self.canvas.after(interval, self.step, self.increment)

    def step(self, delta):
        """Increment extent and update arc and label displaying how much completed."""
        if self.running:
            self.extent = (self.extent + delta) % 360
            self.canvas.itemconfigure(self.arc_id, extent=self.extent)



            percent = (self.extent) / self.full_extent
            time='{:.0f}'.format( timer-(timer*percent))
            print(time)
            if (self.extent)==0:
                time = str(0)
                self.canvas.itemconfigure(self.arc_id,extent=359.99)
                self.stop()

            self.canvas.itemconfigure(self.label_id, text=time)
        self.canvas.after(self.interval, self.step, delta)






    def toggle_pause(self):
        self.running = not self.running

    def stop(self):
        self.running = False



class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.canvas = tk.Canvas(self, width=500, height=500, bg='light steel blue')
        self.canvas.grid(row=0, column=0, columnspan=3)

        self.hour = tk.StringVar()
        self.minute = tk.StringVar()
        self.sec = tk.StringVar()
        self.hour.set("0")
        self.minute.set("0")
        self.sec.set("0")

        self.hour = tk.Entry(self, width=3, font=("Arial", 18, ""),
                             textvariable=self.hour)
        self.hour.place(x=65,y=300)
        self.minute = tk.Entry(self, width=3, font=("Arial", 18, ""),
                               textvariable=self.minute)
        self.minute.place(x=230,y=300)

        self.sec = tk.Entry(self, width=3, font=("Arial", 18, ""),
                            textvariable=self.sec)
        self.sec.place(x=400,y=300)

        self.progressbar = CircularProgressbar(self.canvas, 150, 0, 350, 200, 20)

        self.startButton = tk.Button(self, text='Start', bd='5', command=self.start)
        self.startButton.grid(row=0, column=0)
        self.pauseButton = tk.Button(self, text='Pause', command=self.pause)
        self.pauseButton.grid(row=0, column=1)
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid(row=0, column=2)



    def start(self):

        if self.progressbar.running==False:
            totaltemp = int(self.hour.get()) * 3600 + int(self.minute.get()) * 60 + int(self.sec.get())
            interval=1000
            self.progressbar.start(interval,totaltemp)
            if self.progressbar.running==True:
                tk.Button.grid_remove(self.startButton)



            self.mainloop()

    def pause(self):
        self.progressbar.toggle_pause()


    def stop(self):
        self.progressbar.stop()


if __name__ == '__main__':
    app = Application()
    app.master.title('Sample application')

    app.mainloop()
