from tkinter import *
from tkinter import ttk

def nazny():
    print("се работает хорошо")

root = Tk()

root = ttk.Frame(root,padding=10)
root.title ("большая кнопка")
root.geonetry ("640x480")
frn.grid()

Button(text="это кнопка"
background= "#5",  # фоновый цвет кнопки
             foreground = "#ccc",  # цвет текста
                          padx = "20",  # отступ от границ до содержимого по горизонтали
                                 pady = "8",  # отступ от границ до содержимого по вертикали
                                        font = "16",  # высота шрифта
                                               command =nazny).grid(column=3, rom=5)# ОБЯЗАТЕЛЬНО ПЕРЕДАВАТЬ ССЫЛКУ НА ФУНКЦИЮ


root.mainloop()
