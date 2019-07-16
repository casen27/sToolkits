# baidu  子功能的界面

import os

from PySide2 import QtCore, QtWidgets, QtGui

from .st_baidu import BaiduASR, BaiduSynthesis, BaiduTranslate


class BaiduASRUI(QtWidgets.QWidget):
    # 语音转文字
    version = "1.0.0"

    def __init__(self, workDir, auths):
        super().__init__()
        self.workDir = workDir
        self.auths = auths
        self.file = ""

        self.__initUI()
        self.__initActions()
        self.__initDatas()

    def __initUI(self):
        self.setFixedSize(520, 460)
        self.setWindowTitle("语音转文字")

        self.lineEdit_1 = QtWidgets.QLineEdit(self)
        self.lineEdit_1.setGeometry(QtCore.QRect(10, 10, 500, 20))
        self.lineEdit_1.setPlaceholderText("文件路径")
        self.lineEdit_1.setReadOnly(True)

        self.groupBox_1 = QtWidgets.QGroupBox(self)
        self.groupBox_1.setGeometry(QtCore.QRect(10, 40, 360, 130))
        self.groupBox_1.setTitle("设定语种")

        self.layout_1 = QtWidgets.QWidget(self.groupBox_1)
        self.layout_1.setGeometry(QtCore.QRect(10, 20, 350, 105))
        self.vLayout_1 = QtWidgets.QVBoxLayout(self.layout_1)
        self.vLayout_1.setContentsMargins(0, 0, 0, 0)
        self.radio_11 = QtWidgets.QRadioButton(self.layout_1)
        self.radio_11.setText("RadioButton")
        self.radio_12 = QtWidgets.QRadioButton(self.layout_1)
        self.radio_12.setText("RadioButton")
        self.radio_13 = QtWidgets.QRadioButton(self.layout_1)
        self.radio_13.setText("RadioButton")
        self.radio_14 = QtWidgets.QRadioButton(self.layout_1)
        self.radio_14.setText("RadioButton")
        self.radio_15 = QtWidgets.QRadioButton(self.layout_1)
        self.radio_15.setText("RadioButton")
        self.vLayout_1.addWidget(self.radio_11)
        self.vLayout_1.addWidget(self.radio_12)
        self.vLayout_1.addWidget(self.radio_13)
        self.vLayout_1.addWidget(self.radio_14)
        self.vLayout_1.addWidget(self.radio_15)

        self.layout_2 = QtWidgets.QWidget(self)
        self.layout_2.setGeometry(QtCore.QRect(400, 40, 100, 120))
        self.vLayout_2 = QtWidgets.QVBoxLayout(self.layout_2)
        self.vLayout_2.setContentsMargins(0, 0, 0, 0)
        self.button_10 = QtWidgets.QPushButton(self.layout_2)
        self.button_10.setText("选择声音文件")
        self.button_11 = QtWidgets.QPushButton(self.layout_2)
        self.button_11.setText("执行转化")
        self.button_11.setEnabled(False)
        self.button_12 = QtWidgets.QPushButton(self.layout_2)
        self.button_12.setText("返回主界面")
        self.vLayout_2.addWidget(self.button_10)
        self.vLayout_2.addWidget(self.button_11)
        self.vLayout_2.addWidget(self.button_12)

        self.textBrowser_1 = QtWidgets.QTextBrowser(self)
        self.textBrowser_1.setGeometry(QtCore.QRect(10, 180, 500, 250))

    def __initActions(self):
        self.button_10.clicked.connect(self._choose_file)
        self.button_11.clicked.connect(self._get_result)
        self.button_12.clicked.connect(self.close)

    def __initDatas(self):
        pass

    def _choose_file(self):
        self.file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "选择声音文件", "", "Sound files (*.wav;*.pcm;*.amr)")
        # print(self.file)
        self.lineEdit_1.setText(self.file)
        if os.path.isfile(self.file):
            self.button_11.setEnabled(True)
        else:
            self.button_11.setEnabled(False)

    def _get_result(self):
        pass


