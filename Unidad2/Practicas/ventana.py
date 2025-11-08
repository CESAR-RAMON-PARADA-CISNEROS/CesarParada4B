import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("500x300")

ventana.label = tk.Label(ventana, text="Hello Word")
ventana.label.pack()
ventana.mainloop()
