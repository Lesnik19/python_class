from tkinter import *


class MyLabel:
    # создание текста, требуется x и y, текст, ширина и цвет
    def __init__(self, x, y, text, font, bg_color):
        self.label = Label(text=text, font=font, background=bg_color)
        self.label.place(x=x, y=y)
