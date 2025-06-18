import tkinter as tk
import ttkbootstrap as tb

from .gui_utils import STANDARD_FONT

class InfoScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pack(pady=20)

        infoscreen_length = 110

        self.infotext = tk.Text(self, height=20, width=infoscreen_length, wrap=tk.WORD)
        self.infotext.config(background="black", foreground="green")
        self.infotext.grid(row=0, column=0)

        self.percent_bar = tb.Floodgauge(self,
                                         bootstyle="success",
                                         font=STANDARD_FONT,
                                         mask="User verarbeitet: {}",
                                         maximum=100,
                                         orient="horizontal",
                                         mode="determinate",
                                         value=0, # Start Value,
                                         length = infoscreen_length*10
                                         )
        self.percent_bar.grid(row=1, column=0)