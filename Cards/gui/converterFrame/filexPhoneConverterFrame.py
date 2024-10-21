import tkinter as tk
from tkinter import ttk


class FixedlineTelephoneConverterFrame(ttk.Frame):

    def __init__(self, container, title):
        super().__init__(container)

        # field options
        options = {'padx': 0, 'pady': 1}

        self.labelFrame = ttk.LabelFrame(self, text=title)
        self.labelFrame.grid(column=0, row=0, sticky='w', **options)

        # add padding to the frame and show it
        self.grid(column=0, row=1, sticky="nsew", **options)

    def reset(self):
        pass