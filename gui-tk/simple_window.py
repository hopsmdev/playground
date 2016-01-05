import tkinter as tk
from tkinter import ttk
from functools import partial


def add_window(title):
    window = tk.Tk()
    window.title(title)
    return window


def add_label(window, text, column=0, row=0):
    label = ttk.Label(window, text=text)
    label.grid(column=column, row=row)
    return label


def add_button(window, text, command, column=0, row=0):
    action = ttk.Button(window, text=text, command=command)
    action.grid(column=column, row=row)
    return action


def add_text_widget(window, width=10, column=0, row=0):
    text = tk.StringVar()
    text_entered = ttk.Entry(window, width=width, textvariable=text)
    text_entered.grid(column=column, row=row)
    return text_entered


def click_button_action(text):
    text.configure(foreground='red')


def main():
    window = add_window("Simple Window")
    l1 = add_label(window, "Provide text:", column=0, row=0)
    text_entered = add_text_widget(window, column=0, row=1)
    action = add_button(
        window, text="Process", column=1, row=1,
        command=partial(click_button_action, text_entered))

    window.mainloop()

if __name__ == "__main__":
    main()