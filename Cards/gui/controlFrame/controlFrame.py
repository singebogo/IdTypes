import tkinter as tk
from tkinter import ttk

from utils.temperatureConverter import TemperatureConverter
from gui.converterFrame.groupConverterFrame import GroupConverterFrame
from gui.converterFrame.personConverterFrame import PersonConverterFrame
from gui.converterFrame.settingConverterFrame import SettingConverterFrame
from utils.dbLites.region import select_province_sql


class ControlFrame(ttk.LabelFrame):

    def __init__(self, container):
        super(ControlFrame, self).__init__(container)

        self['text'] = '类型'
        options = {'padx': 0, 'pady': 1}
        # radio buttons
        frame = tk.Frame(self)
        self.selected_value = tk.IntVar()
        ttk.Radiobutton(
            frame,
            text='Person',
            value=0,
            variable=self.selected_value,
            command=self.change_frame).grid(column=0, row=0, **options)

        ttk.Radiobutton(
            frame,
            text='Group',
            value=1,
            variable=self.selected_value,
            command=self.change_frame).grid(column=1, row=0, **options)

        # ttk.Radiobutton(
        #     frame,
        #     text='setting',
        #     value=2,
        #     variable=self.selected_value,
        #     command=self.change_frame).grid(column=2, row=0, **options)
        frame.grid(column=0, row=0, sticky='w', **options)
        self.grid(column=0, row=0, sticky='w', **options)

        # initialize frames
        self.frames = {}
        self.frames[0] = PersonConverterFrame(
            self,
            'Person',
            TemperatureConverter.fahrenheit_to_celsius)

        self.frames[1] = GroupConverterFrame(
            self,
            'Group',
            TemperatureConverter.celsius_to_fahrenheit)
        #
        # self.frames[2] = SettingConverterFrame(
        #     container,
        #     'setting',
        #     TemperatureConverter.celsius_to_fahrenheit)
        #
        self.change_frame()

    def change_frame(self):
        self.frame = self.frames[self.selected_value.get()]
        self.frame.reset()
        self.frame.tkraise()

    def reload(self):
        provincesList = select_province_sql()
        self.frame.init_data(provincesList)
