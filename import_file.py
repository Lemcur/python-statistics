from tkinter import *

from tkinter import filedialog
import statistics_calculation

import pandas as pd

def browse_csv(win):
    filename = filedialog.askopenfilename(
        initialdir = "/", title = "Select a CSV",
        filetypes = (("CSV Files","*.csv"),))

    data = pd.read_csv(filename)

    statistics_calculation.start_statistics_window(win, data)


def browse_excel(win):
    filename = filedialog.askopenfilename(
        initialdir = "/", title = "Select an Excel spreadsheet",
        filetypes = (("Excel Files","*.xlsx"),))
    data = pd.read_excel(filename)

    statistics_calculation.start_statistics_window(win, data)

