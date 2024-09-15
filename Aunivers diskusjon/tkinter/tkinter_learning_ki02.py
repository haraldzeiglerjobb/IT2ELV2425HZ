import tkinter as tk

class RutenettSpill:
    def __init__(self, master):
        self.master = master
        self.master.title("3x3 Rutenettspill")
        
        # Opprette en 3x3 rutenett
        self.brett = []
        for rad in range(3):
            rad_liste = []
            for kolonne in range(3):
                knapp = tk.Button(master, width=10, height=5, bg="white",
                                  command=lambda r=rad, k=kolonne: self.endre_farge(r, k))
                knapp.grid(row=rad, column=kolonne)
                rad_liste.append(knapp)
            self.brett.append(rad_liste)

    def endre_farge(self, rad, kolonne):
        # Endre farge på knappen som ble klikket
        knappen = self.brett[rad][kolonne]
        if knappen['bg'] == "white":
            knappen['bg'] = "black"
        else:
            knappen['bg'] = "white"

if __name__ == "__main__":
    root = tk.Tk()
    spill = RutenettSpill(root)
    root.mainloop()