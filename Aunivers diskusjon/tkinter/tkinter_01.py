import tkinter as tk

window = tk.Tk()
window.title("My First Tkinter App")

label = tk.Label(window, text="Hello, World!")
label.pack()

button = tk.Button(window, text="Click Me!", command=window.quit)
button.pack()

window.mainloop()
