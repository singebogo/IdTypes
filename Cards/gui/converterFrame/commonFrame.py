import datetime
import random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

from utils.Calendar import Calendar
from utils.region import select_province_sql, select_city_sql, select_district_sql, select_street_sql


class CommonConverterFrame(ttk.Frame):

    def __init__(self, container):
        super().__init__(container)
        # field options
        options = {'padx': 0, 'pady': 1}

        self.region_frame = ttk.Frame(container)
        self.init_region(**options)
        self.region_frame.grid(column=0, row=0, sticky='w', **options)

        # add padding to the frame and show it
        self.grid(column=0, row=3, padx=0, pady=1, sticky="w")

        self.provinces = select_province_sql()
        self.init_data()

    @staticmethod
    def init_log(self, container, **options):
        self.log_frame = ttk.Frame(container)
        # create Scrollbar
        scrollbar_v = ttk.Scrollbar(self.log_frame)
        scrollbar_v.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_h = ttk.Scrollbar(self.log_frame, orient=tk.HORIZONTAL)
        scrollbar_h.pack(side=tk.BOTTOM, fill=tk.X)
        self.text1 = tk.Text(self.log_frame, width=48, height=18,
                             yscrollcommand=scrollbar_v.set,
                             xscrollcommand=scrollbar_h.set,
                             wrap=tk.NONE)
        self.text1.pack(expand=tk.YES, fill=tk.BOTH)
        scrollbar_v.config(command=self.text1.yview)  # 垂直滚动条绑定text
        scrollbar_h.config(command=self.text1.xview)  # 水平滚动条绑定text
        self.log_frame.grid(column=0, row=2, sticky='w', **options)
        return self.text1

    def init_region(self, **options):
        # 省 label
        self.province_label = ttk.Label(self.region_frame, text="省", width=2)
        self.province_label.grid(column=0, row=0, sticky='w', **options)

        self.province_var = tk.StringVar()
        self.province_com = ttk.Combobox(self.region_frame, textvariable=self.province_var, width=5)
        self.province_com.grid(column=1, row=0, sticky='w', **options)
        self.province_com.bind('<<ComboboxSelected>>', self.province_com_select)

        # 市 label
        self.city_L = ttk.Label(self.region_frame, text="市", width=2)
        self.city_L.grid(column=2, row=0, sticky='w', **options)

        self.city_var = tk.StringVar()
        self.city_com = ttk.Combobox(self.region_frame, textvariable=self.city_var, width=5)
        self.city_com.grid(column=3, row=0, sticky='w', **options)
        self.city_com.bind('<<ComboboxSelected>>', self.city_com_select)

        # 区县 label
        self.district_label = ttk.Label(self.region_frame, text="区县", width=3)
        self.district_label.grid(column=4, row=0, sticky='w', **options)

        self.district_var = tk.StringVar()
        self.district_com = ttk.Combobox(self.region_frame, textvariable=self.district_var, width=5)
        self.district_com.grid(column=5, row=0, sticky='w', **options)
        self.district_com.bind('<<ComboboxSelected>>', self.district_com_select)

        # 街道 label
        self.street_label = ttk.Label(self.region_frame, text="街道", width=3)
        self.street_label.grid(column=6, row=0, sticky='w', **options)

        self.street_var = tk.StringVar()
        self.street_com = ttk.Combobox(self.region_frame, textvariable=self.street_var, width=6)
        self.street_com.grid(column=7, row=0, sticky='w', **options)
        self.street_com.bind('<<ComboboxSelected>>', self.street_com_select)

        # button
        self.convert_button = ttk.Button(self.region_frame, text='☠', width=2)
        self.convert_button.grid(column=8, row=0, sticky='w', **options)
        self.convert_button.configure(command=self.reload)

    def province_com_select(self, even):
        self.update_region()

    def district_com_select(self, even):
        district = self.district_var.get()
        district_index = self.district_com['value'].index(district)
        district_tuple = self.districts[district_index]
        self.streets = select_street_sql(district_tuple[0])

        self.streets = select_street_sql(district_tuple[0])
        if len(self.streets) <= 0:
            self.street_com['value'] = []
            self.street_var.set("")
        else:
            self.street_com['value'] = [street[2] for street in self.streets]
            self.street_com.current(0)

    def street_com_select(self, even):
        self.getadcode()

    def getadcode(self):
        street = self.street_var.get()
        province = self.province_var.get()
        district = self.district_var.get()
        city = self.city_var.get()
        if street:
            index = self.street_com['value'].index(street)
            street_tuple = self.streets[index]
            self.adcode = street_tuple[4]
        elif district:
            distric_index = self.district_com['value'].index(district)
            district_tuple = self.districts[distric_index]
            self.adcode = district_tuple[4]
        elif city:
            city_index = self.city_com['value'].index(city)
            city_tuple = self.citys[city_index]
            self.adcode = city_tuple[4]
        else:
            province_index = self.province_com['value'].index(province)
            province_tuple = self.provinces[province_index]
            self.adcode = province_tuple[4]


    def city_com_select(self, even):
        province = self.province_var.get()
        index = self.province_com['value'].index(province)
        province_tuple = self.provinces[index]
        self.citys = select_city_sql(province_tuple[0])
        if len(self.citys) <= 0:
            self.city_com['value'] = []
            self.district_com['value'] = []
            self.street_com['value'] = []
            self.city_var.set("")
            self.district_var.set("")
            self.street_var.set("")
        else:
            self.city_com['value'] = [city[2] for city in self.citys]
            index_city = self.city_com['value'].index(self.city_var.get())
            city_tuple = self.citys[index_city]
            self.districts = select_district_sql(city_tuple[0])
            if len(self.districts) <= 0:
                self.district_com['value'] = []
                self.street_com['value'] = []
                self.district_var.set("")
                self.street_var.set("")
            else:
                self.district_com['value'] = [district[2] for district in self.districts]
                self.district_com.current(0)

                district = self.district_var.get()
                district_index = self.district_com['value'].index(district)
                district_tuple = self.districts[district_index]
                self.streets = select_street_sql(district_tuple[0])
                if len(self.streets) <= 0:
                    self.street_com['value'] = []
                    self.street_var.set("")
                else:
                    self.street_com['value'] = [street[2] for street in self.streets]
                    self.street_com.current(0)

    def update_region(self):
        province = self.province_var.get()
        index = self.province_com['value'].index(province)
        province_tuple = self.provinces[index]
        self.citys = select_city_sql(province_tuple[0])
        if len(self.citys) <= 0:
            self.city_com['value'] = []
            self.district_com['value'] = []
            self.street_com['value'] = []
            self.city_var.set("")
            self.district_var.set("")
            self.street_var.set("")

            self.districts = select_district_sql(province_tuple[0])
            if(len(self.districts) > 0):
                self.district_com['value'] = [district[2] for district in self.districts]
                self.district_com.current(0)
                district = self.district_var.get()
                district_index = self.district_com['value'].index(district)
                district_tuple = self.districts[district_index]
                self.streets = select_street_sql(district_tuple[0])
                if len(self.streets) <= 0:
                    self.street_com['value'] = []
                    self.street_var.set("")
                else:
                    self.street_com['value'] = [street[2] for street in self.streets]
                    self.street_com.current(0)
        else:
            self.city_com['value'] = [city[2] for city in self.citys]
            self.city_com.current(0)
            index_city = self.city_com['value'].index(self.city_var.get())
            city_tuple = self.citys[index_city]
            self.districts = select_district_sql(city_tuple[0])
            if len(self.districts) <= 0:
                self.district_com['value'] = []
                self.street_com['value'] = []
                self.district_var.set("")
                self.street_var.set("")
            else:
                self.district_com['value'] = [district[2] for district in self.districts]
                self.district_com.current(0)

                district = self.district_var.get()
                district_index = self.district_com['value'].index(district)
                district_tuple = self.districts[district_index]
                self.streets = select_street_sql(district_tuple[0])
                if len(self.streets) <= 0:
                    self.street_com['value'] = []
                    self.street_var.set("")
                else:
                    self.street_com['value'] = [street[2] for street in self.streets]
                    self.street_com.current(0)

    def init_data(self):
        if len(self.provinces) > 0:
            self.province_com['value'] = [province[2] for province in self.provinces]
            self.province_com.current(0)

            province = self.province_var.get()
            index = self.province_com['value'].index(province)
            province_tuple = self.provinces[index]
            self.citys = select_city_sql(province_tuple[0])
            self.city_com['value'] = [city[2] for city in self.citys]
            self.city_com.current(0)

            index_city = self.city_com['value'].index(self.city_var.get())
            city_tuple = self.citys[index_city]
            self.districts = select_district_sql(city_tuple[0])
            self.district_com['value'] = [district[2] for district in self.districts]
            self.district_com.current(0)

            district = self.district_var.get()
            district_index = self.district_com['value'].index(district)
            district_tuple = self.districts[district_index]
            self.streets = select_street_sql(district_tuple[0])
            self.street_com['value'] = [street[2] for street in self.streets]
            self.street_com.current(0)


    def reload(self):
        self.provinces = select_province_sql()
        self.init_data()

