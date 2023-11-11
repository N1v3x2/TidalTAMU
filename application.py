import tkinter as tk
from tkinter import ttk
import tkinter.filedialog
# import dataplots as dp
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)
window = tk.Tk()


def plot():
    df = pd.read_csv('StudentsPerformance_with_headers.csv')
    print(df["Father education "])
    list_one = []
    list_two = []
    for i in range(145):
        if df["Additional work"][i] == 1:
            list_one.append(1)
        else:
            list_two.append(2)

    data = {'1': len(list_one), '2': len(list_two)}

    subplot.clear()

    subplot.bar(data.keys(), data.values())
    canvas.draw()


def previous_schedule():  # returns a tuple
    file = tkinter.filedialog.askopenfilenames(
        parent=window, title='Choose your schedules')
    print(file)


def previous_transcript():  # returns a tuple
    file = tkinter.filedialog.askopenfilenames(
        parent=window, title='Choose your transcripts')
    print(file)


window.geometry("1000x700")

output_frame = tk.LabelFrame(window, text="Output", bg="#500000", fg="white")
output_frame.grid(row=0, column=0, rowspan=10, columnspan=7, sticky="nsew")


fig = Figure(figsize=(5, 5), dpi=100)
subplot = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=output_frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()


display_plot = tk.Button(output_frame, text="Plot", command=plot)
display_plot.pack(pady=(15, 15), padx=(0, 10))

input_frame = tk.LabelFrame(window, text="Input", bg="#D6D3C4", fg="black")
input_frame.grid(row=0, column=7, columnspan=2, rowspan=10,  sticky="nsew")

schedule_file = tk.Button(input_frame, text="Schedule",
                          command=previous_schedule)
schedule_file.pack(pady=(15, 15))

transcript_file = tk.Button(
    input_frame, text="Transcript", command=previous_transcript)
transcript_file.pack(pady=(15, 15))


input_one_label = tk.Label(input_frame, text='Text Box')
input_one_label.pack()

input_one_entry = tk.Entry(input_frame,)
input_one_entry.pack()


for i in range(10):
    window.grid_rowconfigure(i, weight=1)
for i in range(8):
    window.grid_columnconfigure(i, weight=1)


window.mainloop()
