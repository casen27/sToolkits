# 菜单栏的全部配置

import tkinter
import webbrowser
from tkinter.messagebox import askyesno, showinfo

try:
    from .st_config import CONFIG
except Exception:
    from st_config import CONFIG

try:
    from .st_settings import BAIDU_AI
except Exception:
    from st_settings import BAIDU_AI


class MenuBase(object):

    def __init__(self, root, workDir, auths):
        self.root = root
        self.workDir = workDir
        self.auths = auths


class MenuSetting(MenuBase):

    def __init__(self, root, workDir, auths):
        super().__init__(root, workDir, auths)

    def set_keys(self):
        skw = SetKeysWindow(self.root, self.workDir, self.auths)
        skw.run()

    def quit(self):
        entry = askyesno(title="退出", message="确认退出？")
        if entry is True:
            self.root.destroy()


class MenuHelp(MenuBase):

    def __init__(self, root, workDir, auths):
        super().__init__(root, workDir, auths)

    def about(self):
        showinfo(title="关于", message="关于小工具的一些说明")


def modifyMenubar(root, menubar, workDir, auths):
    # 设置
    menu = tkinter.Menu(menubar, tearoff=0)
    ms = MenuSetting(root, workDir, auths)
    menu.add_command(label="配置Key", command=ms.set_keys)
    menu.add_separator()
    menu.add_command(label="退出", command=ms.quit)
    menubar.add_cascade(label="设置", menu=menu)

    # 帮助
    menu = tkinter.Menu(menubar, tearoff=0)
    mh = MenuHelp(root, workDir, auths)
    menu.add_command(label="关于", command=mh.about)
    menubar.add_cascade(label="帮助", menu=menu)

    # 总集成
    root.config(menu=menubar)


class SetKeysWindow(tkinter.Toplevel):

    def __init__(self, root, workDir, auths):
        super().__init__()
        self.root = root
        self.workDir = workDir
        self.auths = auths

        self.title("语音转文字")
        self.geometry("500x400+550+100")
        self.attributes("-topmost", 1)

        self.label01 = tkinter.Label(self, text="语音转文字、文字转语音、图片OCR", font=("", 12), )
        self.label01.place(x=10, y=10)

        self.label02 = tkinter.Label(self, text="appId", font=("", 12), )
        self.label02.place(x=20, y=40)

        self.str02 = tkinter.StringVar()
        self.text02 = tkinter.Entry(self, textvariable=self.str02, font=("", 12), width=40)
        self.text02.place(x=100, y=40)

        self.label03 = tkinter.Label(self, text="apiKey", font=("", 12), )
        self.label03.place(x=20, y=70)

        self.str03 = tkinter.StringVar()
        self.text03 = tkinter.Entry(self, textvariable=self.str03, font=("", 12), width=40)
        self.text03.place(x=100, y=70)

        self.label04 = tkinter.Label(self, text="secretKey", font=("", 12), )
        self.label04.place(x=20, y=100)

        self.str04 = tkinter.StringVar()
        self.text04 = tkinter.Entry(self, textvariable=self.str04, font=("", 12), width=40)
        self.text04.place(x=100, y=100)

        self.label11 = tkinter.Label(self, text="翻译", font=("", 12), )
        self.label11.place(x=10, y=150)

        self.label12 = tkinter.Label(self, text="apiId", font=("", 12), )
        self.label12.place(x=20, y=180)

        self.str12 = tkinter.StringVar()
        self.text12 = tkinter.Entry(self, textvariable=self.str12, font=("", 12), width=40)
        self.text12.place(x=100, y=180)

        self.label13 = tkinter.Label(self, text="secretKey", font=("", 12), )
        self.label13.place(x=20, y=210)

        self.str13 = tkinter.StringVar()
        self.text13 = tkinter.Entry(self, textvariable=self.str13, font=("", 12), width=40)
        self.text13.place(x=100, y=210)

        self.button1 = tkinter.Button(self, text="申请key", font=("", 20), command=self.get_baidu_ai)
        self.button1.place(x=50, y=300, height=40, width=150)

        self.button2 = tkinter.Button(self, text="保存", font=("", 20), command=self.save)
        self.button2.place(x=250, y=300, height=40, width=150)
        # self.button1.config(state=tkinter.DISABLED)

    def run(self):
        self.str02.set(self.auths["BAIDU_DEFAULT"]["appid"])
        self.str03.set(self.auths["BAIDU_DEFAULT"]["apikey"])
        self.str04.set(self.auths["BAIDU_DEFAULT"]["secretkey"])
        self.str12.set(self.auths["BAIDU_TRANSLATE"]["appid"])
        self.str13.set(self.auths["BAIDU_TRANSLATE"]["secretkey"])
        self.mainloop()

    def save(self):
        self.auths["BAIDU_DEFAULT"]["appid"] = self.str02.get()
        self.auths["BAIDU_DEFAULT"]["apikey"] = self.str03.get()
        self.auths["BAIDU_DEFAULT"]["secretkey"] = self.str04.get()
        self.auths["BAIDU_TRANSLATE"]["appid"] = self.str12.get()
        self.auths["BAIDU_TRANSLATE"]["secretkey"] = self.str13.get()
        con = CONFIG(workDir=self.workDir)
        con.save(self.auths)

        self.root.fresh_connect()
        self.destroy()

    def get_baidu_ai(self):
        webbrowser.open(BAIDU_AI)


if __name__ == '__main__':
    pass
