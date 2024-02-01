import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def plot_graph():
    try:
        expression = entry.get()
        x = np.linspace(-10, 10, 400)
        y = eval(expression)
        ax.clear()
        ax.plot(x, y, label=expression)
        ax.legend()
        canvas.draw()
    except Exception as e:
        result_label.config(text="Error")

# Create the main window
window = tk.Tk()
window.title("Graphing Calculator")

# Entry widget for mathematical expression
entry = ttk.Entry(window, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Button to plot the graph
plot_button = ttk.Button(window, text="Plot", command=plot_graph)
plot_button.grid(row=0, column=3, padx=10, pady=10)

# Result label
result_label = ttk.Label(window, text="")
result_label.grid(row=1, column=0, columnspan=4)

# Matplotlib Figure and Canvas for plotting
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=window)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=2, column=0, columnspan=4)

# Run the Tkinter event loop
window.mainloop()
