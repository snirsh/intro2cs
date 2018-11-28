import tkinter as tk

root = tk.Tk()

my_hero = ['S', 'p', 'o', 'n', 'g', 'e', 'B', 'o', 'b']
my_hero = ['h']

def add_letter(index):
    label = tk.Label(root, text=my_hero[index])
    label.pack()
    # label.after(500, add_letter((index+1)) % len(my_hero))

root.after(1000, add_letter(0))  # add_letter will run as soon as the mainloop starts.
root.mainloop()