class BaiduSynthesisUI(QtWidgets.QWidget):
    # 文字转语音
    version = "1.0.0"

    def __init__(self, workDir, auths):
        super().__init__()
        self.workDir = workDir
        self.auths = auths

        self.__initUI()
        self.__initActions()
        self.__initDatas()

    def __initUI(self):
        self.setFixedSize(520, 400)
        self.setWindowTitle("文字转语音")

        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 500, 12))
        self.label_11.setText("输入文字：")
        self.textBrowser_1 = QtWidgets.QTextBrowser(self)
        self.textBrowser_1.setGeometry(QtCore.QRect(10, 30, 500, 250))

        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(10, 300, 55, 12))
        self.label_11.setText("发言人")
        self.comboBox_11 = QtWidgets.QComboBox(self)
        self.comboBox_11.setGeometry(QtCore.QRect(50, 295, 120, 20))
        self.comboBox_11.addItems(["普通女声音", "普通男声音", "情感合成-度逍遥", "情感合成-度丫丫"])
        self.comboBox_11.setCurrentIndex(0)

        self.label_12 = QtWidgets.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(190, 300, 30, 12))
        self.label_12.setText("语速")
        self.comboBox_12 = QtWidgets.QComboBox(self)
        self.comboBox_12.setGeometry(QtCore.QRect(220, 295, 65, 20))
        self.comboBox_12.addItems(["0最慢", "1", "2", "3", "4", "5中速", "6", "7", "8", "9", "10较快", "11", "12", "13", "14", "15最快"])
        self.comboBox_12.setCurrentIndex(5)

        self.label_13 = QtWidgets.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(300, 300, 30, 12))
        self.label_13.setText("音调")
        self.comboBox_13 = QtWidgets.QComboBox(self)
        self.comboBox_13.setGeometry(QtCore.QRect(330, 295, 65, 20))
        self.comboBox_13.addItems(["0最低", "1", "2", "3", "4", "5中调", "6", "7", "8", "9", "10较高", "11", "12", "13", "14", "15最高"])
        self.comboBox_13.setCurrentIndex(5)

        self.label_14 = QtWidgets.QLabel(self)
        self.label_14.setGeometry(QtCore.QRect(410, 300, 30, 12))
        self.label_14.setText("音量")
        self.comboBox_14 = QtWidgets.QComboBox(self)
        self.comboBox_14.setGeometry(QtCore.QRect(440, 295, 65, 20))
        self.comboBox_14.addItems(["0最低", "1", "2", "3", "4", "5中响", "6", "7", "8", "9", "10较响", "11", "12", "13", "14", "15最响"])
        self.comboBox_14.setCurrentIndex(5)

        self.layout_1 = QtWidgets.QWidget(self)
        self.layout_1.setGeometry(QtCore.QRect(140, 340, 370, 40))
        self.hLayout_1 = QtWidgets.QHBoxLayout(self.layout_1)
        self.hLayout_1.setContentsMargins(0, 0, 0, 0)
        self.button_11 = QtWidgets.QPushButton(self.layout_1)
        self.button_11.setText("试听")
        self.button_12 = QtWidgets.QPushButton(self.layout_1)
        self.button_12.setText("保存到文件")
        self.button_13 = QtWidgets.QPushButton(self.layout_1)
        self.button_13.setText("返回主界面")
        self.hLayout_1.addWidget(self.button_11)
        self.hLayout_1.addWidget(self.button_12)
        self.hLayout_1.addWidget(self.button_13)

    def __initActions(self):
        self.button_11.clicked.connect(self._button_11_clicked)
        self.button_12.clicked.connect(self._button_12_clicked)
        self.button_13.clicked.connect(self.close)

    def __initDatas(self):
        pass

    def _button_11_clicked(self):
        pass

    def _button_12_clicked(self):
        pass


