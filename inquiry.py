from tkinter import*
from tkinter.ttk import*
from tkinter import messagebox

class LoginWindow(Tk):
    def _init_(self, *args, **kwargs):
        Tk._init_(self, *args, **kwargs)

        self.title("Login")
        self.geometry("400x300")
lw=LoginWindow()
lw.mainloop()
