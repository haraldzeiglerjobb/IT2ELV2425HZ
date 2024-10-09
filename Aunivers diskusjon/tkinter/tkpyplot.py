"""
Fra ki.osloskolen.no

Ledetekst: 
i need a short program that will wrap pyplot into a tkinter window with buttons
"""

import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PlotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Matplotlib in Tkinter")

        # Create a figure
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create a button to update the plot
        self.update_button = ttk.Button(self.root, text="Update Plot", command=self.update_plot)
        self.update_button.pack(side=tk.BOTTOM)

        # Initial plot
        self.update_plot()

    def update_plot(self):
        # Clear the previous plot
        self.ax.clear()

        # Generate new data
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        # Plot the data
        self.ax.plot(x, y, label='sin(x)')
        self.ax.set_title("Sine Wave")
        self.ax.set_xlabel("X-axis")
        self.ax.set_ylabel("Y-axis")
        self.ax.legend()

        # Draw the new plot on the canvas
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = PlotApp(root)
    root.mainloop()