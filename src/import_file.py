from tkinter import *

from tkinter import filedialog
import statistics_calculation

import pandas as pd

def browse_csv(win):
    filename = filedialog.askopenfilename(
        initialdir = "/", title = "Wybierz plik CSV",
        filetypes = (("Pliki CSV","*.csv"),))

    data = pd.read_csv(filename)

    statistics_calculation.start_statistics_window(win, data)


def browse_excel(win):
    filename = filedialog.askopenfilename(
        initialdir = "/", title = "Wybierz plik Excel",
        filetypes = (("Pliki Excel","*.xlsx"),))
    data = pd.read_excel(filename)

    statistics_calculation.start_statistics_window(win, data)

