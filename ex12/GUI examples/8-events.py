import tkinter as tk

def print_hi(event):
    print('hi')

root = tk.Tk()
canvas = tk.Canvas(root, width = 200, height=200, bg='white')
canvas.pack()

canvas.bind("<Button-1>", print_hi)



root.mainloop()
