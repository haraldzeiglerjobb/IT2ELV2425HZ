"""
Give me a python program that produces a matplotlib graph within a tkinter window with buttons and dropdown menus
"""
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Matplotlib in Tkinter")
        
        # Create a frame for the Matplotlib figure
        self.frame = ttk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # Create a figure for plotting
        self.figure, self.ax = plt.subplots()
        
        # Create buttons and dropdown menu
        self.create_widgets()
        
        # Draw the initial graph
        self.plot_graph()

    def create_widgets(self):
        # Dropdown menu for selecting function
        self.function_var = tk.StringVar(value='Sine')
        self.function_menu = ttk.Combobox(self.frame, textvariable=self.function_var, 
                                           values=['Sine', 'Cosine', 'Tangent'])
        self.function_menu.pack(side=tk.TOP, padx=10, pady=10)

        # Button to update the graph
        self.plot_button = ttk.Button(self.frame, text="Plot", command=self.plot_graph)
        self.plot_button.pack(side=tk.TOP, padx=10, pady=10)

        # Embed the Matplotlib figure into the Tkinter window
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame)
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def plot_graph(self):
        # Clear the previous graph
        self.ax.clear()

        # Generate x values
        x = np.linspace(0, 10, 100)

        # Determine the function to plot based on dropdown selection
        func = self.function_var.get()
        if func == 'Sine':
            y = np.sin(x)
        elif func == 'Cosine':
            y = np.cos(x)
        elif func == 'Tangent':
            y = np.tan(x)

        # Plot the graph
        self.ax.plot(x, y, label=func)
        self.ax.set_title(f'{func} Function')
        self.ax.set_xlabel('X-axis')
        self.ax.set_ylabel('Y-axis')
        self.ax.legend()
        self.ax.grid()

        # Refresh canvas
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()