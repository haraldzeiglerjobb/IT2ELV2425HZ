import tkinter as tk

r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button.pack()
r.mainloop()

"""UTvidelse: Fem knapper under hverandre"""
r = tk.Tk()
r.title('Counting Seconds')
for i in range(5):
    button = tk.Button(r, text='Stop', width=25, command=r.destroy)
    button.pack()
r.mainloop()