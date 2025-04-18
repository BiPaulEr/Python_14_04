import tkinter as tk

fenetre = tk.Tk()
var_texte = tk.StringVar()

entry_widget = tk.Entry(fenetre, textvariable=var_texte)
entry_widget.pack()

label = tk.Label(fenetre, textvariable=var_texte)
label.pack()

var_int = tk.IntVar()
spin_widget = tk.Spinbox(fenetre, from_=0, to=10, textvariable=var_int)
spin_widget.pack()
label2 = tk.Label(fenetre, textvariable=var_int)
label2.pack()

fenetre.mainloop()
