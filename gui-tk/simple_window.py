try:
    import Tkinter as tk
    from Tkinter import ttk, scrolledtext
except ImportError:
    import tkinter as tk
    from tkinter import ttk, scrolledtext

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
    text_entered.focus()
    return text_entered


def add_combobox(window, width=10, column=0, row=0, values=None):
    text = tk.StringVar()
    text_chosen = ttk.Combobox(
        window, width=width, textvariable=text, state='readonly')
    text_chosen.grid(column=column, row=row)
    text_chosen['values'] = values
    return text_chosen


def add_checkbox(window, text, column=0, row=0):
    status_var = tk.IntVar()
    check = tk.Checkbutton(window, text=text, variable=status_var)
    check.grid(column=column, row=row)
    return check, status_var


def add_scrolledtext(
        window, width=20, height=5, wrap=tk.WORD,
        column=0, row=0, columnspan=3):
    scroll_text = scrolledtext.ScrolledText(
        window, width=width, height=height, wrap=wrap)
    scroll_text.grid(column=column, row=row, columnspan=3)
    return scroll_text


def click_button_action(text):
    print(text.get())
    text.configure(foreground='red')


def click_button_action_checkbox(status):
    print("[checkbox] is selected: ", bool(status.get()))


def click_button_action_scrolledtext(text):
    print(text.get('1.0', tk.END))
    text.configure(foreground='red')


def main():
    window = add_window("Simple Window")

    l1 = add_label(window, "Provide text:", column=0, row=0)
    text_entered = add_text_widget(window, column=1, row=0)
    action = add_button(
        window, text="Process", column=2, row=0,
        command=partial(click_button_action, text_entered))

    l2 = add_label(window, "Select:", column=0, row=1)
    values = (1, 2, 3, 4, 5)
    text_chosen = add_combobox(window, column=1, row=1, values=values)
    text_chosen.current(0)
    action = add_button(
        window, text="Process", column=2, row=1,
        command=partial(click_button_action, text_chosen))

    l3 = add_label(window, "Select:", column=0, row=2)
    check_box, status_var = add_checkbox(window, text="Enable", column=1, row=2)
    action = add_button(
        window, text="Process", column=2, row=2,
        command=partial(click_button_action_checkbox, status_var))

    text = add_scrolledtext(window, column=0, row=3)
    action = add_button(
        window, text="Process", column=4, row=3,
        command=partial(click_button_action_scrolledtext, text))

    window.mainloop()

if __name__ == "__main__":
    main()