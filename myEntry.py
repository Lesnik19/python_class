from tkinter import Entry


class MyEntry:
    # создание поля для ввода, требуется x и y, шрифт, ширина и
    # использовать/не использовать маску
    def __init__(self, x, y, font, width, is_shown=True):
        if not is_shown:
            show = '*'
        else:
            show = ''
        self.entry = Entry(font=font, show=show)
        self.entry.place(x=x, y=y, width=width)
