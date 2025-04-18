import tkinter as tk
import random
def openWindow():
    fenetre_secodnaire = tk.Toplevel(fenetre_principale)
    fenetre_secodnaire.title(f"Fenetre SECONDAIRE")
    fenetre_secodnaire.geometry("400x300")
    fenetre_secodnaire.config(background="pink")

def changeName():
    liste_color =["blue", "red", "pink", "gray", "orange"]
    color = liste_color[random.randint(0, len(liste_color) -1)]
    fenetre_principale.configure(bg=color)

def changeLabel(event):
    if entre_text.get() != "":
        label1.config(text=entre_text.get())
    

fenetre_principale = tk.Tk()
fenetre_principale.title("Fenetre Principale")
fenetre_principale.geometry("400x300")
fenetre_principale.config(background="blue")

bouton = tk.Button(fenetre_principale, text="Open Fenetre Secondaire", command=openWindow)
bouton.bind("<Button-3>", changeLabel)
bouton.pack()
bouton2 = tk.Button(fenetre_principale, text="Change name", command=changeName)
bouton2.pack()
label1 = tk.Label(fenetre_principale, text="Label", bg="lightblue", fg="black", font=("Arial", 14))
label1.pack()
entre_text = tk.Entry(fenetre_principale)
entre_text.pack()

fenetre_principale.mainloop()