import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

from gui.converterFrame.commonFrame import CommonConverterFrame
from utils.IDCards import passport, military, taiwan, hangkangAomen


class OtherConverterFrame(ttk.Frame):

    def __init__(self, container, text):
        super().__init__(container)

        self.container = container
        self.text = text

        # field options
        options = {'padx': 0, 'pady': 1}

        # temperature label
        self.allLabel = ttk.Frame(self)

        self.init_passport(self.allLabel, **options)

        self.allLabel.grid(column=0, row=0, sticky='w', **options)

        # self.log_frame = ttk.Frame(self)
        # self.text1 = CommonConverterFrame.init_log(self.log_frame, self.log_frame, **options)
        # self.log_frame.grid(column=0, row=1, sticky='w', **options)

        # add padding to the frame and show it
        self.grid(column=0, row=2, sticky="nsew", **options)

    def init_passport(self, container, **options):
        # button
        self.passport_button = tk.Button(container, text='护照',  bg="#DCDCDC", width=4)
        self.passport_button.grid(column=0, row=0, sticky='w', **options)
        self.passport_button.configure(command=self.convertPassport)

        # button
        self.passport_button = tk.Button(container, text='军人证', bg="#DCDCDC",  width=6)
        self.passport_button.grid(column=1, row=0, sticky='w', **options)
        self.passport_button.configure(command=self.convertMilitary)

        # 台胞证
        self.passport_button = tk.Button(container, text='台胞证', bg="#DCDCDC",  width=6)
        self.passport_button.grid(column=2, row=0, sticky='w', **options)
        self.passport_button.configure(command=self.convertTaiwan)

        # 港澳通行证
        self.passport_button = tk.Button(container, text='港澳通行证', bg="#DCDCDC",  width=10)
        self.passport_button.grid(column=3, row=0, sticky='w', **options)
        self.passport_button.configure(command=self.convertHangkangAomen)

    def convertPassport(self):
        self.text.insert(tk.END, passport() + '\n' + '\n')
        self.text.see(tk.END)

    def convertMilitary(self, event=None):
        """  Handle button click event
        """
        self.text.insert(tk.END, military() + '\n' + '\n')
        self.text.see(tk.END)

    def convertTaiwan(self, event=None):
        """  Handle button click event
        """
        self.text.insert(tk.END, taiwan() + '\n' + '\n')
        self.text.see(tk.END)

    def convertHangkangAomen(self, event=None):
        """  Handle button click event
        """
        self.text.insert(tk.END, hangkangAomen() + '\n' + '\n')
        self.text.see(tk.END)

    def reset(self):
        pass



