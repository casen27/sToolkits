# pyqt5 主界面

import sys

from PyQt5 import QtCore, QtWidgets

from .st_baidu import BaiduConnect
from .st_config import CONFIG
from .st_ui_baidu import BaiduASRUI, BaiduSynthesisUI, BaiduTranslateUI
from .st_ui_utils import CalcFileHashUI, PicMixZipUI
from .st_ui_images import ColorBoardUI, GIFSpliterUI
from .st_ui_menu import HelpAboutUI, SettingKeysUI


class MainWindow(QtWidgets.QMainWindow):
    version = "1.1.0"

    def __init__(self, workDir):
        super().__init__()
        self.workDir = workDir
        self.auths = {}
        self.auth1 = {}
        self.auth2 = {}

        self.__initUI()
        self.__initMenu()
        self.__initTab_all()
        self.__initActions()
        self.__initDatas()

    def __initUI(self):
        self.setFixedSize(520, 360)  # 固定大小
        self.setWindowTitle("sToolkits —— 实用小工具集")
        self.setObjectName("MainWindow")

        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 23))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

    def __initMenu(self):
        self.menu_setting = QtWidgets.QMenu(self.menubar)
        self.menu_setting.setTitle("设置")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setTitle("帮助")

        self.menu_setting_keys = QtWidgets.QAction(self)
        self.menu_setting_keys.setText("设置Keys")
        self.menu_setting_exit = QtWidgets.QAction(self)
        self.menu_setting_exit.setText("退出")
        self.menu_help_about = QtWidgets.QAction(self)
        self.menu_help_about.setText("关于")

        self.menu_setting.addAction(self.menu_setting_keys)
        self.menu_setting.addSeparator()
        self.menu_setting.addAction(self.menu_setting_exit)
        self.menu_help.addAction(self.menu_help_about)

        self.menubar.addAction(self.menu_setting.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

    def __initTab_all(self):
        # 主要的tabWidget
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 500, 300))
        self.tabWidget.setObjectName("tabWidget")

        self.__initTab_t00()
        self.__initTab_t10()
        self.__initTab_t20()
        self.__initTab_t30()

        self.tabWidget.addTab(self.tab_00, "")
        self.tabWidget.addTab(self.tab_10, "")
        self.tabWidget.addTab(self.tab_20, "")
        self.tabWidget.addTab(self.tab_30, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_00), "百度AI")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), "图像工具")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_20), "媒体工具")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_30), "杂类工具")
        self.tabWidget.setCurrentIndex(0)

    def __initTab_t00(self):
        self.tab_00 = QtWidgets.QWidget()
        self.tab_00.setObjectName("tab_00")

        self.widget_00 = QtWidgets.QWidget(self.tab_00)
        self.widget_00.setGeometry(QtCore.QRect(50, 20, 400, 120))
        self.widget_00.setObjectName("widget_00")
        self.gLayout_00 = QtWidgets.QGridLayout(self.widget_00)
        self.gLayout_00.setContentsMargins(0, 0, 0, 0)
        self.gLayout_00.setObjectName("gLayout_00")
        self.button_01 = QtWidgets.QPushButton(self.widget_00)
        self.button_01.setObjectName("button_01")
        self.button_01.setText("语音转文字")
        self.button_02 = QtWidgets.QPushButton(self.widget_00)
        self.button_02.setObjectName("button_02")
        self.button_02.setText("文字转语音")
        self.button_03 = QtWidgets.QPushButton(self.widget_00)
        self.button_03.setObjectName("button_03")
        self.button_03.setText("按钮03")
        self.button_04 = QtWidgets.QPushButton(self.widget_00)
        self.button_04.setObjectName("button_04")
        self.button_04.setText("翻译")
        self.gLayout_00.addWidget(self.button_01, 0, 0, 1, 1)
        self.gLayout_00.addWidget(self.button_02, 0, 1, 1, 1)
        self.gLayout_00.addWidget(self.button_03, 0, 2, 1, 1)
        self.gLayout_00.addWidget(self.button_04, 1, 0, 1, 1)
        # self.gLayout_00.addWidget(self.button_05, 1, 0, 1, 1)
        # self.gLayout_00.addWidget(self.button_06, 1, 0, 1, 1)

        self.widget_01 = QtWidgets.QWidget(self.tab_00)
        self.widget_01.setGeometry(QtCore.QRect(0, 210, 500, 70))
        self.widget_01.setObjectName("widget_01")
        self.label_01 = QtWidgets.QLabel(self.widget_01)
        self.label_01.setGeometry(QtCore.QRect(100, 10, 200, 20))
        self.label_01.setObjectName("label_01")
        self.label_02 = QtWidgets.QLabel(self.widget_01)
        self.label_02.setGeometry(QtCore.QRect(100, 40, 200, 20))
        self.label_02.setObjectName("label_02")
        self.button_0a = QtWidgets.QPushButton(self.widget_01)
        self.button_0a.setGeometry(QtCore.QRect(300, 10, 100, 23))
        self.button_0a.setObjectName("button_0a")
        self.button_0a.setText("链接BaiduAI")
        self.button_0b = QtWidgets.QPushButton(self.widget_01)
        self.button_0b.setGeometry(QtCore.QRect(300, 40, 100, 23))
        self.button_0b.setObjectName("button_0b")
        self.button_0b.setText("设置Keys")

    def __initTab_t10(self):
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.widget_10 = QtWidgets.QWidget(self.tab_10)
        self.widget_10.setGeometry(QtCore.QRect(50, 20, 400, 120))
        self.widget_10.setObjectName("widget_10")
        self.gLayout_10 = QtWidgets.QGridLayout(self.widget_10)
        self.gLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gLayout_10.setObjectName("gLayout_10")
        self.button_11 = QtWidgets.QPushButton(self.widget_10)
        self.button_11.setObjectName("button_11")
        self.button_11.setText("RGB色彩板")
        self.button_12 = QtWidgets.QPushButton(self.widget_10)
        self.button_12.setObjectName("button_12")
        self.button_12.setText("GIF分割器")
        self.button_13 = QtWidgets.QPushButton(self.widget_10)
        self.button_13.setObjectName("button_13")
        self.button_13.setText("按钮13")
        self.button_14 = QtWidgets.QPushButton(self.widget_10)
        self.button_14.setObjectName("button_14")
        self.button_14.setText("按钮14")
        self.gLayout_10.addWidget(self.button_11, 0, 0, 1, 1)
        self.gLayout_10.addWidget(self.button_12, 0, 1, 1, 1)
        self.gLayout_10.addWidget(self.button_13, 0, 2, 1, 1)
        self.gLayout_10.addWidget(self.button_14, 1, 0, 1, 1)
        # self.gLayout_10.addWidget(self.button_15, 1, 0, 1, 1)
        # self.gLayout_10.addWidget(self.button_16, 1, 0, 1, 1)

    def __initTab_t20(self):
        self.tab_20 = QtWidgets.QWidget()
        self.tab_20.setObjectName("tab_20")

    def __initTab_t30(self):
        self.tab_30 = QtWidgets.QWidget()
        self.tab_30.setObjectName("tab_30")
        self.widget_30 = QtWidgets.QWidget(self.tab_30)
        self.widget_30.setGeometry(QtCore.QRect(50, 20, 400, 120))
        self.widget_30.setObjectName("widget_30")
        self.gLayout_30 = QtWidgets.QGridLayout(self.widget_30)
        self.gLayout_30.setContentsMargins(0, 0, 0, 0)
        self.gLayout_30.setObjectName("gLayout_30")
        self.button_31 = QtWidgets.QPushButton(self.widget_30)
        self.button_31.setObjectName("button_31")
        self.button_31.setText("文件哈希值")
        self.button_32 = QtWidgets.QPushButton(self.widget_30)
        self.button_32.setObjectName("button_32")
        self.button_32.setText("图片种子合成")
        self.button_33 = QtWidgets.QPushButton(self.widget_30)
        self.button_33.setObjectName("button_33")
        self.button_33.setText("按钮33")
        self.button_34 = QtWidgets.QPushButton(self.widget_30)
        self.button_34.setObjectName("button_34")
        self.button_34.setText("按钮34")
        self.gLayout_30.addWidget(self.button_31, 0, 0, 1, 1)
        self.gLayout_30.addWidget(self.button_32, 0, 1, 1, 1)
        self.gLayout_30.addWidget(self.button_33, 0, 2, 1, 1)
        self.gLayout_30.addWidget(self.button_34, 1, 0, 1, 1)
        # self.gLayout_30.addWidget(self.button_35, 1, 0, 1, 1)
        # self.gLayout_30.addWidget(self.button_36, 1, 0, 1, 1)

    def __initActions(self):
        self.menu_setting_keys.triggered.connect(self._menu_setting_keys)
        self.menu_setting_exit.triggered.connect(QtWidgets.qApp.quit)
        self.menu_help_about.triggered.connect(self._menu_help_about)
        self.button_01.clicked.connect(self._button_01_clicked)
        self.button_02.clicked.connect(self._button_02_clicked)
        self.button_04.clicked.connect(self._button_04_clicked)
        self.button_0a.clicked.connect(self._fresh_connect_baidu)
        self.button_0b.clicked.connect(self._menu_setting_keys)
        self.button_11.clicked.connect(self._button_11_clicked)
        self.button_12.clicked.connect(self._button_12_clicked)
        self.button_31.clicked.connect(self._button_31_clicked)
        self.button_32.clicked.connect(self._button_32_clicked)

    def __initDatas(self):
        self.statusbar.showMessage("欢迎使用**小工具箱", 3000)
        self._disable_baidu_all()
        self._get_baidu_auths()

    def _menu_setting_keys(self):
        self._ui_setting_keys = SettingKeysUI(workDir=self.workDir, auths=self.auths)
        self._ui_setting_keys.signal_close.connect(self._fresh_connect_baidu)
        self._ui_setting_keys.show()

    def _menu_help_about(self):
        self._ui_help_about = HelpAboutUI()
        self._ui_help_about.show()

    def _get_baidu_auths(self):
        con = CONFIG(workDir=self.workDir)
        self.auths = con.get()
        tokens1 = self.auths["BAIDU_DEFAULT"]
        tokens2 = self.auths["BAIDU_TRANSLATE"]
        self.auth1 = {
                "apikey": tokens1["apikey"],
                "secretkey": tokens1["secretkey"]
                }
        self.auth2 = {
                "appid": tokens2["appid"],
                "secretkey": tokens2["secretkey"]
                }

    def _disable_baidu_all(self):
        self.label_01.setText("语音图文API：无网络或key错误")
        self.label_02.setText("文字翻译API：无网络或key错误")
        self.button_01.setEnabled(False)
        self.button_02.setEnabled(False)
        self.button_03.setEnabled(False)
        self.button_04.setEnabled(False)

    def _check_baidu_auths(self):
        self._disable_baidu_all()
        if BaiduConnect.connect1(self.auth1):
            self.label_01.setText("语音图文API：已链接")
            # 激活相关功能
            self.button_01.setEnabled(True)
            self.button_02.setEnabled(True)
        if BaiduConnect.connect2(self.auth2):
            self.label_02.setText("文字翻译API：已链接")
            # 激活相关功能
            self.button_04.setEnabled(True)

    def _fresh_connect_baidu(self):
        self._get_baidu_auths()
        self._check_baidu_auths()

    def _button_01_clicked(self):
        self._ui_baidu_asr = BaiduASRUI(workDir=self.workDir, auths=self.auth1)
        self._ui_baidu_asr.show()

    def _button_02_clicked(self):
        self._ui_baidu_syn = BaiduSynthesisUI(workDir=self.workDir, auths=self.auth1)
        self._ui_baidu_syn.show()

    def _button_04_clicked(self):
        self._ui_baidu_tsl = BaiduTranslateUI(workDir=self.workDir, auths=self.auth2)
        self._ui_baidu_tsl.show()

    def _button_11_clicked(self):
        self._ui_colorboard = ColorBoardUI()
        self._ui_colorboard.show()

    def _button_12_clicked(self):
        self._ui_gifspliter = GIFSpliterUI()
        self._ui_gifspliter.show()

    def _button_31_clicked(self):
        self._ui_filehash = CalcFileHashUI()
        self._ui_filehash.show()

    def _button_32_clicked(self):
        self._ui_pmz = PicMixZipUI()
        self._ui_pmz.show()

def run(workDir):
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow(workDir=workDir)
    ui.show()
    sys.exit(app.exec_())
