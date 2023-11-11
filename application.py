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
import pdf_reader as pdfreader
import model as ai
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)
window = tk.Tk()


# def plot():
#     df = pd.read_csv('StudentsPerformance_with_headers.csv')
#     print(df["Father education "])
#     list_one = []
#     list_two = []
#     for i in range(145):
#         if df["Additional work"][i] == 1:
#             list_one.append(1)
#         else:
#             list_two.append(2)

#     data = {'1': len(list_one), '2': len(list_two)}

#     subplot.clear()

#     subplot.bar(data.keys(), data.values())
#     canvas.draw()


def previous_schedule():  # returns a tuple
    file = tkinter.filedialog.askopenfilenames(
        parent=window, title='Choose your schedules')


def previous_transcript():  # returns a tuple
    file = tkinter.filedialog.askopenfilenames(
        parent=window, title='Choose your transcripts')
    df = pdfreader.read_transcript(file[0])
    print(df)


window.geometry("1000x1000")

output_frame = tk.LabelFrame(window, text="Output", bg="#500000", fg="white")
output_frame.grid(row=0, column=0, rowspan=10, columnspan=7, sticky="nsew")


# fig = Figure(figsize=(5, 5), dpi=100)
# subplot = fig.add_subplot(111)
# canvas = FigureCanvasTkAgg(fig, master=output_frame)
# canvas_widget = canvas.get_tk_widget()
# canvas_widget.pack()


# display_plot = tk.Button(output_frame, text="Plot", command=plot)
# display_plot.pack(pady=(15, 15), padx=(0, 10))

input_frame = tk.LabelFrame(window, text="Input", bg="#D6D3C4", fg="black")
input_frame.grid(row=0, column=7, columnspan=2, rowspan=10,  sticky="nsew")

schedule_file = tk.Button(input_frame, text="Schedule",
                          command=previous_schedule)
schedule_file.pack(pady=(15, 15))

transcript_file = tk.Button(
    input_frame, text="Transcript", command=previous_transcript)
transcript_file.pack(pady=(15, 15))


input_one_label = tk.Label(input_frame, text='Work')
input_one_label.pack()

input_one_entry = tk.Entry(input_frame,)
input_one_entry.pack()

input_two_label = tk.Label(input_frame, text='Extracurricular')
input_two_label.pack()

input_two_entry = tk.Entry(input_frame,)
input_two_entry.pack()

input_three_label = tk.Label(input_frame, text='Partner')
input_three_label.pack()

input_three_entry = tk.Entry(input_frame,)
input_three_entry.pack()


input_four_label = tk.Label(input_frame, text='Studyhours')
input_four_label.pack()

input_four_entry = tk.Entry(input_frame,)
input_four_entry.pack()


input_five_label = tk.Label(input_frame, text='Reading Frequencey')
input_five_label.pack()

input_five_entry = tk.Entry(input_frame,)
input_five_entry.pack()

input_six_label = tk.Label(input_frame, text='Reading Frequencey Scientific')
input_six_label.pack()

input_six_entry = tk.Entry(input_frame,)
input_six_entry.pack()


input_seven_label = tk.Label(input_frame, text='Seminar')
input_seven_label.pack()

input_seven_entry = tk.Entry(input_frame,)
input_seven_entry.pack()

input_eight_label = tk.Label(input_frame, text='Outside Projects')
input_eight_label.pack()

input_eight_entry = tk.Entry(input_frame,)
input_eight_entry.pack()

input_nine_label = tk.Label(input_frame, text='Attendence')
input_nine_label.pack()

input_nine_entry = tk.Entry(input_frame,)
input_nine_entry.pack()

input_ten_label = tk.Label(input_frame, text='Midterm')
input_ten_label.pack()

input_ten_entry = tk.Entry(input_frame,)
input_ten_entry.pack()

input_eleven_label = tk.Label(input_frame, text='Amount of Notes')
input_eleven_label.pack()

input_eleven_entry = tk.Entry(input_frame,)
input_eleven_entry.pack()

input_twelve_label = tk.Label(input_frame, text='Amount of listening')
input_twelve_label.pack()

input_twelve_entry = tk.Entry(input_frame,)
input_twelve_entry.pack()

input_thirteen_label = tk.Label(input_frame, text='Your Previous GPA')
input_thirteen_label.pack()

input_thirteen_entry = tk.Entry(input_frame,)
input_thirteen_entry.pack()


def submit():
    i1 = input_one_entry.get()
    i2 = input_two_entry.get()
    i3 = input_three_entry.get()
    i4 = input_four_entry.get()
    i5 = input_five_entry.get()
    i6 = input_six_entry.get()
    i7 = input_seven_entry.get()
    i8 = input_eight_entry.get()
    i9 = input_nine_entry.get()
    i10 = input_ten_entry.get()
    i11 = input_eleven_entry.get()
    i12 = input_twelve_entry.get()
    i13 = input_thirteen_entry.get()
    convert_grade = {7: "A", 6: "B+", 5: "B",
                     4: "C+", 3: "C", 2: "D+", 1: 'D', 0: "F"}
    print(convert_grade[ai.predict_final(i1, i2, i3,
          i4, i5, i6, i7, i8, i9, i10, i11, i12, i13)])


submit = tk.Button(
    input_frame, text="Submit", command=submit)
submit.pack(pady=(15, 15))

for i in range(10):
    window.grid_rowconfigure(i, weight=1)
for i in range(8):
    window.grid_columnconfigure(i, weight=1)


window.mainloop()
