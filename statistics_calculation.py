from tkinter import *

def start_statistics_window(win, data):
    global pop
    pop = Toplevel(win)
    pop.title("Confirmation")
    pop.geometry("700x600")
    pop.config(bg="green3")
    label = Label(pop, text="Get statistics on one of the columns:", bg="green3", fg="white", font=('Aerial', 12))
    label.pack(pady=20)

    label2 = Label(pop, text="Press a button to learn more", bg="green3", fg="white", font=('Aerial', 12), height=6)
    label2.pack(pady=20)

    # Add a Frame
    frame = Frame(pop, bg="green3")
    frame.pack(pady=10)

    create_buttons(frame, data, label2)


def create_buttons(frame, data, label):
    for id, column in enumerate(data.columns):
        button1 = Button(frame, text=column, command=lambda column=column: print_statistics(column, data, label), bg="green")
        row = round(id / 5)
        column = (id % 5)* 2
        button1.grid(row=row, column=column)

def print_statistics(column, data, label):
    statistics = calculate_statistics(data, column)

    if(statistics["error"]):
        label.configure(text = "statistics for {column} cannot be calculated".format(column = column))
        return

    label.configure(text = """
        SELECTED DATA: {column}
        mean: {mean}
        median: {median}
        standard deviation: {deviation}
        IQR: {IQR}
        """.format(column = column, **statistics))


def calculate_statistics(data, column):
    try:
        values = {
            'mean': data[column].mean(numeric_only=True),
            'median': data[column].median(numeric_only=True),
            'deviation': data[column].std(numeric_only=True),
            'IQR': data[column].quantile(0.75) - data[column].quantile(0.25),
            'error': False,
        }
    except TypeError:
        values = { 'error': True }

    return values