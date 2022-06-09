import tkinter as tk
from idlelib.configdialog import changes


plication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.hi_there = None
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Это кнопка\n"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("все работает хорошо")


root = tk.Tk()


class Application:
    pass


app = Application(master=root)




