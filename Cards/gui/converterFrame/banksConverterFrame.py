import tkinter as tk
import random
from threading import Thread
from tkinter import ttk
import tkinter.font as tkfont

from utils.banks import MII, getLastcode
from utils.dbLites.bnkLite import *


class BanksConverterFrame(ttk.LabelFrame):
    def __init__(self, container):
        super().__init__(container)
        # field options
        options = {'padx': 0, 'pady': 1}
        self['text'] = '银行Bin'

        self.btn_index = 0
        self.num = 10
        self.checkBtns = []
        self.checkboxes = {}  # checkboxes字典则是存储选项是否被选取。
        self.needGener = []
        self.checkboxes_text = {}  # checkboxes字典则是存储选项是否被选取。

        self.MII_btn_index = 0
        self.MII_checkboxes = {}  # checkboxes字典则是存储选项是否被选取。
        self.MII_checkBtns = []
        self.MII_needGener = []
        self.MII_checkboxes_text = {}  # checkboxes字典则是存储选项是否被选取。

        self.ctype_btn_index = 0
        self.ctype_checkboxes = {}  # checkboxes字典则是存储选项是否被选取。
        self.ctype_checkBtns = []
        self.ctype_needGener = []
        self.ctype_checkboxes_text = {}  # checkboxes字典则是存储选项是否被选取。

        self.region_frame = ttk.Frame(self)
        self.init_region(**options)
        self.region_frame.grid(column=0, row=0, sticky='w', **options)
        self.banks_frame = ttk.Frame(self)
        self.init_banks(**options)
        self.banks_frame.grid(column=0, row=1, sticky='w', **options)
        self.Other_frame = ttk.Frame(self)
        # self.init_mobie_segment()
        self.initOther(**options)
        self.Other_frame.grid(column=0, row=2, sticky='w', **options)
        self.init_log(**options)

        # add padding to the frame and show it
        self.grid(column=0, row=3, padx=0, pady=1, sticky="w")

        self.provinces = select_province_sql()
        self.init_data()

    def on_combo_configure(self, event):
        combo = event.widget
        style = ttk.Style()
        # check if the combobox already has the "postoffest" property
        current_combo_style = combo.cget('style') or "TCombobox"
        if len(style.lookup(current_combo_style, 'postoffset')) > 0:
            return
        combo_values = combo.cget('values')
        if len(combo_values) == 0:
            return
        longest_value = max(combo_values, key=len)
        font = tkfont.nametofont(str(combo.cget('font')))
        width = font.measure(longest_value + "0") - event.width
        if (width < 0):
            # no need to make the popdown smaller
            return
        # create an unique style name using widget's id
        unique_name = 'Combobox{}'.format(combo.winfo_id())
        # the new style must inherit from curret widget style (unless it's our custom style!)
        if unique_name in current_combo_style:
            style_name = current_combo_style
        else:
            style_name = "{}.{}".format(unique_name, current_combo_style)

        style.configure(style_name, postoffset=(0, 0, width, 0))
        combo.configure(style=style_name)

    def init_banks(self, **options):
        MIIFrame = ttk.LabelFrame(self.banks_frame, text="行业标识")
        self.MII_list = [item for item in MII.items()]
        self.MII_group_list = [self.MII_list[i:i + 3] for i in range(0, len(self.MII_list), 3)]
        for i in range(len(self.MII_group_list)):
            f = tk.Frame(MIIFrame)
            for j in self.MII_group_list[i]:
                self.create_MII_checkbtn(f, j[0], j[1])
            f.pack(side=tk.TOP)
        MIIFrame.grid(column=0, row=0, sticky='w', **options)

        # 卡类型
        self.card_type = select_card_type_sql()
        card_typeFrame = ttk.LabelFrame(self.banks_frame, text="卡类型")
        card_typeFrame.grid(column=0, row=1, sticky='w', **options)
        for i in self.card_type:
            self.create_ctype_checkbtn(card_typeFrame, i[0], i[0])

        self.banks = select_all_banks_sql()
        lf = ttk.LabelFrame(self.banks_frame, text="国内银行")
        self.banks_list = [self.banks[i:i + 4] for i in range(0, len(self.banks), 4)]
        for i in range(len(self.banks_list)):
            f = tk.Frame(lf)
            for item in self.banks_list[i]:
                self.create_checkbtn(f, item[0], item[1])
            f.pack(side=tk.TOP)
        lf.grid(column=0, row=2, sticky='w', **options)

    def create_checkbtn(self, container, value, title):
        self.checkboxes[self.btn_index] = tk.BooleanVar()
        self.checkboxes_text[self.btn_index] = tk.StringVar(value=title)
        t = tk.Checkbutton(container, textvariable=title,
                           variable=self.checkboxes[self.btn_index], text=title)
        t.pack(side=tk.LEFT)
        t.select()
        self.checkBtns.append(t)
        self.btn_index = self.btn_index + 1

    def create_ctype_checkbtn(self, container, value, title):
        self.ctype_checkboxes[self.ctype_btn_index] = tk.BooleanVar()
        self.ctype_checkboxes_text[self.ctype_btn_index] = tk.StringVar(value=value)
        t = tk.Checkbutton(container, textvariable=title,
                           variable=self.ctype_checkboxes[self.ctype_btn_index], text=title)
        t.pack(side=tk.LEFT)
        t.select()
        self.ctype_checkBtns.append(t)
        self.ctype_btn_index = self.ctype_btn_index + 1

    def create_MII_checkbtn(self, container, value, title):
        self.MII_checkboxes[self.MII_btn_index] = tk.BooleanVar()
        self.MII_checkboxes_text[self.MII_btn_index] = tk.StringVar(value=value)
        t = tk.Checkbutton(container, textvariable=title,
                           variable=self.MII_checkboxes[self.MII_btn_index], text=title)
        t.pack(side=tk.LEFT)
        t.select()
        self.MII_checkBtns.append(t)
        self.MII_btn_index = self.MII_btn_index + 1

    def initOther(self, **options):
        frame = ttk.Frame(self.Other_frame)
        self.countryvar = tk.IntVar()
        self.countryvar.set(1)
        self.ck_country = tk.Checkbutton(frame, text="固定", variable=self.countryvar)
        self.ck_country.grid(row=0, column=0, sticky='w', **options)
        self.num_label = ttk.Label(frame, text="数目:", width=5)
        self.num_label.grid(column=3, row=0, sticky='w', **options)
        self.num_var = tk.StringVar()
        self.num_com = ttk.Combobox(frame, textvariable=self.num_var, state='readonly', width=5)
        self.num_com.grid(column=4, row=0, sticky='w', **options)
        self.num_com.bind('<<ComboboxSelected>>', self.num_com_select)
        self.num_com['value'] = (10, 50, 100, 500, 1000, 1000, 10000)
        self.num_com.current(0)

        self.all_btn = tk.Button(frame, text='全选', width=4, bg="#DCDCDC",
                                 command=self.all)  # 开始按钮
        self.all_btn.grid(row=0, column=1, sticky='w', **options)

        self.clear_all_btn = tk.Button(frame, text='不全选', width=6, bg="#DCDCDC",
                                       command=self.clearAll)  # 开始按钮
        self.clear_all_btn.grid(row=0, column=2, sticky='w', **options)

        self.gener_btn = tk.Button(frame, text='生成', width=4, bg="#DCDCDC", command=self.fun)  # 开始按钮
        self.gener_btn.grid(row=0, column=5, sticky='w', **options)
        self.clear_btn = tk.Button(frame, text='清空', width=4, bg="#DCDCDC",
                                   command=lambda: self.text1.delete('1.0', tk.END))  # 开始按钮
        self.clear_btn.grid(row=0, column=6, sticky='w', **options)
        frame.grid(row=2, column=0, sticky='w', **options)

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
        global card_info
        self.text1.delete('1.0', tk.END)
        self.getbankcode()

        for i in range(0, len(self.MII_checkboxes)):
            if self.MII_checkboxes[i].get():
                self.MII_needGener.append(self.MII_checkboxes_text[i].get())
        for i in range(0, len(self.ctype_checkboxes)):
            if self.ctype_checkboxes[i].get():
                self.ctype_needGener.append(self.ctype_checkboxes_text[i].get())
        # 无选择则默认 9
        if len(self.MII_needGener) < 0:
            self.MII_needGener.append('9')
        if len(self.ctype_needGener) < 0:
            self.ctype_needGener.append(random.choice(self.ctype_checkboxes_text).get())
        if not self.countryvar.get():
            #  获取国内银行
            self.needGener = []
            for i in range(0, len(self.checkboxes)):
                if self.checkboxes[i].get():
                    bin = self.checkboxes_text[i].get()
                    self.needGener.append(bin)

        for i in range(0, self.num):
            mii = random.choice(self.MII_needGener)
            if self.countryvar.get():
                # 固定
                # 获取当前银行具体信息
                bank_name = self.bank_var.get()
                if '其他银行' in bank_name:
                    subbank = self.subbank_var.get()
                    if subbank:
                        index = self.subbank_com['value'].index(subbank)
                        subbank_tuple = self.subbanks[index]
                        bank_name = subbank_tuple[1]
                        if str(bank_name).find('银行') != -1:
                            bank_name = bank_name.split('银行')[0] + '银行'
                card_info = select_card_sql(bank_name)
            else:
                # 国内银行
                bank_name = random.choice(self.needGener)
                if '其他银行' in bank_name:
                    banks = [i if '其他银行' not in i else i for i in self.needGener]
                    card_info = select_random_card_sql(banks, self.ctype_needGener)
                else:
                    ctype = random.choice(self.ctype_needGener)
                    if str(bank_name).find('中国') != -1:
                        bank_name = str(bank_name).replace('中国', '')
                    if '农村合作信用社' in bank_name:
                        bank_name = '农村信用社'
                    card_info = select_card_bytype_sql(bank_name, ctype)
                    # 出现银行无ctype类型，则随机获取
                    card_info = select_card_sql(bank_name)

            if not card_info or len(card_info) == 0:
                self.text1.insert(tk.END, bank_name + '\n')
                head = mii + self.subbankCode
                if len(head) > 15:
                    head = head[:15]
                self.text1.insert(tk.END, "   无维护BIN数据，随机生成账号: " + head + getLastcode(head) + '\n' + '\n')
                self.text1.see("end")
            else:
                issuing_bank, len1, Bin, BIN_len, card_type, card_name = card_info[0]
                need_len = int(len1) - int(BIN_len) - 1
                area_code = self.subbankCode[:8]
                need = area_code + "".join(random.choices('0123456789', k=need_len - len(area_code)))

                self.text1.insert(tk.END, issuing_bank + "  长度：" + len1 + "  " + card_type + "  " + card_name + '\n')
                self.text1.insert(tk.END, Bin + need + getLastcode(Bin + need) + '\n' + '\n')
                self.text1.see("end")

    def init_region(self, **options):
        # 省 label
        self.province_label = ttk.Label(self.region_frame, text="省", width=2)
        self.province_label.grid(column=0, row=0, sticky='w', **options)

        self.province_var = tk.StringVar()
        self.province_com = ttk.Combobox(self.region_frame, textvariable=self.province_var, state='readonly', width=5)
        self.province_com.grid(column=1, row=0, sticky='w', **options)
        self.province_com.bind('<<ComboboxSelected>>', self.province_com_select)

        # 市 label
        self.city_L = ttk.Label(self.region_frame, text="市", width=2)
        self.city_L.grid(column=2, row=0, sticky='w', **options)

        self.city_var = tk.StringVar()
        self.city_com = ttk.Combobox(self.region_frame, textvariable=self.city_var, state='readonly', width=5)
        self.city_com.grid(column=3, row=0, sticky='w', **options)
        self.city_com.bind('<<ComboboxSelected>>', self.city_com_select)

        # 区县 label
        self.bank_label = ttk.Label(self.region_frame, text="区县", width=3)
        self.bank_label.grid(column=4, row=0, sticky='w', **options)

        self.bank_var = tk.StringVar()
        self.bank_com = ttk.Combobox(self.region_frame, textvariable=self.bank_var, state='readonly', width=5)
        self.bank_com.grid(column=5, row=0, sticky='w', **options)
        self.bank_com.bind('<Configure>', self.on_combo_configure)
        self.bank_com.bind('<<ComboboxSelected>>', self.bank_com_select)

        # 街道 label
        self.subbank_label = ttk.Label(self.region_frame, text="街道", width=3)
        self.subbank_label.grid(column=6, row=0, sticky='w', **options)

        self.subbank_var = tk.StringVar()
        self.subbank_com = ttk.Combobox(self.region_frame, textvariable=self.subbank_var, justify=tk.CENTER,
                                        state='readonly', width=8)
        self.subbank_com.grid(column=7, row=0, sticky='w', **options)
        self.subbank_com.bind('<Configure>', self.on_combo_configure)
        self.subbank_com.bind('<<ComboboxSelected>>', self.subbank_com_select)

        # button
        # 使用PhotoImage函数导入图像
        self.convert_button = tk.Button(self.region_frame, text="加载", bg="#DCDCDC", width=4)
        self.convert_button.grid(column=8, row=0, sticky='w', **options)
        self.convert_button.configure(command=self.reload)

    def subbank_com_select(self, even):
        self.getbankcode()

    def getbankcode(self):
        subbank = self.subbank_var.get()
        if subbank:
            index = self.subbank_com['value'].index(subbank)
            subbank_tuple = self.subbanks[index]
            self.subbankCode = subbank_tuple[0]

    def bank_com_select(self, even):
        index_city = self.city_com['value'].index(self.city_var.get())
        city_tuple = self.citys[index_city]
        bank = self.bank_var.get()
        bank_index = self.bank_com['value'].index(bank)
        bank_tuple = self.banks[bank_index]
        self.subbanks = select_subbanks_sql(bank_tuple[0], city_tuple[0])

        if len(self.subbanks) <= 0:
            self.subbank_com['value'] = []
            self.subbank_var.set("")
        else:
            self.subbank_com['value'] = [self.skeletonize(subbank[1]) for subbank in self.subbanks]
            self.subbank_com.current(0)

    def skeletonize(self, text):
        return text
        # if str(text).find('银行') != -1:
        #     text = text.split('银行')[1]
        # return text.replace('股份有限公司', '')

    def city_com_select(self, even):
        province = self.province_var.get()
        index = self.province_com['value'].index(province)
        province_tuple = self.provinces[index]
        self.citys = select_city_sql(province_tuple[0])
        if len(self.citys) <= 0:
            self.city_com['value'] = []
            self.bank_com['value'] = []
            self.subbank_com['value'] = []
            self.city_var.set("")
            self.bank_var.set("")
            self.subbank_var.set("")
        else:
            self.city_com['value'] = [city[1] for city in self.citys]
            index_city = self.city_com['value'].index(self.city_var.get())
            city_tuple = self.citys[index_city]
            self.banks = select_banks_sql(city_tuple[0])
            if len(self.banks) <= 0:
                self.bank_com['value'] = []
                self.subbank_com['value'] = []
                self.bank_var.set("")
                self.subbank_var.set("")
            else:
                self.bank_com['value'] = [bank[1] for bank in self.banks]
                self.bank_com.current(0)

                bank = self.bank_var.get()
                bank_index = self.bank_com['value'].index(bank)
                bank_tuple = self.banks[bank_index]
                self.subbanks = select_subbanks_sql(bank_tuple[0], city_tuple[0])
                if len(self.subbanks) <= 0:
                    self.subbank_com['value'] = []
                    self.subbank_var.set("")
                else:
                    self.subbank_com['value'] = [self.skeletonize(subbank[1]) for subbank in self.subbanks]
                    self.subbank_com.current(0)

    def province_com_select(self, even):
        self.update_region()

    def update_region(self):
        province = self.province_var.get()
        index = self.province_com['value'].index(province)
        province_tuple = self.provinces[index]
        self.citys = select_city_sql(province_tuple[0])
        if len(self.citys) <= 0:
            self.city_com['value'] = []
            self.bank_com['value'] = []
            self.subbank_com['value'] = []
            self.city_var.set("")
            self.bank_var.set("")
            self.subbank_var.set("")

            self.banks = select_banks_sql(province_tuple[0])
            if (len(self.banks) > 0):
                self.bank_com['value'] = [bank[1] for bank in self.banks]
                self.bank_com.current(0)
                bank = self.bank_var.get()
                bank_index = self.bank_com['value'].index(bank)
                bank_tuple = self.banks[bank_index]
                self.subbanks = select_subbanks_sql(bank_tuple[0], "")
                if len(self.subbanks) <= 0:
                    self.subbank_com['value'] = []
                    self.subbank_var.set("")
                else:
                    self.subbank_com['value'] = [self.skeletonize(subbank[1]) for subbank in self.subbanks]
                    self.subbank_com.current(0)
        else:
            self.city_com['value'] = [city[1] for city in self.citys]
            self.city_com.current(0)
            index_city = self.city_com['value'].index(self.city_var.get())
            city_tuple = self.citys[index_city]
            self.banks = select_banks_sql(city_tuple[0])
            if len(self.banks) <= 0:
                self.bank_com['value'] = []
                self.subbank_com['value'] = []
                self.bank_var.set("")
                self.subbank_var.set("")
            else:
                self.bank_com['value'] = [bank[1] for bank in self.banks]
                self.bank_com.current(0)

                bank = self.bank_var.get()
                bank_index = self.bank_com['value'].index(bank)
                bank_tuple = self.banks[bank_index]
                self.subbanks = select_subbanks_sql(bank_tuple[0], city_tuple[0])
                if len(self.subbanks) <= 0:
                    self.subbank_com['value'] = []
                    self.subbank_var.set("")
                else:
                    self.subbank_com['value'] = [self.skeletonize(subbank[1]) for subbank in self.subbanks]
                    self.subbank_com.current(0)

    def init_log(self, **options):
        self.log_frame = ttk.Frame(self)
        # create Scrollbar
        scrollbar_v = ttk.Scrollbar(self.log_frame)
        scrollbar_v.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_h = ttk.Scrollbar(self.log_frame, orient=tk.HORIZONTAL)
        scrollbar_h.pack(side=tk.BOTTOM, fill=tk.X)
        self.text1 = tk.Text(self.log_frame, width=50, height=20,
                             yscrollcommand=scrollbar_v.set,
                             xscrollcommand=scrollbar_h.set,
                             wrap=tk.NONE)
        self.text1.tag_configure("tag_name", justify='center')
        self.text1.pack(expand=tk.YES, fill=tk.BOTH)
        scrollbar_v.config(command=self.text1.yview)  # 垂直滚动条绑定text
        scrollbar_h.config(command=self.text1.xview)  # 水平滚动条绑定text
        self.log_frame.grid(column=0, row=3, sticky='w', **options)
        return self.text1

    def init_data(self):
        if len(self.provinces) > 0:
            self.province_com['value'] = [province[1] for province in self.provinces]
            self.province_com.current(0)

            province = self.province_var.get()
            index = self.province_com['value'].index(province)
            province_tuple = self.provinces[index]
            self.citys = select_city_sql(province_tuple[0])
            self.city_com['value'] = [city[1] for city in self.citys]
            self.city_com.current(0)

            index_city = self.city_com['value'].index(self.city_var.get())
            city_tuple = self.citys[index_city]
            self.banks = select_banks_sql(city_tuple[0])
            self.bank_com['value'] = [bank[1] for bank in self.banks]
            self.bank_com.current(0)

            bank = self.bank_var.get()
            bank_index = self.bank_com['value'].index(bank)
            bank_tuple = self.banks[bank_index]
            self.subbanks = select_subbanks_sql(bank_tuple[0], city_tuple[0])
            self.subbank_com['value'] = [self.skeletonize(subbank[1]) for subbank in self.subbanks]
            self.subbank_com.current(0)

    def reload(self):
        self.provinces = select_province_sql()
        self.init_data()

    def reset(self):
        pass
