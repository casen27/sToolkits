# 主界面

import tkinter

try:
    from .st_config import CONFIG
except Exception:
    from st_config import CONFIG

try:
    from .st_connect import ConnectBaidu
except Exception:
    from st_connect import ConnectBaidu

try:
    from .stui_menu import modifyMenubar
except Exception:
    from stui_menu import modifyMenubar

try:
    from .stui_subs import SubWindow1, SubWindow2, SubWindow4
except Exception:
    from stui_subs import SubWindow1, SubWindow2, SubWindow4


class MainWindow(tkinter.Tk):

    def __init__(self, workDir):
        super().__init__()
        self.workDir = workDir
        self.auths = {}
        self.auth1 = {}
        self.auth2 = {}

        self._get_auths()
        self._init_root()
        self._init_options()
        self._check_auths()

    def _init_root(self):
        # 主窗口
        self.geometry("400x400+400+300")
        self.title("sToolkits —— AI小工具箱")
        # 菜单栏
        menubar = tkinter.Menu(self)
        modifyMenubar(self, menubar, self.workDir, self.auths)

    def _init_options(self):
        # 内容
        self.status1 = tkinter.StringVar()
        self.status2 = tkinter.StringVar()

        self.label1 = tkinter.Label(self, textvariable=self.status1, font=("", 12), )
        self.label1.place(x=10, y=5)

        self.label2 = tkinter.Label(self, textvariable=self.status2, font=("", 12), )
        self.label2.place(x=10, y=30)

        self.sub1 = tkinter.IntVar(self, value=0)
        self.button1 = tkinter.Button(self, text="语音转文字", font=("", 20), command=self._button1_click)
        self.button1.place(x=30, y=80, height=40, width=150)

        self.sub2 = tkinter.IntVar(self, value=0)
        self.button2 = tkinter.Button(self, text="文字转语音", font=("", 20), command=self._button2_click)
        self.button2.place(x=220, y=80, height=40, width=150)

        self.sub3 = tkinter.IntVar(self, value=0)
        self.button3 = tkinter.Button(self, text="功能3", font=("", 20), command=self._button3_click)
        self.button3.place(x=30, y=140, height=40, width=150)

        self.sub4 = tkinter.IntVar(self, value=0)
        self.button4 = tkinter.Button(self, text="语言翻译", font=("", 20), command=self._button4_click)
        self.button4.place(x=220, y=140, height=40, width=150)

    def run(self):
        self.mainloop()

    def fresh_connect(self):
        self._get_auths()
        self._check_auths()

    def _get_auths(self):
        con = CONFIG(workDir=self.workDir)
        self.auths = con.get()
        tokens1 = self.auths["BAIDU_DEFAULT"]
        tokens2 = self.auths["BAIDU_TRANSLATE"]
        self.auth1 = {
                "appid": tokens1["appid"],
                "apikey": tokens1["apikey"],
                "secretkey": tokens1["secretkey"]
                }
        self.auth2 = {
                "appid": tokens2["appid"],
                "secretkey": tokens2["secretkey"]
                }

    def _disable_all(self):
        self.status1.set("语音图文API：无网络或key错误")
        self.status2.set("文字翻译API：无网络或key错误")
        self.button1.config(state=tkinter.DISABLED)
        self.button2.config(state=tkinter.DISABLED)
        self.button3.config(state=tkinter.DISABLED)
        self.button4.config(state=tkinter.DISABLED)

    def _check_auths(self):
        self._disable_all()
        if ConnectBaidu.connect1(self.auth1):
            self.status1.set("语音图文API：已链接")
            # 激活相关功能
            self.button1.config(state=tkinter.ACTIVE)
            self.button2.config(state=tkinter.ACTIVE)
        if ConnectBaidu.connect2(self.auth2):
            self.status2.set("文字翻译API：已链接")
            # 激活相关功能
            self.button4.config(state=tkinter.ACTIVE)

    def _button1_click(self):
        # 功能1：语音转文字
        if self.sub1.get() == 0:
            self.sub1.set(1)
            sw = SubWindow1(self, self.workDir, self.auth1)
            self.button1.wait_window(sw)
            self.sub1.set(0)

    def _button2_click(self):
        # 功能2：文字转语音
        if self.sub2.get() == 0:
            self.sub2.set(1)
            sw = SubWindow2(self, self.workDir, self.auth1)
            self.button2.wait_window(sw)
            self.sub2.set(0)

    def _button3_click(self):
        pass

    def _button4_click(self):
        # 功能4：翻译
        if self.sub4.get() == 0:
            self.sub4.set(1)
            sw = SubWindow4(self, self.workDir, self.auth2)
            self.button4.wait_window(sw)
            self.sub4.set(0)


if __name__ == "__main__":
    pass
