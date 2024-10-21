import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

from utils.threading.stopped_able_threading import StoppableThread
from utils.region import *
from utils.contains import key


class SettingConverterFrame(ttk.Frame):

    def __init__(self, container):
        super().__init__(container)

        self.unit_from = "高德KEY:"

        # field options
        options = {'padx': 5, 'pady': 1}

        # temperature label
        self.temperature_label = ttk.Label(self, text=self.unit_from)
        self.temperature_label.grid(column=0, row=0, sticky='w', **options)

        # temperature entry
        self.gaodeKey = tk.StringVar()

        self.gaodeKey.set(key)

        self.gaodeKey_entry = ttk.Entry(self, textvariable=self.gaodeKey, state='disable')
        self.gaodeKey_entry.grid(column=1, row=0, sticky='w', **options)
        self.gaodeKey_entry.focus()

        # button
        self.convert_button = ttk.Button(self, text='Update', width=8)
        self.convert_button.grid(column=2, row=0, sticky='w', **options)
        self.convert_button.configure(command=self.convert)

        # result label
        self.result_label = ttk.Label(self, width=25)
        self.result_label.grid(row=1,column=0,columnspan=4, **options)
        # result label
        self.log_label = ttk.Label(self, width=40)
        self.log_label.grid(row=2,column=0,columnspan=4, **options)

        # add padding to the frame and show it
        self.grid(column=0, row=2, sticky="nsew", **options)

    def convert(self, event=None):
        """  Handle button click event
        """
        try:
            self.conn = StoppableThread(target=self.Conn)
            self.conn.setDaemon(True)  # 设置守护线程，当线程结束，守护线程同时关闭，要不然这个线程会一直运行下去。
            self.conn.start()
        except ValueError as error:
            showerror(title='Error', message=error)

    def reset(self):
        pass

    def Conn(self):
        self.result_label.config(text="数据删除开始...")
        dele()
        self.result_label.config(text="数据删除完成...")
        self.result_label.config(text="数据更新开始...")
        get(self.log_label)
        self.result_label.config(text="数据更新完成...")


