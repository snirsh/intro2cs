import tkinter as tk

def click(event):
    print("button_pressed",event.x, event.y)

root = tk.Tk()
canvas = tk.Canvas(root, width = 200, height=200, bg='white')
canvas.pack()

canvas.bind("<Button-1>", click)

root.mainloop()
