# pyqt5 子功能的界面

import os

from PyQt5 import QtCore, QtWidgets


class BaiduASR(QtWidgets.QWidget):
    # 语音转文字
    version = "v1.0.0"

    def __init__(self, parent, workDir, auths):
        super().__init__()
        self.parent = parent
        self.workDir = workDir
        self.auths = auths
        self.file = ""
        self.__initUI()

    def __initUI(self):
        self.setObjectName("BaiduASR")
        self.setFixedSize(520, 460)  # 固定大小
        self.setWindowTitle("语音转文字")

        self.lineEdit_1 = QtWidgets.QLineEdit(self)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_1.setGeometry(QtCore.QRect(10, 10, 500, 20))
        self.lineEdit_1.setPlaceholderText("文件路径")
        self.lineEdit_1.setReadOnly(True)

        self.groupBox_1 = QtWidgets.QGroupBox(self)
        self.groupBox_1.setGeometry(QtCore.QRect(10, 40, 360, 130))
        self.groupBox_1.setObjectName("groupBox_1")
        self.groupBox_1.setTitle("设定语种")

        self.layoutWidget_1 = QtWidgets.QWidget(self.groupBox_1)
        self.layoutWidget_1.setGeometry(QtCore.QRect(10, 20, 350, 105))
        self.layoutWidget_1.setObjectName("layoutWidget_1")
        self.vLayout_1 = QtWidgets.QVBoxLayout(self.layoutWidget_1)
        self.vLayout_1.setContentsMargins(0, 0, 0, 0)
        self.vLayout_1.setObjectName("vLayout_1")
        self.radio_11 = QtWidgets.QRadioButton(self.layoutWidget_1)
        self.radio_11.setObjectName("radio_11")
        self.radio_11.setText("RadioButton")
        self.radio_12 = QtWidgets.QRadioButton(self.layoutWidget_1)
        self.radio_12.setObjectName("radio_12")
        self.radio_12.setText("RadioButton")
        self.radio_13 = QtWidgets.QRadioButton(self.layoutWidget_1)
        self.radio_13.setObjectName("radio_13")
        self.radio_13.setText("RadioButton")
        self.radio_14 = QtWidgets.QRadioButton(self.layoutWidget_1)
        self.radio_14.setObjectName("radio_14")
        self.radio_14.setText("RadioButton")
        self.radio_15 = QtWidgets.QRadioButton(self.layoutWidget_1)
        self.radio_15.setObjectName("radio_15")
        self.radio_15.setText("RadioButton")
        self.vLayout_1.addWidget(self.radio_11)
        self.vLayout_1.addWidget(self.radio_12)
        self.vLayout_1.addWidget(self.radio_13)
        self.vLayout_1.addWidget(self.radio_14)
        self.vLayout_1.addWidget(self.radio_15)

        self.layoutWidget_2 = QtWidgets.QWidget(self)
        self.layoutWidget_2.setGeometry(QtCore.QRect(400, 40, 100, 120))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.vLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.vLayout_2.setContentsMargins(0, 0, 0, 0)
        self.vLayout_2.setObjectName("vLayout_2")
        self.button_10 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.button_10.setObjectName("button_10")
        self.button_10.setText("选择声音文件")
        self.button_10.clicked.connect(self._choose_file)
        self.button_11 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.button_11.setObjectName("button_11")
        self.button_11.setText("执行转化")
        self.button_11.setEnabled(False)
        self.button_11.clicked.connect(self._get_result)
        self.button_12 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.button_12.setObjectName("button_12")
        self.button_12.setText("返回主界面")
        self.button_12.clicked.connect(self.close)
        self.vLayout_2.addWidget(self.button_10)
        self.vLayout_2.addWidget(self.button_11)
        self.vLayout_2.addWidget(self.button_12)

        self.textBrowser_1 = QtWidgets.QTextBrowser(self)
        self.textBrowser_1.setGeometry(QtCore.QRect(10, 180, 500, 250))
        self.textBrowser_1.setObjectName("textBrowser_1")

    def _choose_file(self):
        self.file, _ = QtWidgets.QFileDialog.getOpenFileName(self,"选择声音文件","C:\\","Sound files (*.wav;*.pcm;*.amr)")
        print(self.file)
        self.lineEdit_1.setText(self.file)
        if os.path.isfile(self.file):
            self.button_11.setEnabled(True)
        else:
            self.button_11.setEnabled(False)

    def _get_result(self):
        pass


