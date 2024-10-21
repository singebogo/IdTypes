import tkinter as tk
from tkinter import ttk
import ctypes

from gui.controlFrame.controlFrame import ControlFrame
from gui.controlFrame.customNotebook import CustomNotebook
from gui.controlFrame.phone_controlFrame import PhoneControlFrame
from gui.converterFrame.settingConverterFrame import SettingConverterFrame


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        img = "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"
        self.title('cards-kxw-singebogo@163.com')
        self.tk.call("wm", "iconphoto", self._w, tk.PhotoImage(data=img))
        self.resizable(False, False)

        # 告诉操作系统使用程序自身的dpi适配
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        # 获取屏幕的缩放因子
        ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
        # 设置程序缩放
        self.tk.call('tk', 'scaling', ScaleFactor / 75)

        self.place_window_center()

        self.init_data()

    def place_window_center(self):
        """Position the toplevel in the center of the screen. Does not
        account for titlebar height."""
        self.update_idletasks()
        w_height = self.winfo_height()
        w_width = self.winfo_width()
        s_height = self.winfo_screenheight()
        s_width = self.winfo_screenwidth()
        xpos = (s_width - w_width) // 2  -100
        ypos = 100
        self.geometry(f'+{xpos}+{ypos}')

    def init_data(self):
        # hotkey win+F10
        self.notebook = ttk.Notebook(self)

        self.idsFrame = ControlFrame(self.notebook)
        self.idsFrame_tab = self.notebook.add(self.idsFrame, text="证件号码")

        self.phoneFrame = PhoneControlFrame(self.notebook)
        self.phoneFrame_tab = self.notebook.add(self.phoneFrame, text="电话号码")

        self.setting = SettingConverterFrame(self.notebook)
        self.setting_tab = self.notebook.add(self.setting, text="设置")

        options = {'padx': 0, 'pady': 1}
        self.notebook.grid(column=0, row=0, sticky='w', **options)
        # 设置选中tab2
        self.notebook.select(self.idsFrame)


if __name__ == '__main__':
    app = App()
    app.mainloop()
