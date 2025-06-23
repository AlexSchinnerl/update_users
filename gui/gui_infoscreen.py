import tkinter as tk
import ttkbootstrap as tb

from .gui_utils import STANDARD_FONT, INFOSCREEN_WINDOW_SIZE

class InfoScreen(tk.Toplevel):
    def __init__(self, parent, user_max):
        super().__init__(parent)

        self.geometry(INFOSCREEN_WINDOW_SIZE)

        self.infotext = tk.Text(self, height=20, wrap=tk.WORD)
        self.infotext.config(background="black", foreground="green")
        self.infotext.grid(row=0, column=0, sticky="nesw")

        self.percent_bar = tb.Floodgauge(self,
                                         bootstyle="success",
                                         font=STANDARD_FONT,
                                         mask=f"User verarbeitet: 0/{user_max}",
                                         maximum=user_max,
                                         orient="horizontal",
                                         mode="determinate",
                                         value=0, # Start Value,
                                         )
        self.percent_bar.grid(row=1, column=0, sticky="nesw")