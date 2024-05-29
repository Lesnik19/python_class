from tkinter import Button


class MyButton:
    # создание кнопки, требуется x и y, текст, шрифт, ширина, цвет и команда
    def __init__(self, x, y, text, font, width, color, command):
        self.x = x
        self.y = y
        self.text = text
        self.width = width
        self.font = font
        self.color = color

        self.button = Button(text=self.text, font=self.font, activebackground=self.color)
        self.button.place(x=self.x, y=self.y, width=self.width)
        self.button.bind("<Button-1>", command)
