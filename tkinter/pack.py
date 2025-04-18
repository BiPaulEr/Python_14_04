import tkinter as tk


fenetre_principale = tk.Tk()
fenetre_principale.title("Fenetre Principale")
fenetre_principale.geometry("400x300")
fenetre_principale.config(background="blue")

label1 = tk.Label(fenetre_principale, text="LABEL 1 TOP X")
label1.pack(side=tk.TOP, fill=tk.X, padx =10, pady =10)

label2 = tk.Label(fenetre_principale, text="LABEL 2 LEFT Y")
label2.pack(side=tk.LEFT, fill=tk.Y, padx =10, pady =10)

label3 = tk.Label(fenetre_principale, text="LABEL 3 BOTTOM EXPAND")
label3.pack(side=tk.BOTTOM, expand=True, padx =10, pady =10)

label4 = tk.Label(fenetre_principale, text="LABEL 4 BOTTOM")
label4.pack(side=tk.BOTTOM, expand=False, padx =10, pady =10)
fenetre_principale.mainloop()