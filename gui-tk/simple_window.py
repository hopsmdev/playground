import tkinter as tk
from tkinter import ttk
from functools import partial


def get_window(title):
    window = tk.Tk()
    window.title(title)
    return window


def add_label(window, text):
    label = ttk.Label(window, text=text)
    label.grid(column=0, row=0)
    return label


def click_button(label):
    label.configure(foreground='red')


def main():
    window = get_window("Simple Window")
    l1 = add_label(window, "label_1")
    action = ttk.Button(window, text="Click", command=partial(click_button, l1))
    action.grid(column=1, row=0)
    window.mainloop()

if __name__ == "__main__":
    main()