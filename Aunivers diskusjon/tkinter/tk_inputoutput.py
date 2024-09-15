import tkinter as tk

# Opprett hovedvinduet
root = tk.Tk()
root.title("Flere Bokser i Tkinter App")
root.geometry("400x200")

# Første ramme (boks)
frame1 = tk.Frame(root, bg="lightblue", padx=20, pady=20)
frame1.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

label1 = tk.Label(frame1, text="Boks 1", bg="lightblue")
label1.pack()

button1 = tk.Button(frame1, text="Klikk meg fra boks 1", command=lambda: label1.config(text="Knappen ble trykket!"))
button1.pack(pady=5)

frame2 = tk.Frame(root, bg="lightblue", padx=20, pady=20)
frame2.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

label2 = tk.Label(frame2, text="Boks 2", bg="lightblue")
label2.pack()

button2 = tk.Button(frame2, text="Klikk for å telle oppover!")
button2.pack(pady=5)
root.mainloop()

i = 0

def increase(x):
    i +=1
    return i

clicked = False
while True:
    #root.mainloop()


    if clicked:
        label2.config(bg = "red", text = f"Hei! .....{i}")
        i +=1
        clicked = False
    label2.pack()
    root.mainloop()

root.mainloop()