import tkinter as tk


def button_function():
    # Just some function
    print('square pants')

root = tk.Tk()
label_text1 = tk.Label(root,
                       text='Hello!!',
                       font=('Helvetica',20))
label_text1.pack()

button = tk.Button(root,
                   text='SpongeBob',
                   command=button_function
                   # What function to call
                   # when the button is pressed
                   )
button.pack()
root.mainloop()
