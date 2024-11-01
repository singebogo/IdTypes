import os
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
import win32gui
import win32con

from utils.threading.stopped_able_threading import StoppableThread
from utils.dbLites.region import *
from utils.dbLites.bnkLite import get as bankGet, dele as bnkDelete
from utils.contains import key
from utils.dbLites.comLite import local_db

class SettingConverterFrame(ttk.Frame):

    def __init__(self, container):
        super().__init__(container)

        self.unit_from = "高德KEY:"
        self.container = container
        self.top = False
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
        self.convert_button = ttk.Button(self, text='Update', state=tk.DISABLED, width=8)
        self.convert_button.grid(column=2, row=0, sticky='w', **options)
        self.convert_button.configure(command=self.convert)

        # button
        self.replace_button = ttk.Button(self, text='替换数据库', width=12)
        self.replace_button.grid(column=3, row=0, sticky='w', **options)
        self.replace_button.configure(command=self.replace)

        # result label
        self.result_label = tk.Text(self, width=48, height=5)
        self.result_label.grid(row=2,column=0, columnspan=4, **{'padx': 5, 'pady': 10})

        self.result_label.insert(tk.END, "因获取地区代码需计流量，付费行为，故停止服务，可以使用替换数据库目录：" + '\n')
        self.result_label.see("end")
        self.result_label.configure(state='disabled')

        # result label
        self.log_label = ttk.Label(self, width=40)
        self.log_label.grid(row=4,column=0,columnspan=4, **options)

        # button
        self.topmost_button = ttk.Button(self, text='置顶界面', width=12)
        self.topmost_button.grid(column=3, row=1, sticky='w', **options)
        self.topmost_button.configure(command=self.topmost)

        # self.pupo = tk.StringVar()
        # self.pupo.set(1)
        # self.bgPupo = ttk.Checkbutton(self, text="关闭时托盘", variable=self.pupo)
        # self.bgPupo.grid(column=2, row=1, sticky='w', **options)

        # add padding to the frame and show it
        self.grid(column=0, row=2, sticky="nsew", **options)

    def topmost(self):
        self.top = not self.top
        self.container.master.attributes("-topmost", self.top)
        if self.top:
            self.topmost_button.config(text="已置顶界面")
        else:
            self.topmost_button.config(text="置顶界面")

    def replace(self, event=None):
        home = os.path.dirname(local_db())
        if os.path.exists(home):
            try:
                self.result_label.configure(state="normal")
                self.result_label.delete('1.0', tk.END)
                self.result_label.insert(tk.END, "数据库目录：" + '\n')
                self.result_label.insert(tk.END, home + '\n')
                self.result_label.see("end")
                self.result_label.configure(state="disabled")
                os.startfile(home)
            except Exception as e:
                print(e)

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
        self.log_label.config(text="数据删除开始...")
        #dele()
        bnkDelete()
        self.log_label.config(text="数据删除完成...")
        self.log_label.config(text="数据更新开始...")
        #get(self.log_label)
        bankGet(self.log_label)
        self.log_label.config(text="Key 无效，请替换数据库！")
        self.log_label.config(text="数据更新完成...")