class BaiduSynthesis(QtWidgets.QWidget):
    # 文字转语音
    version = "v1.0.0"

    def __init__(self, parent, workDir, auths):
        super().__init__()
        self.parent = parent
        self.workDir = workDir
        self.auths = auths
        self.__initUI()

    def __initUI(self):
        self.setObjectName("BaiduSynthesis")
        self.setFixedSize(520, 400)  # 固定大小
        # self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)  # 禁止最大化
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowTitle("文字转语音")

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setGeometry(QtCore.QRect(10, 10, 500, 12))
        self.label_1.setObjectName("label_1")
        self.label_1.setText("输入文字：")
        self.textBrowser_1 = QtWidgets.QTextBrowser(self)
        self.textBrowser_1.setGeometry(QtCore.QRect(10, 30, 500, 250))
        self.textBrowser_1.setObjectName("textBrowser_1")

        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(10, 300, 55, 12))
        self.label_11.setObjectName("label_11")
        self.label_11.setText("发言人")
        self.comboBox_11 = QtWidgets.QComboBox(self)
        self.comboBox_11.setGeometry(QtCore.QRect(50, 295, 120, 20))
        self.comboBox_11.setObjectName("comboBox_11")
        for i in range(0, 4):
            self.comboBox_11.addItem("")
        self.comboBox_11.setItemText(0, "普通女声音")
        self.comboBox_11.setItemText(1, "普通男声音")
        self.comboBox_11.setItemText(2, "情感合成-度逍遥")
        self.comboBox_11.setItemText(3, "情感合成-度丫丫")

        self.label_12 = QtWidgets.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(190, 300, 30, 12))
        self.label_12.setObjectName("label_12")
        self.label_12.setText("语速")
        self.comboBox_12 = QtWidgets.QComboBox(self)
        self.comboBox_12.setGeometry(QtCore.QRect(220, 295, 65, 20))
        self.comboBox_12.setObjectName("comboBox_12")
        for i in range(0, 16):
            self.comboBox_12.addItem("")
        self.comboBox_12.setItemText(0, "0最慢")
        self.comboBox_12.setItemText(1, "1")
        self.comboBox_12.setItemText(2, "2")
        self.comboBox_12.setItemText(3, "3")
        self.comboBox_12.setItemText(4, "4")
        self.comboBox_12.setItemText(5, "5中速")
        self.comboBox_12.setItemText(6, "6")
        self.comboBox_12.setItemText(7, "7")
        self.comboBox_12.setItemText(8, "8")
        self.comboBox_12.setItemText(9, "9")
        self.comboBox_12.setItemText(10, "10较快")
        self.comboBox_12.setItemText(11, "11")
        self.comboBox_12.setItemText(12, "12")
        self.comboBox_12.setItemText(13, "13")
        self.comboBox_12.setItemText(14, "14")
        self.comboBox_12.setItemText(15, "15最快")

        self.label_13 = QtWidgets.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(300, 300, 30, 12))
        self.label_13.setObjectName("label_13")
        self.label_13.setText("音调")
        self.comboBox_13 = QtWidgets.QComboBox(self)
        self.comboBox_13.setGeometry(QtCore.QRect(330, 295, 65, 20))
        self.comboBox_13.setObjectName("comboBox_13")
        for i in range(0, 16):
            self.comboBox_13.addItem("")
        self.comboBox_13.setItemText(0, "0最低")
        self.comboBox_13.setItemText(1, "1")
        self.comboBox_13.setItemText(2, "2")
        self.comboBox_13.setItemText(3, "3")
        self.comboBox_13.setItemText(4, "4")
        self.comboBox_13.setItemText(5, "5中调")
        self.comboBox_13.setItemText(6, "6")
        self.comboBox_13.setItemText(7, "7")
        self.comboBox_13.setItemText(8, "8")
        self.comboBox_13.setItemText(9, "9")
        self.comboBox_13.setItemText(10, "10较高")
        self.comboBox_13.setItemText(11, "11")
        self.comboBox_13.setItemText(12, "12")
        self.comboBox_13.setItemText(13, "13")
        self.comboBox_13.setItemText(14, "14")
        self.comboBox_13.setItemText(15, "15最高")

        self.label_14 = QtWidgets.QLabel(self)
        self.label_14.setGeometry(QtCore.QRect(410, 300, 30, 12))
        self.label_14.setObjectName("label_14")
        self.label_14.setText("音量")
        self.comboBox_14 = QtWidgets.QComboBox(self)
        self.comboBox_14.setGeometry(QtCore.QRect(440, 295, 65, 20))
        self.comboBox_14.setObjectName("comboBox_14")
        for i in range(0, 16):
            self.comboBox_14.addItem("")
        self.comboBox_14.setItemText(0, "0最低")
        self.comboBox_14.setItemText(1, "1")
        self.comboBox_14.setItemText(2, "2")
        self.comboBox_14.setItemText(3, "3")
        self.comboBox_14.setItemText(4, "4")
        self.comboBox_14.setItemText(5, "5中等")
        self.comboBox_14.setItemText(6, "6")
        self.comboBox_14.setItemText(7, "7")
        self.comboBox_14.setItemText(8, "8")
        self.comboBox_14.setItemText(9, "9")
        self.comboBox_14.setItemText(10, "10较响")
        self.comboBox_14.setItemText(11, "11")
        self.comboBox_14.setItemText(12, "12")
        self.comboBox_14.setItemText(13, "13")
        self.comboBox_14.setItemText(14, "14")
        self.comboBox_14.setItemText(15, "15最响")

        self.layoutWidget_1 = QtWidgets.QWidget(self)
        self.layoutWidget_1.setGeometry(QtCore.QRect(140, 340, 370, 40))
        self.layoutWidget_1.setObjectName("layoutWidget_1")
        self.hLayout_1 = QtWidgets.QHBoxLayout(self.layoutWidget_1)
        self.hLayout_1.setContentsMargins(0, 0, 0, 0)
        self.hLayout_1.setObjectName("hLayout_1")
        self.button_11 = QtWidgets.QPushButton(self.layoutWidget_1)
        self.button_11.setObjectName("button_11")
        self.button_11.setText("试听")
        self.button_11.clicked.connect(self._button_11_clicked)
        self.button_12 = QtWidgets.QPushButton(self.layoutWidget_1)
        self.button_12.setObjectName("button_12")
        self.button_12.setText("保存到文件")
        self.button_12.clicked.connect(self._button_12_clicked)
        self.button_13 = QtWidgets.QPushButton(self.layoutWidget_1)
        self.button_13.setObjectName("button_13")
        self.button_13.setText("返回主界面")
        self.button_13.clicked.connect(self.close)
        self.hLayout_1.addWidget(self.button_11)
        self.hLayout_1.addWidget(self.button_12)
        self.hLayout_1.addWidget(self.button_13)

    def _button_11_clicked(self):
        pass

    def _button_12_clicked(self):
        pass
