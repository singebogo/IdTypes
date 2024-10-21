import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

from gui.converterFrame.IDConverterFrame import IDConverterFrame
from gui.converterFrame.OtherConverterFrame import OtherConverterFrame
from utils.temperatureConverter import TemperatureConverter


class PersonConverterFrame(ttk.LabelFrame):

    def __init__(self, container, unit_from, converter):
        super().__init__(container)

        self.unit_from = unit_from
        self.converter = converter

        options = {'padx': 0, 'pady': 1}

        self['text'] = '个人证件类型'
        frame = tk.Frame(self)
        frame.grid(column=0, row=0, sticky='w', **options)
        self.init_radio_frame(frame, **options)

        self.grid(column=0, row=1, sticky="nsew", **options)

        # initialize frames
        self.frames = {}
        self.frames[0] = IDConverterFrame(
            self,
            'Person',
            TemperatureConverter.fahrenheit_to_celsius)

        self.frames[1] = OtherConverterFrame(
            self,
            'Group')

        self.change_frame()

    def init_radio_frame(self, frame, **options):
        # radio buttons
        self.selected_value = tk.IntVar()
        self.radio1 = ttk.Radiobutton(
            frame,
            text='身份证',
            value=0,
            variable=self.selected_value,
            command=self.change_frame).grid(column=0, row=0, sticky='E', **options)

        # self.radio2 = ttk.Radiobutton(
        #     frame,
        #     text='其他',
        #     value=1,
        #     variable=self.selected_value,
        #     command=self.change_frame).grid(column=1, row=0, sticky='w', **options)

    def change_frame(self):
        frame = self.frames[self.selected_value.get()]
        frame.reset()
        frame.tkraise()

    def reset(self):
        pass
