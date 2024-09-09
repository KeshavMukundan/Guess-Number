import tkinter as tk

import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.6
    output_string.set(km_output)    

window = ttk.Window(themename = "darkly")
window.title("Demo")
window.geometry("350x150")

title_label = ttk.Label(master = window, text = "Miles to Kilometer", font = ("Lustra Text Medium",18))
title_label.pack()

input_frame = ttk.Frame(master = window)

entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = "convert", command = convert)

entry.pack(side = "left", padx = 10)
button.pack(side = "left")
input_frame.pack(pady = 10)

output_string = tk.StringVar()
output = ttk.Label(master = window, font = ("Lustra Text Medium", 18), textvariable = output_string)
output.pack(pady = 5)

window.mainloop()