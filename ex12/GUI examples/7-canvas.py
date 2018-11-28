import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width = 200, height=200, bg='white')
canvas.pack()

line = canvas.create_line(0, 0, 100, 100, fill='red', width=2)
root.mainloop()
