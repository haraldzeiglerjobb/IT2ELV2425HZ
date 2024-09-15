import tkinter as tk

# Opprett hovedvinduet
root = tk.Tk()
root.title("Flere Bokser i Tkinter App")
root.geometry("400x390")

# Første ramme (boks)
frame1 = tk.Frame(root, bg="lightblue", padx=20, pady=20)
frame1.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

label1 = tk.Label(frame1, text="Boks 1", bg="lightblue")
label1.pack()

button1 = tk.Button(frame1, text="Klikk meg fra boks 1", command=lambda: label1.config(text="Knappen ble trykket!"))
button1.pack(pady=5)

# Andre ramme (boks)
frame2 = tk.Frame(root, bg="lightgreen", padx=20, pady=20)
frame2.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

label2 = tk.Label(frame2, text="Boks 2", bg="lightgreen")
label2.pack()

button2 = tk.Button(frame2, text="Klikk meg fra boks 2", command=lambda: label2.config(text="Knappen ble trykket!"))
button2.pack(pady=5)

# Tredje ramme (boks)
frame3 = tk.Frame(root, bg="lightcoral", padx=20, pady=20)
frame3.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

label3 = tk.Label(frame3, text="Boks 3", bg="lightcoral")
label3.pack()

button3 = tk.Button(frame3, text="Klikk meg fra boks 3", command=lambda: label3.config(text="Knappen ble trykket!"))
button3.pack(pady=5)

# Start hovedløkka
root.mainloop()