import tkinter as tk


root = tk.Tk()
label_text1 = tk.Label(root, text='Hello!!', font=('Helvetica',20))
label_text1.pack()

smiley_img = tk.PhotoImage(file="smiley.png")
label_text2 = tk.Label(root, image=smiley_img)
label_text2.pack()

root.mainloop()
