import tkinter as tk


fenetre_principale = tk.Tk()
fenetre_principale.title("Fenetre Principale")
fenetre_principale.geometry("400x300")
fenetre_principale.config(background="blue")

label1 = tk.Label(fenetre_principale, text="LABEL 1")
label2 = tk.Label(fenetre_principale, text="LABEL 2")
label3 = tk.Label(fenetre_principale, text="LABEL 3")
label4 = tk.Label(fenetre_principale, text="LABEL 4")

label1.grid(row = 0, column=0, padx= 5, pady =5, sticky="nsew")
label2.grid(row = 0, column=1, padx= 5, rowspan=2, pady =5, sticky="nsew")
label3.grid(row = 1, column=0, padx= 5, pady =5, sticky="nsew")
label4.grid(row = 2, column=1, padx= 5, pady =5, sticky="nsew")

fenetre_principale.grid_columnconfigure(0, weight=1)
fenetre_principale.grid_columnconfigure(1, weight=1)
fenetre_principale.grid_rowconfigure(0, weight=1)
fenetre_principale.grid_rowconfigure(1, weight=1)
fenetre_principale.grid_rowconfigure(2, weight=1)
fenetre_principale.mainloop()