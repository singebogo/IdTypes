import random
import tkinter as tk
from tkinter import ttk
from threading import Thread

from gui.converterFrame.commonFrame import CommonConverterFrame
from utils.phones import category, mobie_segment, vritual_segment, iot_segment, \
    satellite_segment, gener, random_phone, \
    paser


class FixedlineTelephoneConverterFrame(ttk.Frame):

    def __init__(self, container, title):
        super().__init__(container)

        self.count = 1

        self.country_code = '0086'
        self.num = 10
        self.btn_index = 0
        self.PHONE_NUM = 11

        self.checkBtns = []
        self.checkboxes = {}  # checkboxes字典则是存储选项是否被选取。
        self.needGener = []
        self.checkboxes_text = {}  # checkboxes字典则是存储选项是否被选取。

        self.company400 = {"4006": "中国联通",
                           "4007": "中国移动原铁通",
                           "4008": "中国电信",
                           "4001": "中国移动新号段",
                           "4000": "中国联通新号段",
                           "4009": "中国电信新号段"}

        # field options
        self.options = {'padx': 0, 'pady': 0}
        self.labelFrame = ttk.LabelFrame(self, text="区域")
        self.region_frame = ttk.Frame(self.labelFrame)
        self.region = CommonConverterFrame(self.region_frame)
        self.region.grid(column=0, row=0, sticky='w', **self.options)
        self.region_frame.grid(column=0, row=0, sticky='w', **self.options)

        self.labelFrame.grid(column=0, row=0, sticky='w', **self.options)

        self.log_frame = ttk.Frame(self)
        self.region.init_log(self.region, self.log_frame, **self.options)

        self.Other_frame = ttk.Frame(self)
        self.init_mobie_segment()
        self.initOther()
        self.Other_frame.grid(column=0, row=self.count, sticky='w', **self.options)

        self.count = self.count + 1
        self.log_frame.grid(column=0, row=self.count, sticky='w', **self.options)

        self.clearAll()
        # add padding to the frame and show it
        self.grid(column=0, row=1, sticky="nsew", **self.options)

    def init_mobie_segment(self):
        lf = ttk.LabelFrame(self.Other_frame, text="400")
        for k, v in self.company400.items():
            self.create_checkbtn(lf, k, k)
        lf.grid(column=0, row=0, sticky='w', **self.options)

    def create_checkbtn(self, container, value, title):
        self.checkboxes[self.btn_index] = tk.BooleanVar()
        self.checkboxes_text[self.btn_index] = tk.StringVar(value=value)
        t = tk.Checkbutton(container, textvariable=self.checkboxes_text[self.btn_index],
                           variable=self.checkboxes[self.btn_index], text=title)
        t.pack(side=tk.LEFT)
        t.select()
        self.checkBtns.append(t)
        self.btn_index = self.btn_index + 1

    def initOther(self):
        self.countryvar = tk.IntVar()
        self.countryvar.set(0)
        self.ck_country = tk.Checkbutton(self.Other_frame, text="国家区号", variable=self.countryvar)
        self.ck_country.grid(row=1, column=0, sticky='w', **self.options)
        self.checkBtns.append(self.ck_country)

        frame = ttk.Frame(self.Other_frame)

        self.num_label = ttk.Label(frame, text="数目:", width=5)
        self.num_label.grid(column=2, row=2, sticky='w', **self.options)
        self.num_var = tk.StringVar()
        self.num_com = ttk.Combobox(frame, textvariable=self.num_var, state='readonly', width=5)
        self.num_com.grid(column=3, row=2, sticky='w', **self.options)
        self.num_com.bind('<<ComboboxSelected>>', self.num_com_select)
        self.num_com['value'] = (10, 50, 100, 500, 1000, 1000, 10000)
        self.num_com.current(0)

        self.all_btn = tk.Button(frame, text='全选', width=4, bg="#DCDCDC",
                                 command=self.all)  # 开始按钮
        self.all_btn.grid(row=2, column=0, sticky='w', **self.options)

        self.clear_all_btn = tk.Button(frame, text='不全选', width=6, bg="#DCDCDC",
                                       command=self.clearAll)  # 开始按钮
        self.clear_all_btn.grid(row=2, column=1, sticky='w', **self.options)

        self.gener_btn = tk.Button(frame, text='生成', width=4, bg="#DCDCDC", command=self.fun)  # 开始按钮
        self.gener_btn.grid(row=2, column=4, sticky='w', **self.options)
        self.clear_btn = tk.Button(frame, text='清空', width=4, bg="#DCDCDC",
                                   command=lambda: self.region.text1.delete('1.0', tk.END))  # 开始按钮
        self.clear_btn.grid(row=2, column=5, sticky='w', **self.options)
        frame.grid(row=2, column=0, sticky='w', **self.options)

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
        self.region.text1.delete('1.0', tk.END)
        self.region.getCityCode()
        self.needGener = []
        for i in range(0, len(self.checkboxes)):
            if self.checkboxes[i].get():
                segments = paser(self.checkboxes_text[i].get())
                for se in segments:
                    self.needGener.append(se)
        self.needGener.append(self.region.citycode)

        for i in range(0, self.num):
            # 固定电话的填写格式是：中国国家长途代码（区号） + 国内地区长途代码（区号） + 电话号码 区号是3-4位数字，号码是6-7位数字
            # 国家码（86）+ 长途区号 + 本地用户号码；
            # 固定网电话号码采用不等位编号，国内有效号码最大位长为11位。
            # 没有区号，全国都可以直接拨打使用，400电话只能接听，不能拨打
            phone = random.choice(self.needGener)
            if phone.startswith('400'):
                phone = phone + "-" + ''.join(random.choices('0123456789', k=self.PHONE_NUM - len(phone)))
            else:
                phone = phone + "-" + ''.join(
                    random.choices('0123456789', k=self.PHONE_NUM - len(phone)))
            if self.countryvar.get() and not phone.startswith('400'):
                self.region.text1.insert(tk.END, self.country_code + "-" + phone + '\n')
            else:
                self.region.text1.insert(tk.END, phone + '\n')
            self.region.text1.see("end")

    def reset(self):
        pass
