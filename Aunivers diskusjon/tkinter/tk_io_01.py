"""Fra geekforgeeks"""
# importing necessary libraries
from functools import partial
import tkinter as tk
 
# defining function
 
i = 0
 
def function_name(func):
    i +=1
    print(func)

def use_i(x):
    i +=1
    return i
 
 
# creating root window
root = tk.Tk()
 
# root window title and dimension
root.title("Welcome to GeekForGeeks")
root.geometry("380x400")
 
# creating button
btn = tk.Button(root, text="Click Me", command=partial(
    function_name, f"Thanks, Geeks for Geeks {i}"))
btn.pack()
 
# running the main loop
root.mainloop()