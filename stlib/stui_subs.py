# 子功能的界面

import os
import time
import tkinter
from tkinter import ttk
from tkinter.filedialog import askopenfilename

try:
    from .st_connect import ASR, Synthesis
except Exception:
    from st_connect import ASR, Synthesis


class SubWindow1(tkinter.Toplevel):
    # 功能1：语音转文字

    def __init__(self, root, workDir, auths):
        super().__init__()
        self.root = root
        self.workDir = workDir
        self.auths = auths
        self.asr = None

        self.title("语音转文字")
        self.geometry("800x600+550+100")
        # self.attributes("-topmost", 1)

        self.fullpath = ""
        self.string = ""

        self.text1 = tkinter.Text(self, font=("", 15), width=60, height=1)
        self.text1.place(x=20, y=20)

        self.button1 = tkinter.Button(self, text="选择语音文件", font=("", 15), command=self._button1_click)
        self.button1.place(x=650, y=10, height=30)

        self.button2 = tkinter.Button(self, text="转换文字", font=("", 15), command=self._button2_click)
        self.button2.place(x=650, y=50, height=30)

        self.text2 = tkinter.Text(self, font=("", 15), width=75, height=22)
        self.text2.place(x=20, y=100)

    def run(self):
        self.mainloop()

    def _button1_click(self):
        self.fullpath = askopenfilename(filetypes=(("Sound Files", "*.wav;*.pcm;*.amr"),))
        self.text1.delete(0.0, tkinter.END)
        self.text1.insert(tkinter.INSERT, self.fullpath)
        self.text2.delete(0.0, tkinter.END)

    def _button2_click(self):
        if self.fullpath:
            self.asr = ASR(self.workDir, self.fullpath, self.auths)
        if self.asr:
            self.string = self.asr.run()
        else:
            self.string = "（错误：未选择声音文件！）"
        self.text2.delete(0.0, tkinter.END)
        self.text2.insert(tkinter.INSERT, self.string)


class SubWindow2(tkinter.Toplevel):
    # 功能1：文字转语音

    def __init__(self, root, workDir, auths):
        super().__init__()
        self.root = root
        self.workDir = workDir
        self.auths = auths
        self.options = {}

        self.strdate = ""
        self.sound = None

        self.title("文字转语音")
        self.geometry("800x550+550+100")
        # self.attributes("-topmost", 1)

        self.text1 = tkinter.Text(self, font=("", 15), width=75, height=22)
        self.text1.place(x=20, y=20)

        self.label1 = tkinter.Label(self, text="发言人", font=("", 12), )
        self.label1.place(x=20, y=500)

        self.cv1 = tkinter.IntVar()
        self.cbox1 = ttk.Combobox(self, textvariable=self.cv1, width=13, state='readonly')
        # per  选填  发音人选择, 0为普通女声，1为普通男生，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女声
        self.cbox1["values"] = ("普通女声", "普通男生", "情感合成-度逍遥", "情感合成-度丫丫")
        self.cbox1.current(0)
        # self.cbox1.bind("<<ComboboxSelected>>", self._cbselected1)
        self.cbox1.place(x=80, y=500)

        self.label2 = tkinter.Label(self, text="语速", font=("", 12), )
        self.label2.place(x=210, y=500)

        self.cv2 = tkinter.IntVar()
        self.cbox2 = ttk.Combobox(self, textvariable=self.cv2, width=6, state='readonly')
        # spd  选填  语速，取值0-15，默认为5中语速
        self.cbox2["values"] = ("0最慢", "1", "2", "3", "4", "5中速", "6", "7", "8", "9", "10较快", "11", "12", "13", "14", "15最快")
        self.cbox2.current(5)
        self.cbox2.place(x=250, y=500)

        self.label3 = tkinter.Label(self, text="音调", font=("", 12), )
        self.label3.place(x=330, y=500)

        self.cv3 = tkinter.IntVar()
        self.cbox3 = ttk.Combobox(self, textvariable=self.cv3, width=6, state='readonly')
        # pit  选填  音调，取值0-15，默认为5中语调
        self.cbox3["values"] = ("0最低", "1", "2", "3", "4", "5中调", "6", "7", "8", "9", "10较高", "11", "12", "13", "14", "15最尖")
        self.cbox3.current(5)
        self.cbox3.place(x=370, y=500)

        self.label4 = tkinter.Label(self, text="音量", font=("", 12), )
        self.label4.place(x=450, y=500)

        self.cv4 = tkinter.IntVar()
        self.cbox4 = ttk.Combobox(self, textvariable=self.cv4, width=6, state='readonly')
        # vol  选填  音量，取值0-15，默认为5中音量
        self.cbox4["values"] = ("0最低", "1", "2", "3", "4", "5中音", "6", "7", "8", "9", "10较响", "11", "12", "13", "14", "15最响")
        self.cbox4.current(5)
        self.cbox4.place(x=490, y=500)

        self.button1 = tkinter.Button(self, text="获取", font=("", 12), command=self._button1_click)
        self.button1.place(x=570, y=500, height=30, width=80)

        self.button2 = tkinter.Button(self, text="储存", font=("", 12), command=self._button2_click)
        self.button2.place(x=670, y=500, height=30, width=80)
        self.button2.config(state=tkinter.DISABLED)

    def _get_options(self):
        self.options = {}
        per = self.cbox1.current()
        if per == 0:
            self.options["per"] = 0
        elif per == 1:
            self.options["per"] = 1
        elif per == 2:
            self.options["per"] = 3
        elif per == 3:
            self.options["per"] = 4
        self.options["spd"] = self.cbox2.current()
        self.options["pit"] = self.cbox3.current()
        self.options["vol"] = self.cbox4.current()

    def _button1_click(self):
        # 获取声音
        self._get_options()
        self.strdate = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        sy = Synthesis(auths=self.auths, text=self.text1.get(0.0, tkinter.END), options=self.options)
        self.sound = sy.run()
        # TODO 播放声音
        # text1 改变，抑制掉button2
        self.button2.config(state=tkinter.ACTIVE)

    def _button2_click(self):
        # 储存声音文件
        file = self.strdate + ".mp3"
        fullpath = os.path.join(self.workDir, file)
        if not isinstance(self.sound, dict):
            with open(fullpath, 'wb') as fp:
                fp.write(self.sound)

    def run(self):
        self.mainloop()


class SubWindow4(tkinter.Toplevel):
    # 功能4：文字转语音

    def __init__(self, root, workDir, auths):
        super().__init__()
        self.root = root
        self.workDir = workDir
        self.auths = auths
        self.params = {}

        self.title("语言翻译")
        self.geometry("800x550+550+100")
        self.attributes("-topmost", 1)


if __name__ == "__main__":
    pass
