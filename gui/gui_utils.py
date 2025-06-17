import tkinter as tk

STANDARD_FONT = ("Arial", 14)
TITLE_FONT = ("Arial", 18)

WINDOW_SIZE = ("1250x750")
INFOSCREEN_WINDOW_SIZE = ("500x500")

def update_textbox(infoscreen, text_2_insert):
    infoscreen.infotext.insert(tk.INSERT, text_2_insert)
    infoscreen.update()