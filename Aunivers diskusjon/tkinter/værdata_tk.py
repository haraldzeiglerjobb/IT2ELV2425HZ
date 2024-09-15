import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

# Sample temperature data for a week (in degrees Celsius)
temperature_data = {
    "Monday": [20, 21, 19, 22, 20],
    "Tuesday": [22, 23, 21, 24, 23],
    "Wednesday": [19, 20, 18, 21, 20],
    "Thursday": [23, 24, 22, 25, 24],
    "Friday": [21, 22, 20, 23, 21],
    "Saturday": [25, 26, 24, 27, 26],
    "Sunday": [24, 25, 23, 26, 24]
}

def plot_temperature(day):
    """Plot temperature for the selected day."""
    # Fetch the temperature data for the selected day
    temperatures = temperature_data[day]
    
    # Create a new figure
    plt.figure()
    plt.plot(temperatures, marker='o')
    plt.title(f'Temperature on {day}')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Temperature (°C)')
    plt.xticks(range(len(temperatures)), [f'{i} AM' for i in range(len(temperatures))])
    plt.grid()
    plt.show()

def on_select(event):
    """Handle selection from the dropdown menu."""
    selected_day = day_combobox.get()  # Get selected day from the combobox
    plot_temperature(selected_day)  # Plot the temperature

# Create the main window
root = tk.Tk()
root.title("Weather Data Viewer")

# Create a label for instructions
label = tk.Label(root, text="Select a day to view temperature data:")
label.pack(pady=10)

# Create a dropdown menu using ComboBox
day_combobox = ttk.Combobox(root, values=list(temperature_data.keys()))
day_combobox.pack(pady=10)

# Bind selection event to the combobox
day_combobox.bind("<>", on_select)

# Run the application
root.mainloop()