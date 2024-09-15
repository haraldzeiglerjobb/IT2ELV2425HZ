#How to put text on the screen
from tkinter import *
import time

#To learn this, let ut put som text to loop not too fast out here
#Let us control the time a little better now.

time_start = time.time_ns()
time_ongoing = time_start
text_variable = ""
delay = 1E+9

#Let ut put the tkinter stuff here
root = Tk()
T = Text(root, height=2, width=30)
T.pack()
T.insert(END, text_variable)

i = 0

while True:
    if time.time_ns()-time_ongoing>delay:
        text_variable = "Teller: "+str(i)
        T.pack()
        T.insert(END, text_variable)
        i +=1

mainloop()