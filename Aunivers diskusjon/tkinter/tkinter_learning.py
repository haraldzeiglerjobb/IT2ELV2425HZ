"""
Whilst learning tkinter,
this is the notebook to keep track
of the
learning process

I use this site for learning tk:
https://realpython.com/python-gui-tkinter/
"""

import tkinter as tk
# import pygame as pg

window = tk.Tk()

label = tk.Label(text="Hello, Tkinter")
ipsum = tk.Label(text = str(
                 "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium\n"+
                 "doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore \n"+
                 "veritatis et quasi \n architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam \n"+
                 "voluptatem quia voluptas sit aspernatur \n "+
                 "aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem \n"+
                 "sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, \n"+
                 "consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut \n"+
                 "labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis \n"+
                 "nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea \n"+
                 "commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit \n"+
                 "esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo \n voluptas nulla pariatur?"))

#txt = str("lorem ipsum"+"hello")
#ipsum = tk.Label(text = ipsum)
#label.pack()
#ipsum.pack()

#window.mainloop()

"""
A bit more advanced label
"""

label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)

#label.pack()
#window.mainloop()

label = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10
)

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

entry = tk.Entry(fg="yellow", bg="blue", width=50)

label.pack()
button.pack()
entry.pack()

window.mainloop()
print(entry.get("1.0",tk.END))
window.mainloop()

#print(name)