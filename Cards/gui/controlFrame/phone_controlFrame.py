import tkinter as tk
from tkinter import ttk

from gui.converterFrame.fixedLineTelephoneConverterFrame import FixedlineTelephoneConverterFrame
from gui.converterFrame.phoneConverterFrame import PhoneConverterFrame


class PhoneControlFrame(ttk.LabelFrame):

    def __init__(self, container):
        super(PhoneControlFrame, self).__init__(container)

        self['text'] = '类型'
        options = {'padx': 0, 'pady': 1}
        # radio buttons
        frame = tk.Frame(self)
        self.selected_value = tk.IntVar()
        ttk.Radiobutton(
            frame,
            text='手机号码',
            value=0,
            variable=self.selected_value,
            command=self.change_frame).grid(column=0, row=0, **options)

        ttk.Radiobutton(
            frame,
            text='固定电话',
            value=1,
            variable=self.selected_value,
            command=self.change_frame).grid(column=1, row=0, **options)

        frame.grid(column=0, row=0, sticky='w', **options)
        self.grid(column=0, row=0, sticky='w', **options)

        # initialize frames
        self.frames = {}
        self.frames[0] = PhoneConverterFrame(
            self,
            '移动电话号码')

        self.frames[1] = FixedlineTelephoneConverterFrame(
            self,
            '固定电话号码')

        self.change_frame()

    def change_frame(self):
        self.frame = self.frames[self.selected_value.get()]
        self.frame.reset()
        self.frame.tkraise()

    def reload(self):
        pass
