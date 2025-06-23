import tkinter as tk
import ttkbootstrap as tb

from .gui_utils import STANDARD_FONT

# class InfoScreen(tk.Frame):
#     def __init__(self, parent):
#         super().__init__(parent)

#         self.pack(pady=20)

#         self.infotext = tk.Text(self, height=20, wrap=tk.WORD)
#         self.infotext.config(background="black", foreground="green")
#         self.infotext.grid(row=0, column=0, sticky="nesw")

#         self.percent_bar = tb.Floodgauge(self,
#                                          bootstyle="success",
#                                          font=STANDARD_FONT,
#                                          mask="User verarbeitet: {}",
#                                          maximum=100,
#                                          orient="horizontal",
#                                          mode="determinate",
#                                          value=0, # Start Value,
#                                          )
#         self.percent_bar.grid(row=1, column=0, sticky="nesw")

class InfoScreen(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # self.pack(pady=20)

        self.infotext = tk.Text(self, height=20, wrap=tk.WORD)
        self.infotext.config(background="black", foreground="green")
        self.infotext.grid(row=0, column=0, sticky="nesw")

        self.percent_bar = tb.Floodgauge(self,
                                         bootstyle="success",
                                         font=STANDARD_FONT,
                                         mask="User verarbeitet: {}",
                                         maximum=100,
                                         orient="horizontal",
                                         mode="determinate",
                                         value=0, # Start Value,
                                         )
        self.percent_bar.grid(row=1, column=0, sticky="nesw")