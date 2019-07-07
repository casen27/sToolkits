# pyqt5  baiduAI  子功能的界面

import os

from PyQt5 import QtCore, QtWidgets


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

    def __initUI(self):        self.setFixedSize(520, 460)
        self.setWindowTitle("语音转文字")

        self.lineEdit_1 = QtWidgets.QLineEdit(self)        self.lineEdit_1.setGeometry(QtCore.QRect(10, 10, 500, 20))
        self.lineEdit_1.setPlaceholderText("文件路径")
        self.lineEdit_1.setReadOnly(True)

        self.groupBox_1 = QtWidgets.QGroupBox(self)
        self.groupBox_1.setGeometry(QtCore.QRect(10, 40, 360, 130))        self.groupBox_1.setTitle("设定语种")

        self.layout_1 = QtWidgets.QWidget(self.groupBox_1)
        self.layout_1.setGeometry(QtCore.QRect(10, 20, 350, 105))        self.vLayout_1 = QtWidgets.QVBoxLayout(self.layout_1)
        self.vLayout_1.setContentsMargins(0, 0, 0, 0)        self.radio_11 = QtWidgets.QRadioButton(self.layout_1)        self.radio_11.setText("RadioButton")
        self.radio_12 = QtWidgets.QRadioButton(self.layout_1)        self.radio_12.setText("RadioButton")
        self.radio_13 = QtWidgets.QRadioButton(self.layout_1)        self.radio_13.setText("RadioButton")
        self.radio_14 = QtWidgets.QRadioButton(self.layout_1)        self.radio_14.setText("RadioButton")
        self.radio_15 = QtWidgets.QRadioButton(self.layout_1)        self.radio_15.setText("RadioButton")
        self.vLayout_1.addWidget(self.radio_11)
        self.vLayout_1.addWidget(self.radio_12)
        self.vLayout_1.addWidget(self.radio_13)
        self.vLayout_1.addWidget(self.radio_14)
        self.vLayout_1.addWidget(self.radio_15)

        self.layout_2 = QtWidgets.QWidget(self)
        self.layout_2.setGeometry(QtCore.QRect(400, 40, 100, 120))        self.vLayout_2 = QtWidgets.QVBoxLayout(self.layout_2)
        self.vLayout_2.setContentsMargins(0, 0, 0, 0)        self.button_10 = QtWidgets.QPushButton(self.layout_2)        self.button_10.setText("选择声音文件")
        self.button_11 = QtWidgets.QPushButton(self.layout_2)        self.button_11.setText("执行转化")
        self.button_11.setEnabled(False)
        self.button_12 = QtWidgets.QPushButton(self.layout_2)        self.button_12.setText("返回主界面")
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
        self.file, _ = QtWidgets.QFileDialog.getOpenFileName(self,"选择声音文件","","Sound files (*.wav;*.pcm;*.amr)")
        print(self.file)
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

    def __initUI(self):        self.setFixedSize(520, 400)
        self.setWindowTitle("文字转语音")

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setGeometry(QtCore.QRect(10, 10, 500, 12))        self.label_1.setText("输入文字：")
        self.textBrowser_1 = QtWidgets.QTextBrowser(self)
        self.textBrowser_1.setGeometry(QtCore.QRect(10, 30, 500, 250))
        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(10, 300, 55, 12))        self.label_11.setText("发言人")
        self.comboBox_11 = QtWidgets.QComboBox(self)
        self.comboBox_11.setGeometry(QtCore.QRect(50, 295, 120, 20))        self.comboBox_11.addItems(["普通女声音","普通男声音","情感合成-度逍遥","情感合成-度丫丫"])
        self.comboBox_11.setCurrentIndex(0)

        self.label_12 = QtWidgets.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(190, 300, 30, 12))        self.label_12.setText("语速")
        self.comboBox_12 = QtWidgets.QComboBox(self)
        self.comboBox_12.setGeometry(QtCore.QRect(220, 295, 65, 20))        self.comboBox_12.addItems(["0最慢","1","2","3","4","5中速","6","7","8","9","10较快","11","12","13","14","15最快"])
        self.comboBox_12.setCurrentIndex(5)

        self.label_13 = QtWidgets.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(300, 300, 30, 12))        self.label_13.setText("音调")
        self.comboBox_13 = QtWidgets.QComboBox(self)
        self.comboBox_13.setGeometry(QtCore.QRect(330, 295, 65, 20))        self.comboBox_13.addItems(["0最低","1","2","3","4","5中调","6","7","8","9","10较高","11","12","13","14","15最高"])
        self.comboBox_13.setCurrentIndex(5)

        self.label_14 = QtWidgets.QLabel(self)
        self.label_14.setGeometry(QtCore.QRect(410, 300, 30, 12))        self.label_14.setText("音量")
        self.comboBox_14 = QtWidgets.QComboBox(self)
        self.comboBox_14.setGeometry(QtCore.QRect(440, 295, 65, 20))        self.comboBox_14.addItems(["0最低","1","2","3","4","5中响","6","7","8","9","10较响","11","12","13","14","15最响"])
        self.comboBox_14.setCurrentIndex(5)

        self.layout_1 = QtWidgets.QWidget(self)
        self.layout_1.setGeometry(QtCore.QRect(140, 340, 370, 40))        self.hLayout_1 = QtWidgets.QHBoxLayout(self.layout_1)
        self.hLayout_1.setContentsMargins(0, 0, 0, 0)        self.button_11 = QtWidgets.QPushButton(self.layout_1)        self.button_11.setText("试听")
        self.button_12 = QtWidgets.QPushButton(self.layout_1)        self.button_12.setText("保存到文件")
        self.button_13 = QtWidgets.QPushButton(self.layout_1)        self.button_13.setText("返回主界面")
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
