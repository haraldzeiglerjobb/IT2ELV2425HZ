import tkinter as tk

# Opprett hovedvinduet
root = tk.Tk()
root.title("Min Første Tkinter App")
root.geometry("300x200")  # Sett størrelsen på vinduet

# Legg til en etikett
label = tk.Label(root, text="Hei, verden!")
label.pack(pady=20)  # Plasser etiketten i midten av vinduet

# Legg til en knapp
def on_button_click():
    label.config(text="Knappen ble trykket!")

button = tk.Button(root, text="Klikk meg!", command=on_button_click)
button.pack(pady=10)  # Plasser knappen under etiketten

# Start hovedløkka
root.mainloop()