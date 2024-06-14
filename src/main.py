#-*- coding: ibm852 -*-
# inspiration:
# https://www.tutorialspoint.com/what-is-the-correct-way-to-implement-a-custom-popup-tkinter-dialog-box

"""
  Statictics application using pandas

  Rafał Klimek and Igor Karwacik
"""

# Import required libraries
from tkinter import *
from tkinter import ttk
from tkinter import constants, messagebox
import import_file as import_file
import statistics_calculation as statistics_calculation

# from import_file import browse_csv, browse_excel
# from statistics_calculation import browse_csv, browse_excel

# Create an instance of tkinter frame
win = Tk()
# Set the window size
win.geometry("300x250")

def About():
  messagebox.showinfo('statystyki', 'Aplikacja do obliczania statystyk z użyciem pandas')

def Quit(event):
  quit()

button_opt = {'fill': constants.BOTH, 'padx': 15, 'pady': 5}

# Create a Label widget
Mlabel = Label(win, text="", font=('Arial', 14))
Mlabel.pack(pady=40)

# Create commands buttons
ttk.Button(win, text="Szukaj CSV", command=lambda: import_file.browse_csv(win)).pack(**button_opt)
ttk.Button(win, text="Szukaj Excel", command=lambda: import_file.browse_excel(win)).pack(**button_opt)
ttk.Button(win, text="[ O programie: ]", command=About).pack(**button_opt)

ttk.Button(win, text="[    Zamknij   ]", command=quit).pack(**button_opt)
win.bind("<KeyPress-Escape>", Quit)

# start interface:
win.mainloop()
