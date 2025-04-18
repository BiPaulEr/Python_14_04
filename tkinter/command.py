import tkinter as tk

fenetre_principale = tk.Tk()
fenetre_principale.title("Fenetre Principale")
fenetre_principale.geometry("400x300")
fenetre_principale.config(background="blue")

label1 = tk.Label(fenetre_principale, text="LABEL 1", width=20, height=10)
label1.pack()

label1.bind("<Button-1>", lambda x: print("Clic Gauche"))
label1.bind("<Button-3>", lambda x: print("Clic Droit"))

label1.bind("<KeyPress-a>", lambda x: print("a"))

label1.bind("<Enter>", lambda x: print("Enter"))
label1.bind("<Leave>", lambda x: print("Leave"))

#label1.bind("<Configure>", lambda event: print(f"{event.width}x{event.height}"))
fenetre_principale.bind("<Configure>", lambda event: print(f"{event}"))
fenetre_principale.mainloop()