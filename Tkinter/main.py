# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# download libraries required for filepathing
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Importing the tkinter library
import tkinter as tk
from tkinter import ttk
from tkinter import *

# Create an instance of tkinter frame as a splash window
splash_win = Tk()

#Set the title of the window
splash_win.title("Splash")

#Remove border of the splash Window and window buttons
#splash_win.overrideredirect(True)

splash_win.geometry("1024x600")  # set size of window
splash_win.configure(bg="#FFFFFF")

canvas = Canvas(
    splash_win,
    bg = "#FFFFFF",
    height = 600,
    width = 1024,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("uml_logo.png"))
image_1 = canvas.create_image(
    97.0,
    79.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("logo_bridgewell.png"))
image_2 = canvas.create_image(
    512.0,
    80.0,
    image=image_image_2
)

canvas.create_text(
    262.0,
    263.0,
    anchor="nw",
    text="Visual Timer",
    fill="#000000",
    font=("Inter Bold", 80 * -1)
)

canvas.create_text(
    880.0,
    480.0,
    anchor="nw",
    text="Group 22-004:\nSarvesh Handa\nKevin Logli\nFlorinda Martinez\nRussell Soto\nBrandon Zuniga",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)
splash_win.resizable(False, False)

# main window
def mainWin():
    splash_win.destroy()
    win = Tk()
    win.title("Enter Time")
    win.geometry("1024x600")






    # win_label = Label(win, text="Main Window", font=('Helvetica', 25), fg="red").pack(pady=20)
    canvas_main = Canvas(
        win,
        bg="#FFFFFF",
        height=600,
        width=1024,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas_main.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("img_enterTime.png"))
    image_1 = canvas_main.create_image(
        512.0,
        170.0,
        image=image_image_1
    )

    # time entry
    image_image_2 = PhotoImage(
        file=relative_to_assets("timeEntry.png"))


    # Enter Time frame

    enterTime = ttk.Frame(win)
    enterTime.pack(padx=10, pady=10, fill='x', expand=True)

    # email
    enterTime_label = ttk.Label(enterTime, text="Time:")
    enterTime_label.pack(fill='x', expand=False)
    timeEntered = tk.StringVar()
    email_entry = ttk.Entry(enterTime, textvariable=enterTime)
    email_entry.pack(fill='x', expand=False)
    email_entry.focus()

    image_2 = canvas_main.create_image(
        512.0,
        300.0,
        image=image_image_2
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=417.0,
        y=430.0,
        width=190.0,
        height=40.0
    )
    win.mainloop()
# Splash Window Timer

splash_win.after(3000, mainWin)


mainloop()

