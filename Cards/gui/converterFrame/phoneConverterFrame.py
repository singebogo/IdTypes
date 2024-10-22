import random
import tkinter as tk
from tkinter import ttk
from threading import Thread

from gui.converterFrame.commonFrame import CommonConverterFrame
from utils.phones import category, mobie_segment, vritual_segment, iot_segment, \
    satellite_segment, gener, random_phone, \
    paser


class PhoneConverterFrame(ttk.Frame):

    def __init__(self, container, title):
        super().__init__(container)

        self.count = 1
        self.btn_index = 0

        self.num = 10
        self.checkBtns = []
        self.checkboxes = {}  # checkboxes字典则是存储选项是否被选取。
        self.needGener = []
        self.checkboxes_text = {}  # checkboxes字典则是存储选项是否被选取。

        # field options
        self.options = {'padx': 0, 'pady': 0}

        self.labelFrame = ttk.LabelFrame(self, text=title)
        self.init_mobie_segment()
        self.init_other_segment(vritual_segment, "虚拟号码段", True)
        self.init_other_segment(iot_segment, "物联网号码段")
        self.init_other_segment(satellite_segment, "卫星电话号段")
        self.labelFrame.grid(column=0, row=0, sticky='w', **self.options)

        frame = ttk.Frame(self)
        self.count = self.count + 1
        self.num_label = ttk.Label(frame, text="数目:", width=5)
        self.num_label.grid(column=2, row=0, sticky='w', **self.options)
        self.num_var = tk.StringVar()
        self.num_com = ttk.Combobox(frame, textvariable=self.num_var, state='readonly', width=5)
        self.num_com.grid(column=3, row=0, sticky='w', **self.options)
        self.num_com.bind('<<ComboboxSelected>>', self.num_com_select)
        self.num_com['value'] = (10, 50, 100, 500, 1000, 1000, 10000)
        self.num_com.current(0)

        # button

        self.all_btn = tk.Button(frame, text='全选', width=4, bg="#DCDCDC",
                                    command=self.all)  # 开始按钮
        self.all_btn.grid(row=0, column=0, sticky='w', **self.options)

        self.clear_all_btn = tk.Button(frame, text='不全选', width=6, bg="#DCDCDC",
                                    command=self.clearAll)  # 开始按钮
        self.clear_all_btn.grid(row=0, column=1, sticky='w', **self.options)

        self.gener_btn = tk.Button(frame, text='生成', width=4, bg="#DCDCDC", command=self.fun)  # 开始按钮
        self.gener_btn.grid(row=0, column=4, sticky='w', **self.options)
        self.clear_btn = tk.Button(frame, text='清空', width=4, bg="#DCDCDC",
                                    command=lambda: self.text1.delete('1.0', tk.END))  # 开始按钮
        self.clear_btn.grid(row=0, column=5, sticky='w', **self.options)

        frame.grid(column=0, row=self.count, sticky='w', **self.options)

        self.count = self.count + 1
        self.frame = ttk.Frame(self)
        self.init_log(self.frame, **self.options)
        self.frame.grid(column=0, row=self.count, sticky='w', **self.options)

        # add padding to the frame and show it
        self.grid(column=0, row=1, sticky="nsew", **self.options)


    def clearAll(self):
        for btn in self.checkBtns:
            btn.deselect()

    def all(self):
        for btn in self.checkBtns:
            btn.select()

    def num_com_select(self, *args):
        self.num = int(self.num_var.get())

    def fun(self):
        t = Thread(target=self.target, args=(), daemon=True)
        t.start()

    def target(self):
        self.text1.delete('1.0', tk.END)
        self.needGener = []
        for i in range(0, len(self.checkboxes)):
            if self.checkboxes[i].get():
                segments = paser(self.checkboxes_text[i].get())
                for se in segments:
                    self.needGener.append(se)

        # 判断是否有充足的数据
        if not len(self.needGener):
            for i in range(0, self.num):
                self.text1.insert(tk.END, random_phone() + '\n')
                self.text1.see("end")
        else:
            if int(self.num) > len(self.needGener):
                phones = self.needGener
                # 循环生成
                for ins in range(0, self.num, len(self.needGener)):
                    for needse in self.needGener:
                        self.text1.insert(tk.END, gener(needse) + '\n')
                        self.text1.see("end")
            else:
                phones = random.choices(self.needGener, k=int(self.num))
                for needse in phones:
                    self.text1.insert(tk.END, gener(needse) + '\n')
                    self.text1.see("end")


    def init_log(self, container, **options):
        self.log_frame = ttk.Frame(container)
        # create Scrollbar
        scrollbar_v = ttk.Scrollbar(self.log_frame)
        scrollbar_v.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_h = ttk.Scrollbar(self.log_frame, orient=tk.HORIZONTAL)
        scrollbar_h.pack(side=tk.BOTTOM, fill=tk.X)
        self.text1 = tk.Text(self.log_frame, width=50, height=10,
                             yscrollcommand=scrollbar_v.set,
                             xscrollcommand=scrollbar_h.set,
                             wrap=tk.NONE)
        self.text1.tag_configure("tag_name", justify='center')
        self.text1.pack(expand=tk.YES, fill=tk.BOTH)
        scrollbar_v.config(command=self.text1.yview)  # 垂直滚动条绑定text
        scrollbar_h.config(command=self.text1.xview)  # 水平滚动条绑定text
        self.log_frame.grid(column=0, row=0, sticky='w', **options)
        return self.text1

    def init_mobie_segment(self):
        keys = [k for k in mobie_segment.keys()]
        for i in range(0, len(keys)):
            lf = ttk.LabelFrame(self.labelFrame, text=keys[i])
            self.init_every_category_detail(lf, mobie_segment.get(keys[i]))
            lf.grid(column=0, row=i, sticky='w', **self.options)
            self.count = self.count + 1

    def init_every_category_detail(self, container, item):
        for i in item:
            if isinstance(i, list):
                f = tk.Frame(container)
                for c in i:
                    self.create_checkbtn(f, c)
                f.pack(side=tk.TOP)
            else:
                self.create_checkbtn(container, i)

    def create_checkbtn(self, container, text):
        self.checkboxes[self.btn_index] = tk.BooleanVar()
        self.checkboxes_text[self.btn_index] = tk.StringVar(value=text)
        t = tk.Checkbutton(container, textvariable=self.checkboxes_text[self.btn_index],
                           variable=self.checkboxes[self.btn_index], text=text)
        t.pack(side=tk.LEFT)
        t.select()
        self.checkBtns.append(t)
        self.btn_index = self.btn_index + 1

    def init_other_segment(self, dict, title, flag=False):
        self.count = self.count + 1
        labelFrame = ttk.LabelFrame(self, text=title)
        labelFrame.grid(column=0, row=self.count, sticky='w', **self.options)
        keys = [k for k in dict.keys()]
        row = 0
        col = 0
        for i in range(0, len(keys)):
            self.count = self.count + 1
            lf = ttk.LabelFrame(labelFrame, text=keys[i])
            self.init_every_category_detail(lf, dict.get(keys[i]))
            if flag:
                if i % 2 == 0:
                    row = row + 1
                    col = 0
                else:
                    col = col + 1
            else:
                col = i
            lf.grid(column=col, row=row, sticky='w', **self.options)

    def reset(self):
        pass
