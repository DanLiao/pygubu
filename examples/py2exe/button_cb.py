# button_cb.py
import sys
import os

try:
    import tkinter as tk
    from tkinter import messagebox
except:
    import Tkinter as tk
    import tkMessageBox as messagebox

try:
    CDIR = os.path.dirname(__file__)
except NameError:
    CDIR = os.path.dirname(os.path.abspath(sys.argv[0]))

import pygubu

class Myapp:
    def __init__(self, master):
        self.builder = builder = pygubu.Builder()
        fpath = os.path.join(CDIR,"button_cb.ui")
        builder.add_from_file(fpath)

        mainwindow = builder.get_object('mainwindow', master)

        builder.connect_callbacks(self)

        callbacks = {
            'on_button2_clicked': self.on_button2_clicked
            }

        builder.connect_callbacks(callbacks)

    def on_my_button_clicked(self):
        messagebox.showinfo('From callback', 'My button was clicked !!')

    def on_button2_clicked(self):
        messagebox.showinfo('From callback', 'Button 2 was clicked !!')

if __name__ == '__main__':
    root = tk.Tk()
    app = Myapp(root)
    root.mainloop()

