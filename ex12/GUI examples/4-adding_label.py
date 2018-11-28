import tkinter as tk


root = tk.Tk()
label_text = tk.Label(root, text='Hello!!', font=('Helvetica',20))
# Option 1
#label_text.pack()
#label_text.pack(expand=True)
#label_text.pack(fill='y')

# # Option 2
#label_text.pack(side=tk.RIGHT)

# # Option 3
#label_text.grid()

# # Option 4
label_text.grid(row=0)
label_text2 = tk.Label(root, text='bye!', font=('Helvetica',20))
label_text2.grid(row=1)
root.mainloop()
