import tkinter as tk

hi_counter = 0

def print_hi(event):
    global hi_counter
    print('hi', hi_counter)
    hi_counter += 1

def print_bi(event):
    print('bi')

root = tk.Tk()
canvas = tk.Canvas(root, width = 200, height=200, bg='white')
canvas.pack()

canvas.bind("<Button-1>", print_hi)
canvas.bind("<Button-3>", print_bi)


root.mainloop()
