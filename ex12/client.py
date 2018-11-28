from tkinter import *
from tkinter import Listbox
import socket
import select
import ast
import sys
from copy import deepcopy

BUFFER_SIZE = 1024
MESSAGE_DELIMITER = b'\n'
RECTANGLE = "Rectangle"
TRIANGLE = "Triangle"
LINE = "Line"
CIRCLE = "Circle"
SCREW_YOU_GUYS_IM_GOING_HOME = "leave"


class Client:
    def __init__(self, address, port, name, group):
        self.address = address
        self.port = port
        self.server = (address, port)
        self.name = name
        self.group = group
        self.points = []
        self.shape = None
        self.socket = socket.socket()
        self.client_Gui()

    def connect_to_server(self):
        self.socket.connect((self.address, self.port))
        message = b'join;' + bytes(self.name, "UTF-8") + b';' + bytes(
            self.group, "UTF-8") + b'\n'
        self.socket.sendall(message)

    def message_to_server(self, message):
        encrypted_message = bytes(message, "UTF-8") + b'\n'
        self.socket.sendall(encrypted_message)

    def read_from_server(self):
        output_message = str('')
        r, w, x = select.select([self.socket], [], [], 0.01)
        for sock in r:
            if sock == self.socket:
                data = r[0].recv(BUFFER_SIZE)
                output_message += data.decode()
        output_message = output_message[:-1]
        if output_message:
            print("output = ", output_message)
        if "join;" in output_message:
            self.lb.insert(END, output_message[5:])
        if "shape;" in output_message:
            self.draw_shape_from_server(output_message[6:])
        if "leave;" in output_message:
            left = output_message[6:]
            self.lb.delete(self.lb.index(left))
        if "users;" in output_message and "," in output_message:
            users_to_add = output_message[6:].split(',')
            print(users_to_add)
            for user in users_to_add:
                if user != self.name:
                    print("user = ", user)
                    self.lb.insert(END, user)
        if "error;" in output_message:
            print(output_message[5:])
        self.root.after(1000, self.read_from_server)

    def client_Gui(self):
        self.connect_to_server()
        self.root = Tk()
        self.canvas = Canvas(self.root, width=500, height=500, bg='white')
        menu = Menu(self.root)
        self.root.config(menu=menu)
        menu.add_command(labe="Help", command=Message)
        toolbar = Frame(self.root, bd=1)
        optionsLabel = Label(toolbar, text="Colors:")
        self.color = StringVar(toolbar)
        self.color.set("blue")
        colors = ["blue", "red", "green", "yellow", "black", "violet"]
        colorOptions = OptionMenu(toolbar, self.color, *colors)
        button1 = Button(toolbar, text=RECTANGLE,
                         command=lambda: self.set_shape(RECTANGLE))
        button2 = Button(toolbar, text=TRIANGLE,
                         command=lambda: self.set_shape(TRIANGLE))
        button3 = Button(toolbar, text=LINE,
                         command=lambda: self.set_shape(LINE))
        button4 = Button(toolbar, text=CIRCLE,
                         command=lambda: self.set_shape(CIRCLE))
        # creating a window with the users and groups
        self.canvas.bind("<Button-1>", self.draw_shape)
        self.lb = Listbox(self.root, selectmode=BROWSE)
        self.lb.insert(END, self.group)
        self.lb.insert(END, self.name)
        self.lb.pack(side=LEFT)
        # Packing and grid placing
        optionsLabel.grid(row=0, column=0, sticky=W)
        colorOptions.grid(row=0, column=1, sticky=W)
        button1.grid(row=0, column=3, sticky=E)
        button2.grid(row=0, column=4, sticky=E)
        button3.grid(row=0, column=5, sticky=E)
        button4.grid(row=0, column=6, sticky=E)
        toolbar.pack(side=TOP)
        self.canvas.pack()
        self.read_from_server()
        self.root.mainloop()
        self.message_to_server(SCREW_YOU_GUYS_IM_GOING_HOME)
        self.socket.close()

    def set_shape(self, shape):
        if self.shape != shape:
            self.points = []
            self.shape = shape

    def draw_shape(self, event):
        new_point = (event.x, event.y)
        self.points.append(new_point)
        points_amount = len(self.points)
        if self.shape is RECTANGLE:
            if points_amount == 2:
                self.draw_rect()
        elif self.shape is LINE:
            if points_amount == 2:
                self.draw_line()
        elif self.shape is CIRCLE:
            if points_amount == 2:
                self.draw_circ()
        elif self.shape is TRIANGLE:
            if points_amount == 3:
                self.draw_tria()

    def draw_rect(self):
        first_dot = self.points[0]
        second_dot = self.points[1]
        self.canvas.create_rectangle(first_dot[0], first_dot[1], second_dot[
            0], second_dot[1], fill=self.color.get())
        self.canvas.create_text(first_dot[0], first_dot[1], text=self.name,
                                fill='black', font=("David", 16))
        message = str("shape;" + self.shape + ";" + str(self.points) +
                      ";" + self.color.get())
        self.message_to_server(message)
        self.points.clear()

    def draw_line(self):
        first_dot = self.points[0]
        second_dot = self.points[1]
        self.canvas.create_line(first_dot[0], first_dot[1], second_dot[0],
                                second_dot[1], fill=self.color.get())
        self.canvas.create_text(first_dot[0], first_dot[1], text=self.name,
                                fill='black', font=("David", 16))
        message = str("shape;" + self.shape + ";" + str(self.points) +
                      ";" + self.color.get())
        self.message_to_server(message)
        self.points.clear()

    def draw_circ(self):
        first_dot = self.points[0]
        second_dot = self.points[1]
        self.canvas.create_oval(first_dot[0], first_dot[1], second_dot[0],
                                second_dot[1], fill=self.color.get())
        self.canvas.create_text(first_dot[0], first_dot[1], text=self.name,
                                fill='black', font=("David", 16))
        message = str("shape;" + self.shape + ";" + str(self.points) +
                      ";" + self.color.get())
        self.message_to_server(message)
        self.points.clear()

    def draw_tria(self):
        first_dot = self.points[0]
        second_dot = self.points[1]
        third_dot = self.points[2]
        self.canvas.create_polygon(first_dot[0], first_dot[1], second_dot[0],
                                   second_dot[1], third_dot[0], third_dot[1],
                                   fill=self.color.get())
        self.canvas.create_text(first_dot[0], first_dot[1], text=self.name,
                                fill='black', font=("David", 16))
        message = str("shape;" + self.shape + ";" + str(self.points) +
                      ";" + self.color.get())
        self.message_to_server(message)
        self.points.clear()

    def draw_shape_from_server(self, shape_properties):
        coords = list(ast.literal_eval(shape_properties[2]))
        list_benayim = deepcopy(self.points)
        name_benayim = deepcopy(self.name)
        self.points = coords
        self.name = shape_properties[0]
        if shape_properties[1] is RECTANGLE:
            self.draw_rect()
        elif shape_properties[1] is LINE:
            self.draw_line()
        elif shape_properties[1] is CIRCLE:
            self.draw_circ()
        elif shape_properties[1] is TRIANGLE:
            self.draw_tria()
        self.points = deepcopy(list_benayim)
        self.name = deepcopy(name_benayim)


def main():
    player = Client(address, port, name, group)

    return  # Bye!


if __name__ == "__main__":
    MAX_ARGUMENTS = 4  # amount of needed parameters.
    file_source = 1
    if len(sys.argv) == MAX_ARGUMENTS + file_source:
        # needed exactly the file, and 5 more parameters.
        address = sys.argv[1]
        port = int(sys.argv[2])
        name = sys.argv[3]
        group = sys.argv[4]
        # we got all the needed parameters. ready to run "main".
        main()
    else:  # wrong amount of parameters...
        print("wrong number of parameters. the correct usage is:\n"
              "ex12.py <address> <port> <name> <group>")
