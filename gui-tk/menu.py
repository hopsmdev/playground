try:
    import Tkinter as tk
    from Tkinter import Menu, messagebox
except ImportError:
    import tkinter as tk
    from tkinter import Menu, messagebox

from functools import partial
from collections import OrderedDict


def add_menu(handler, cascade=True, label=None, **kwargs):
    menu = Menu(handler, tearoff=0, **kwargs)
    if cascade:
        handler.add_cascade(label=label, menu=menu)
    return handler, menu


def add_commands(menu, commands_dict):
    for label, command in commands_dict.items():
        menu.add_command(label=label, command=command)
    return menu


class Command(object):

    @classmethod
    def new(cls):
        messagebox.showinfo("New", "Create new something")

    @classmethod
    def open(cls):
        messagebox.showinfo("Open", "Open something")

    @classmethod
    def save(cls):
        messagebox.showinfo("Save", "Save something")

    @classmethod
    def exit(cls, root):
        answer = messagebox.askyesno("Exit", "Are you sure")
        if answer:
            root.quit()

    @classmethod
    def help(cls):
        messagebox.showinfo("Help", "It should help ...")

    @classmethod
    def about(cls):
        messagebox.showinfo("About", "About this program")


def main():
    root = tk.Tk(className="Test Menu")

    root, menu = add_menu(root, cascade=False)
    root.config(menu=menu)

    root, file_menu = add_menu(menu, label='File')
    root, help_menu = add_menu(menu, label='Help')

    file_commands = OrderedDict([
        ('New', Command.new),
        ('Open', Command.open),
        ('Save', Command.save),
        ('Exit', partial(Command.exit, root)),
    ])

    help_commands = OrderedDict([
        ('Help', Command.help),
        ('About', Command.about),
    ])

    add_commands(file_menu, file_commands)
    add_commands(help_menu, help_commands)

    root.mainloop()

if __name__ == "__main__":
    main()