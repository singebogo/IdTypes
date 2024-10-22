import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

from gui.converterFrame.commonFrame import CommonConverterFrame
from utils.iIndustrial import iIndustrialCode
from utils.organization import organizationCode, organizationDigitsCode
from utils.other import Other
from utils.socialCreditCode import SocialCreditCode
from utils.taxRegistration import companyTaxRegistration, TaxRegistration
from utils.taxpayerIdentificationNumber import nsrsbh_15, nsrsbh_18, nsrsbh_20


class GroupConverterFrame(ttk.Frame):

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

        self.labelFrame.grid(column=0, row=0, sticky='w', **options)


        self.initOther(**options)

        self.log_frame = ttk.Frame(self)
        self.region.init_log(self.region, self.log_frame, **options)
        self.log_frame.grid(column=0, row=2, sticky='w', **options)

        # add padding to the frame and show it
        self.grid(column=0, row=1, sticky="nsew", **options)

    def initOther(self, **options):
        self.labelOtherFrame = ttk.Frame(self)

        self.initGroupName(self.labelOtherFrame)
        self.initOganizationName(self.labelOtherFrame)
        self.initTaxpayerId(self.labelOtherFrame)
        self.initTaxRegistration(self.labelOtherFrame)
        frame = ttk.Frame(self.labelOtherFrame)
        # button
        self.clear_btn = tk.Button(frame, text='清空', width=4,  bg="#DCDCDC",
                                   command=lambda: self.region.text1.delete('1.0', tk.END))  # 开始按钮
        self.clear_btn.grid(row=1, column=0, sticky='w', **options)
        frame.grid(column=0, row=5, sticky='w', **options)

        self.labelOtherFrame.grid(column=0, row=1, sticky='w', **options)

    def initGroupName(self, container, **options):
        self.labelFrame = ttk.Frame(container)
        self.labelNameFrame = ttk.LabelFrame(self.labelFrame, text="公司名称")
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

        self.labelCreditCodeFrame = ttk.LabelFrame(self.labelFrame, text="统一社会信用代码模式")
        self.selectedCreditCodeValue = tk.IntVar()
        ttk.Radiobutton(
            self.labelCreditCodeFrame,
            text='固定',
            value=0,
            variable=self.selectedCreditCodeValue).grid(column=1, row=0, **options)

        ttk.Radiobutton(
            self.labelCreditCodeFrame,
            text='随机',
            value=1,
            variable=self.selectedCreditCodeValue).grid(column=2, row=0, **options)

        self.selectedCreditCodeValue.set(0)

        # button
        self.convert_button = tk.Button(self.labelCreditCodeFrame, text='统一社会信用代码',  bg="#DCDCDC", width=15)
        self.convert_button.grid(column=4, row=0, sticky='w', **options)
        self.convert_button.configure(command=self.convert)

        self.labelCreditCodeFrame.grid(column=1, row=1, sticky='w', **options)
        self.labelFrame.grid(column=0, row=1, sticky='w', **options)

    def initOganizationName(self, container, **options):

        self.labelOganizationeFrame = ttk.LabelFrame(container, text="组织机构代码模式")

        self.selectedOganizationValue = tk.IntVar()
        ttk.Radiobutton(
            self.labelOganizationeFrame,
            text='8位数字',
            value=0,
            variable=self.selectedOganizationValue).grid(column=1, row=0, **options)

        ttk.Radiobutton(
            self.labelOganizationeFrame,
            text='大写字母+0-9/X',
            value=1,
            variable=self.selectedOganizationValue).grid(column=2, row=0, **options)

        self.selectedOganizationValue.set(0)

        # button
        self.convert_button = tk.Button(self.labelOganizationeFrame, text='组织机构代码', bg="#DCDCDC", width=12)
        self.convert_button.grid(column=3, row=0, sticky='w', **options)
        self.convert_button.configure(command=self.convertOganization)

        self.labelOganizationeFrame.grid(column=0, row=2, sticky='w', **options)

    def initTaxpayerId(self, container, **options):
        self.labelTaxpayerIdFrame = ttk.LabelFrame(container, text="纳税人识别号模式")

        self.selectedTaxpayerIdValue = tk.IntVar()
        ttk.Radiobutton(
            self.labelTaxpayerIdFrame,
            text='15位',
            value=0,
            variable=self.selectedTaxpayerIdValue).grid(column=0, row=0, **options)

        ttk.Radiobutton(
            self.labelTaxpayerIdFrame,
            text='18位',
            value=1,
            variable=self.selectedTaxpayerIdValue).grid(column=1, row=0, **options)

        ttk.Radiobutton(
            self.labelTaxpayerIdFrame,
            text='20位',
            value=2,
            variable=self.selectedTaxpayerIdValue).grid(column=2, row=0, **options)

        self.selectedTaxpayerIdValue.set(0)

        # button
        self.convert_button = tk.Button(self.labelTaxpayerIdFrame, text='纳税人识别号', bg="#DCDCDC", width=12)
        self.convert_button.grid(column=3, row=0, sticky='w', **options)
        self.convert_button.configure(command=self.convertTaxpayerId)

        self.initIndustrialId(self.labelTaxpayerIdFrame)
        self.labelTaxpayerIdFrame.grid(column=0, row=3, sticky='w', **options)


    def initIndustrialId(self, container, **options):
        frame = ttk.Frame(container)
        # button
        self.convert_button = tk.Button(frame, text='工商注册号', bg="#DCDCDC", width=12)
        self.convert_button.grid(column=0, row=0, sticky='w', **options)
        self.convert_button.configure(command=self.convertIndustrial)
        frame.grid(column=4, row=0, sticky='w', **options)

    def initTaxRegistration(self, container, **options):

        self.labelTaxRegistrationFrame = ttk.LabelFrame(container, text="税务登记号模式")

        self.selectedTaxRegistrationValue = tk.IntVar()
        ttk.Radiobutton(
            self.labelTaxRegistrationFrame,
            text='企业',
            value=0,
            variable=self.selectedTaxRegistrationValue).grid(column=1, row=0, **options)

        ttk.Radiobutton(
            self.labelTaxRegistrationFrame,
            text='个人',
            value=1,
            variable=self.selectedTaxRegistrationValue).grid(column=2, row=0, **options)

        self.selectedTaxRegistrationValue.set(0)

        # button
        self.convert_button = tk.Button(self.labelTaxRegistrationFrame, text='税务登记号', bg="#DCDCDC", width=12)
        self.convert_button.grid(column=3, row=0, sticky='w', **options)
        self.convert_button.configure(command=self.convertTaxRegistration)

        self.labelTaxRegistrationFrame.grid(column=0, row=4, sticky='w', **options)


    def convert(self, event=None):
        """  Handle button click event
        """
        self.region.getadcode()
        code = SocialCreditCode(self.region.adcode).getSocialCode()
        # 中文名字
        model = self.selectedNameValue.get()
        fake_name = Other(model)

        codeModel =  self.selectedCreditCodeValue.get()
        if codeModel:
            fake_code = Other(codeModel)
            self.region.text1.insert(tk.END, fake_name.company() + "  " + fake_code.credit_code() + '\n' + '\n')
        else:
            self.region.text1.insert(tk.END, fake_name.company() + "  " +code + '\n' + '\n')
        self.region.text1.see("end")

    def reset(self):
        pass

    def convertOganization(self, event=None):
        """  Handle button click event
        """

        model = self.selectedNameValue.get()
        fake_name = Other(model)

        oganizationModel = self.selectedOganizationValue.get()
        if oganizationModel == 0:
            self.region.text1.insert(tk.END, fake_name.company() + "  " + organizationDigitsCode() + '\n' + '\n')
        else:
            self.region.text1.insert(tk.END, fake_name.company() + "  " + organizationCode() + '\n' + '\n')
        self.region.text1.see("end")

    def convertTaxpayerId(self, event=None):
        """  Handle button click event
        """
        # 中文名字
        model = self.selectedNameValue.get()
        fake_name = Other(model)

        self.region.getadcode()
        model = self.selectedTaxpayerIdValue.get()
        code = None
        if model == 0:
            code = nsrsbh_15()
        elif model == 1:
            code = nsrsbh_18(self.region.adcode)
        else:
            code = nsrsbh_20(self.region.adcode)

        self.region.text1.insert(tk.END, fake_name.company() + "  " + code + '\n' + '\n')
        self.region.text1.see("end")


    def convertIndustrial(self, event=None):
        # 中文名字
        model = self.selectedNameValue.get()
        fake_name = Other(model)

        self.region.getadcode()
        code = iIndustrialCode(self.region.adcode)

        self.region.text1.insert(tk.END, fake_name.company() + "  " + code + '\n' + '\n')
        self.region.text1.see("end")


    def convertTaxRegistration(self, event=None):
        # 中文名字
        model = self.selectedNameValue.get()
        fake_name = Other(model)

        self.region.getadcode()

        model = self.selectedTaxRegistrationValue.get()
        if model == 0:
            code = companyTaxRegistration(self.region.adcode)
            self.region.text1.insert(tk.END, fake_name.company() + "  " + code + '\n' + '\n')
        else:
            code = TaxRegistration(self.region.adcode)
            self.region.text1.insert(tk.END, fake_name.name() + "  " + code + '\n' + '\n')
        self.region.text1.see("end")