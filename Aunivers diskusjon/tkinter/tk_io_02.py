from functools import partial
 
def mltask (mlvar):
    print (mlvar)
    return mlvar
 
from tkinter import *
root = Tk()
root.configure(background = 'white')
root.geometry("800x500")
 
cbutton = Button(root, text="Let's Start", bg="white", \
                        fg="firebrick", relief = "groove", font = "Helvitica 60")
cbutton.pack()
 
mymenu = Menu(root)
root.config(menu=mymenu)
# Create missing letter easy menu
MLEasyMenu = Menu(mymenu)
mymenu.add_cascade(label = "easy", menu=MLEasyMenu)
MLEasyMenu.add_command(label="firstcolor", command = partial(mltask,'red'))
MLEasyMenu.add_command(label="secondcolor", command= partial(mltask,'green'))
 
root.mainloop()