class BaiduTranslateUI(QtWidgets.QWidget):
    version = "1.0.5"
    # signal_1 = QtCore.Signal()
    # signal_2 = QtCore.Signal(int)
    # self.signal_1.emit()
    fromlang_support = [
                        ("auto","自动识别"),
                        ("en","英语"),
                        ("zh","简体中文"),
                        ("cht","繁体中文"),
                        ]
    tolang_support = [
                        ("zh","简体中文"),
                        ("en","英语"),
                        ("cht","繁体中文"),
                        ("jp","日语"),
                        ("fra","法语"),
                        ("spa","西班牙语"),
                        ("ru","俄语"),
                        ]
    fromlang = "auto"
    tolang = "zh"
    _return = 0
    text_original = ""
    text_result = ""

    def __init__(self, workDir, auths):
        super().__init__()
        self.workDir = workDir
        self.auths = auths

        self.__initUI()
        self.__initActions()
        self.__initDatas()

    def __initUI(self):
        self.setFixedSize(640, 700)
        self.setWindowTitle("百度翻译")

        self.groupBox_1 = QtWidgets.QGroupBox(self)
        self.groupBox_1.setGeometry(QtCore.QRect(10, 10, 620, 280))
        self.groupBox_1.setObjectName("groupBox_1")
        self.groupBox_1.setTitle("原文")
        self.text_11 = QtWidgets.QTextEdit(self.groupBox_1)
        self.text_11.setGeometry(QtCore.QRect(10, 15, 600, 220))
        self.text_11.setObjectName("text_11")
        self.text_11.setFont(QtGui.QFont("", 12))
        self.label_11 = QtWidgets.QLabel(self.groupBox_1)
        self.label_11.setGeometry(QtCore.QRect(10, 245, 75, 25))
        self.label_11.setObjectName("label_11")
        self.label_11.setText("指定语种")
        self.comboBox_11 = QtWidgets.QComboBox(self.groupBox_1)
        self.comboBox_11.setGeometry(QtCore.QRect(70, 245, 75, 25))
        self.comboBox_11.setObjectName("comboBox_11")
        for k,v in self.fromlang_support:
            self.comboBox_11.addItem(v)
        self.button_11 = QtWidgets.QPushButton(self.groupBox_1)
        self.button_11.setGeometry(QtCore.QRect(400, 245, 75, 25))
        self.button_11.setObjectName("button_11")
        self.button_11.setText("清空")
        self.button_12 = QtWidgets.QPushButton(self.groupBox_1)
        self.button_12.setGeometry(QtCore.QRect(500, 245, 75, 25))
        self.button_12.setObjectName("button_12")
        self.button_12.setText("读取剪切板")

        self.button_1 = QtWidgets.QPushButton(self)
        self.button_1.setGeometry(QtCore.QRect(270, 300, 75, 30))
        self.button_1.setObjectName("button_1")
        self.button_1.setFont(QtGui.QFont("", 16))
        self.button_1.setText("翻译")

        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 340, 620, 280))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setTitle("译文")

        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        self.label_21.setGeometry(QtCore.QRect(10, 15, 75, 25))
        self.label_21.setObjectName("label_21")
        self.label_21.setText("目标语种")
        self.comboBox_21 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_21.setGeometry(QtCore.QRect(70, 15, 75, 25))
        self.comboBox_21.setObjectName("comboBox_21")
        for k,v in self.tolang_support:
            self.comboBox_21.addItem(v)
        self.label_22 = QtWidgets.QLabel(self.groupBox_2)
        self.label_22.setGeometry(QtCore.QRect(200, 15, 75, 25))
        self.label_22.setObjectName("label_22")
        self.label_22.setText("结果展示")
        self.comboBox_22 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_22.setGeometry(QtCore.QRect(260, 15, 75, 25))
        self.comboBox_22.setObjectName("comboBox_22")
        self.comboBox_22.addItems(["仅译文", "json全部"])

        self.button_21 = QtWidgets.QPushButton(self.groupBox_2)
        self.button_21.setGeometry(QtCore.QRect(400, 15, 75, 25))
        self.button_21.setObjectName("button_21")
        self.button_21.setText("清空")
        self.button_22 = QtWidgets.QPushButton(self.groupBox_2)
        self.button_22.setGeometry(QtCore.QRect(500, 15, 75, 25))
        self.button_22.setObjectName("button_22")
        self.button_22.setText("写入剪切板")
        self.text_21 = QtWidgets.QTextEdit(self.groupBox_2)
        self.text_21.setGeometry(QtCore.QRect(10, 50, 600, 220))
        self.text_21.setObjectName("text_21")
        self.text_21.setFont(QtGui.QFont("", 12))

        self.timer_1 = QtCore.QTimer(self)

    def __initActions(self):
        self.button_1.clicked.connect(self._button_1_clicked)
        self.button_11.clicked.connect(self._button_11_clicked)
        self.button_12.clicked.connect(self._button_12_clicked)
        self.button_21.clicked.connect(self._button_21_clicked)
        self.button_22.clicked.connect(self._button_22_clicked)
        self.comboBox_11.activated.connect(self._cbox_1_changed)
        self.comboBox_21.activated.connect(self._cbox_2_changed)
        self.comboBox_22.activated.connect(self._cbox_3_changed)
        self.timer_1.timeout.connect(self._timer_1_out)

    def __initDatas(self):
        self.text_11.setText(self.text_original)
        self.text_21.setText(self.text_result)

    def _cbox_1_changed(self):
        index = self.comboBox_11.currentIndex()
        self.fromlang = self.fromlang_support[index][0]

    def _cbox_2_changed(self):
        index = self.comboBox_21.currentIndex()
        self.tolang = self.tolang_support[index][0]

    def _cbox_3_changed(self):
        index = self.comboBox_22.currentIndex()
        self._return = index

    def _button_1_clicked(self):
        # 执行翻译
        # 获取界面参数 （text必须有值）
        text = self.text_11.toPlainText()
        if text:
            self.params = {
                "from":self.fromlang,
                "to":self.tolang,
                "text":text,
                "_return":self._return,
                }
            self.text_21.clear()
            self.timer_1.start(1000)
        else:
            QtWidgets.QMessageBox.critical(self, "警告", "\n\n原文为空！\n\n")

    def _timer_1_out(self):
        # 发送请求
        bt = BaiduTranslate(auths=self.auths,params=self.params)
        self.text_result = bt.run()

        # 结果展示
        self.text_21.setText(self.text_result)
        self.timer_1.stop()

    def _button_11_clicked(self):
        # 清空原文文本
        self.text_original = ""
        self.text_11.setText(self.text_original)

    def _button_12_clicked(self):
        # 读取剪切板（检测剪切板数据是否为字符串）
        clipboard = QtWidgets.QApplication.clipboard()
        content = clipboard.text()
        if isinstance(content, str):
            self.text_original = content
        else:
            self.text_original = ""
        self.text_11.setText(self.text_original)

    def _button_21_clicked(self):
        # 清空翻译文本
        self.text_result = ""
        self.text_21.setText(self.text_result)

    def _button_22_clicked(self):
        # 翻译后的结果写入剪切板
        text = self.text_21.toPlainText()
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(text)
        QtWidgets.QMessageBox.about(self, "提示", "\n\n结果已经复制到剪切板中\n\n")
