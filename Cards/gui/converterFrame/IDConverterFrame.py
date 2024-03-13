import datetime
import random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

from utils.Calendar import Calendar
from utils.region import select_province_sql, select_city_sql, select_district_sql, select_street_sql
from utils.IDCards import generate_id
from utils.other import Other
from gui.converterFrame.commonFrame import CommonConverterFrame
from gui.converterFrame.OtherConverterFrame import OtherConverterFrame


class IDConverterFrame(ttk.Frame):

    def __init__(self, container, unit_from, converter):
        super().__init__(container)

        self.unit_from = unit_from
        self.converter = converter

        # field options
        options = {'padx': 0, 'pady': 1}

        self.labelFrame = ttk.LabelFrame(self, text="区域")
        self.region_frame = ttk.Frame(self.labelFrame)
        self.region = CommonConverterFrame(self.region_frame)
        self.region.grid(column=1, row=0, sticky='w', **options)
        self.region_frame.grid(column=0, row=0, sticky='w', **options)

        self.data_frame = ttk.Frame(self.labelFrame)
        self.init_date(**options)
        self.data_frame.grid(column=0, row=1, sticky='w', **options)

        self.labelFrame.grid(column=0, row=0, sticky='w', **options)

        self.initOther(**options)

        self.log_frame = ttk.Frame(self)
        self.region.init_log(self.region, self.log_frame, **options)

        self.Other_frame = ttk.Frame(self)
        self.other = OtherConverterFrame(self.Other_frame, self.region.text1)
        self.other.grid(column=0, row=0, sticky='w', **options)
        # button
        self.convert_button = ttk.Button(self.Other_frame, text='身份证', width=8)
        self.convert_button.grid(column=1, row=0, sticky='w', **options)
        self.convert_button.configure(command=self.convert)

        self.clear_btn = ttk.Button(self.Other_frame, text='清空', width=4,
                                    command=lambda: self.region.text1.delete('1.0', tk.END))  # 开始按钮
        self.clear_btn.grid(row=0, column=2, sticky='w', **options)

        self.Other_frame.grid(column=0, row=2, sticky='w', **options)

        self.log_frame.grid(column=0, row=3, sticky='w', **options)

        # add padding to the frame and show it
        self.grid(column=0, row=2, sticky="nsew", **options)

    def initOther(self, **options):
        self.labelOtherFrame = ttk.Frame(self)
        self.labelNameFrame = ttk.LabelFrame(self.labelOtherFrame, text="名称")
        self.selectedNameValue = tk.IntVar()
        ttk.Radiobutton(
            self.labelNameFrame,
            text='中文',
            value=0,
            variable=self.selectedNameValue).grid(column=1, row=0, **options)

        ttk.Radiobutton(
            self.labelNameFrame,
            text='英文',
            value=1,
            variable=self.selectedNameValue).grid(column=2, row=0, **options)

        self.selectedNameValue.set(0)
        self.labelNameFrame.grid(column=0, row=1, sticky='w', **options)

        self.labelAddrFrame = ttk.LabelFrame(self.labelOtherFrame, text="地址")
        self.selectedAddrValue = tk.IntVar()
        ttk.Radiobutton(
            self.labelAddrFrame,
            text='固定',
            value=2,
            variable=self.selectedAddrValue).grid(column=0, row=0, **options)

        ttk.Radiobutton(
            self.labelAddrFrame,
            text='中文',
            value=0,
            variable=self.selectedAddrValue).grid(column=1, row=0, **options)

        ttk.Radiobutton(
            self.labelAddrFrame,
            text='英文',
            value=1,
            variable=self.selectedAddrValue).grid(column=2, row=0, **options)

        self.selectedAddrValue.set(2)
        self.labelAddrFrame.grid(column=1, row=1, sticky='w', **options)

        self.labelOtherFrame.grid(column=0, row=1, sticky='w', **options)


    def init_date(self, **options):
        # 日期 label
        self.calendar_label = ttk.Label(self.data_frame, text="日期", width=4)
        self.calendar_label.grid(column=0, row=1, sticky='w', **options)

        self.date = tk.StringVar()  # 结束日期
        self.date.set(str(datetime.datetime.now().year)
                      + '-' + str(datetime.datetime.now().month).rjust(2, '0')
                      + "-" + str(datetime.datetime.now().day).rjust(2, '0'))
        self.date_entry = ttk.Entry(self.data_frame, textvariable=self.date, width=10)
        self.date_entry.grid(column=1, row=1, sticky='w', **options)
        self.date_entry.focus()
        self.date_btn = ttk.Button(self.data_frame, text='出生日期', width=8, command=lambda: self.getdate())  # 开始按钮
        self.date_btn.grid(row=1, column=2, sticky='w', **options)

        # 性别 label
        self.sex_label = ttk.Label(self.data_frame, text="性别")
        self.sex_label.grid(column=3, row=1, sticky='w', **options)

        self.sex_var = tk.StringVar()
        self.sex_com = ttk.Combobox(self.data_frame, textvariable=self.sex_var, width=2)
        self.sex_com['value'] = ('男', '女')
        self.sex_com.current(0)
        self.sex_com.grid(column=4, row=1, sticky='w', **options)

    def getdate(self):
        x, y = self.date_btn.winfo_pointerxy()

        for date in [Calendar((x - 100, y + 20 )).selection()]:
            if date:
                self.date.set(date)

    def convert(self, event=None):
        """  Handle button click event
        """
        try:
            yearmonthday = self.date.get().replace('-', '')
            sex = self.sex_var.get()
            if sex == '男':
                sexCode = str(random.choice('13579'))
            else:
                sexCode = str(random.choice('2468'))

            self.region.getadcode()
            id = str(generate_id(str(self.region.adcode), yearmonthday, str(sexCode)))
            # 中文名字
            model = self.selectedNameValue.get()
            fake_name = Other(model)

            addrModel = self.selectedAddrValue.get()
            addr = ""
            if addrModel == 2:
                addr = self.region.province_var.get()+self.region.city_var.get()+self.region.district_var.get()+\
                       self.region.street_var.get()+" " + self.region.adcode
            else:
                fake_addr = Other(addrModel)
                addr = fake_addr.address()

            self.region.text1.insert(tk.END, fake_name.name() + " " + id + '\n')
            self.region.text1.insert(tk.END, addr + '\n' + '\n')
            self.region.text1.see("end")

        except ValueError as error:
            showerror(title='Error', message=error)

    def reset(self):
        pass
