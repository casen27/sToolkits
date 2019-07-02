# pyqt5 主界面

import sys

from PyQt5 import QtCore, QtWidgets

from .st_config import CONFIG
from .st_baiduai import ConnectBaidu
from .st_qtui_menu import HelpAbout, SettingKeys
from .st_qtui_baidu import BaiduASR, BaiduSynthesis
from .st_qtui_tools import ColorBoard


class MainWindow(QtWidgets.QMainWindow):
    version = "v1.0.0"

    def __init__(self, workDir):
        super().__init__()
        self.workDir = workDir
        self.auths = {}
        self.auth1 = {}
        self.auth2 = {}

        self._get_auths()
        self.__initUI()
        self.__initMenu()
        self.__initFuncs()
        self._check_auths()

    def __initUI(self):
        self.setObjectName("MainWindow")
        self.setFixedSize(420, 280)  # 固定大小
        # self.setWindowFlags(Qt.WindowMinimizeButtonHint)  # 禁止最大化
        self.setWindowTitle("小工具集")

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 23))
        self.menubar.setObjectName("menubar")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.statusBar().showMessage('准备就绪')

    def __initMenu(self):
        self.menu_setting = QtWidgets.QMenu(self.menubar)
        self.menu_setting.setObjectName("menu_setting")
        self.menu_setting.setTitle("设置")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        self.menu_help.setTitle("帮助")

        self.setMenuBar(self.menubar)

        self.menu_setting_keys = QtWidgets.QAction(self)
        self.menu_setting_keys.setObjectName("menu_setting_keys")
        self.menu_setting_keys.setText("设置Keys")
        self.menu_setting_keys.triggered.connect(self._menu_setting_keys_triggered)
        self.menu_setting_exit = QtWidgets.QAction(self)
        self.menu_setting_exit.setObjectName("menu_setting_exit")
        self.menu_setting_exit.setText("退出")
        self.menu_setting_exit.triggered.connect(QtWidgets.qApp.quit)
        self.menu_help_about = QtWidgets.QAction(self)
        self.menu_help_about.setObjectName("menu_help_about")
        self.menu_help_about.setText("关于")
        self.menu_help_about.triggered.connect(self._menu_help_about_triggered)

        self.menu_setting.addAction(self.menu_setting_keys)
        self.menu_setting.addSeparator()
        self.menu_setting.addAction(self.menu_setting_exit)
        self.menu_help.addAction(self.menu_help_about)

        self.menubar.addAction(self.menu_setting.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

    def __initFuncs(self):
        self.layoutWidget_1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_1.setGeometry(QtCore.QRect(10, 5, 400, 40))
        self.layoutWidget_1.setObjectName("layoutWidget_1")
        self.vLayout_1 = QtWidgets.QVBoxLayout(self.layoutWidget_1)
        self.vLayout_1.setContentsMargins(0, 0, 0, 0)
        self.vLayout_1.setObjectName("vLayout_1")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_1)
        self.label_11.setObjectName("label_11")
        self.label_11.setText("检测状态1")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget_1)
        self.label_12.setObjectName("label_12")
        self.label_12.setText("检测状态2")
        self.vLayout_1.addWidget(self.label_11)
        self.vLayout_1.addWidget(self.label_12)

        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 60, 400, 120))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gLayout_1 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gLayout_1.setContentsMargins(0, 0, 0, 0)
        self.gLayout_1.setObjectName("gLayout_1")

        self.button_11 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.button_11.setObjectName("button_11")
        self.button_11.setText("语音转文字")
        self.button_11.setEnabled(False)
        self.button_11.clicked.connect(self._button_11_clicked)
        self.button_12 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.button_12.setObjectName("button_12")
        self.button_12.setText("文字转语音")
        self.button_12.setEnabled(False)
        self.button_12.clicked.connect(self._button_12_clicked)
        self.button_13 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.button_13.setObjectName("button_13")
        self.button_13.setText("功能3")
        self.button_13.setEnabled(False)
        self.button_14 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.button_14.setObjectName("button_14")
        self.button_14.setText("翻译")
        self.button_14.setEnabled(False)
        self.button_15 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.button_15.setObjectName("button_15")
        self.button_15.setText("功能5")
        self.button_15.setEnabled(False)
        self.button_16 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.button_16.setObjectName("button_16")
        self.button_16.setText("功能6")
        self.button_16.setEnabled(False)
        self.button_17 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.button_17.setObjectName("button_17")
        self.button_17.setText("功能7")
        self.button_17.setEnabled(False)
        self.button_18 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.button_18.setObjectName("button_18")
        self.button_18.setText("功能8")
        self.button_18.setEnabled(False)
        self.button_19 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.button_19.setObjectName("button_19")
        self.button_19.setText("功能9")
        self.button_19.setEnabled(True)
        self.button_19.clicked.connect(self._button_19_clicked)

        self.gLayout_1.addWidget(self.button_11, 0, 0, 1, 1)
        self.gLayout_1.addWidget(self.button_12, 0, 1, 1, 1)
        self.gLayout_1.addWidget(self.button_13, 0, 2, 1, 1)
        self.gLayout_1.addWidget(self.button_14, 1, 0, 1, 1)
        self.gLayout_1.addWidget(self.button_15, 1, 1, 1, 1)
        self.gLayout_1.addWidget(self.button_16, 1, 2, 1, 1)
        self.gLayout_1.addWidget(self.button_17, 2, 0, 1, 1)
        self.gLayout_1.addWidget(self.button_18, 2, 1, 1, 1)
        self.gLayout_1.addWidget(self.button_19, 2, 2, 1, 1)

        self.button_01 = QtWidgets.QPushButton(self.centralwidget)
        self.button_01.setGeometry(QtCore.QRect(300, 200, 100, 23))
        self.button_01.setObjectName("button_01")
        self.button_01.setText("退出")
        self.button_01.clicked.connect(QtWidgets.qApp.quit)

        self.setCentralWidget(self.centralwidget)

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
        self.label_11.setText("语音图文API：无网络或key错误")
        self.label_12.setText("文字翻译API：无网络或key错误")
        self.button_11.setEnabled(False)
        self.button_12.setEnabled(False)
        self.button_13.setEnabled(False)
        self.button_14.setEnabled(False)
        self.button_15.setEnabled(False)
        self.button_16.setEnabled(False)
        self.button_17.setEnabled(False)
        self.button_18.setEnabled(False)

    def _check_auths(self):
        self._disable_all()
        if ConnectBaidu.connect1(self.auth1):
            self.label_11.setText("语音图文API：已链接")
            # 激活相关功能
            self.button_11.setEnabled(True)
            self.button_12.setEnabled(True)
        if ConnectBaidu.connect2(self.auth2):
            self.label_12.setText("文字翻译API：已链接")
            # 激活相关功能
            self.button_14.setEnabled(True)

    def _fresh_connect(self):
        self._get_auths()
        self._check_auths()

    def _menu_setting_keys_triggered(self):
        self._ui_setting_keys = SettingKeys(workDir=self.workDir, auths=self.auths)
        self._ui_setting_keys.signal.connect(self._fresh_connect)
        self._ui_setting_keys.show()

    def _menu_help_about_triggered(self):
        self._ui_help_about = HelpAbout()
        self._ui_help_about.show()

    def _button_11_clicked(self):
        self._ui_sub1 = BaiduASR(parent=self, self.workDir, self.auth1)
        self._ui_sub1.show()

    def _button_12_clicked(self):
        self._ui_sub2 = BaiduSynthesis(parent=self, self.workDir, self.auth2)
        self._ui_sub2.show()

    def _button_19_clicked(self):
        self._ui_colorboard = ColorBoard(parent=self)
        self._ui_colorboard.show()

def run_qtui(workDir):
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow(workDir=workDir)
    ui.show()
    sys.exit(app.exec_())
