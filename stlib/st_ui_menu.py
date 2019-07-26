# 菜单栏的全部配置

"""
menu_setting_keys    SettingKeysUI
menu_help_about      HelpAboutUI
"""

from PySide2 import QtCore, QtGui, QtWidgets

from .st_baidu import BaiduConnect
from .st_config import CONFIG
from .st_settings import AboutHTML, BAIDU_AI_KEYS_URL, ProjectURL


class HelpAboutUI(QtWidgets.QWidget):
    version = "1.0.0"

    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.__init_actions()

    def __init_ui(self):
        self.setFixedSize(440, 210)  # 固定大小
        self.setWindowTitle("关于")

        self.text_01 = QtWidgets.QTextBrowser(self)
        self.text_01.setGeometry(QtCore.QRect(20, 20, 400, 120))
        self.text_01.setHtml(AboutHTML)

        self.button_2 = QtWidgets.QPushButton(self)
        self.button_2.setGeometry(QtCore.QRect(150, 160, 100, 30))
        self.button_2.setText("项目主页")
        self.button_1 = QtWidgets.QPushButton(self)
        self.button_1.setGeometry(QtCore.QRect(300, 160, 100, 30))
        self.button_1.setText("关闭")

    def __init_actions(self):
        self.button_1.clicked.connect(self.close)
        self.button_2.clicked.connect(self._open_project_url)

    def _open_project_url(self):
        # 项目主页
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(ProjectURL))


class SettingKeysUI(QtWidgets.QWidget):
    version = "1.0.0"
    signal_close = QtCore.Signal()

    def __init__(self, work_dir, auths):
        super().__init__()
        self.work_dir = work_dir
        self.auths = auths

        self.__init_ui()
        self.__init_actions()
        self.__init_datas()

    def __init_ui(self):
        self.setFixedSize(480, 280)  # 固定大小
        self.setWindowTitle("百度AI Key设置")

        self.groupBox_1 = QtWidgets.QGroupBox(self)
        self.groupBox_1.setGeometry(QtCore.QRect(10, 10, 460, 80))
        self.groupBox_1.setTitle("语音转文字、文字转语音、截图文字识别")
        self.layout_1 = QtWidgets.QWidget(self.groupBox_1)
        self.layout_1.setGeometry(QtCore.QRect(10, 20, 330, 80))
        self.fLayout_1 = QtWidgets.QFormLayout(self.layout_1)
        self.fLayout_1.setContentsMargins(0, 0, 0, 0)
        # self.label_111 = QtWidgets.QLabel(self.layout_1)
        # self.label_111.setText("appId")
        self.label_112 = QtWidgets.QLabel(self.layout_1)
        self.label_112.setText("apiKey")
        self.label_113 = QtWidgets.QLabel(self.layout_1)
        self.label_113.setText("secretKey")
        # self.lineEdit_121 = QtWidgets.QLineEdit(self.layout_1)
        self.lineEdit_122 = QtWidgets.QLineEdit(self.layout_1)
        self.lineEdit_123 = QtWidgets.QLineEdit(self.layout_1)
        # self.fLayout_1.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_111)
        # self.fLayout_1.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_121)
        self.fLayout_1.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_112)
        self.fLayout_1.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_122)
        self.fLayout_1.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_113)
        self.fLayout_1.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_123)

        self.label_131 = QtWidgets.QLabel(self.groupBox_1)
        self.label_131.setGeometry(QtCore.QRect(360, 10, 80, 20))
        self.label_131.setAlignment(QtCore.Qt.AlignCenter)
        self.label_131.setText("未检测")
        self.button_131 = QtWidgets.QPushButton(self.groupBox_1)
        self.button_131.setGeometry(QtCore.QRect(360, 40, 80, 23))
        self.button_131.setText("检测")

        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 100, 460, 80))
        self.groupBox_2.setTitle("翻译")
        self.layout_2 = QtWidgets.QWidget(self.groupBox_2)
        self.layout_2.setGeometry(QtCore.QRect(10, 20, 330, 50))
        self.fLayout_2 = QtWidgets.QFormLayout(self.layout_2)
        self.fLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_211 = QtWidgets.QLabel(self.layout_2)
        self.label_211.setText("appid")
        self.label_212 = QtWidgets.QLabel(self.layout_2)
        self.label_212.setText("secretKey")
        self.lineEdit_221 = QtWidgets.QLineEdit(self.layout_2)
        self.lineEdit_222 = QtWidgets.QLineEdit(self.layout_2)
        self.fLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_211)
        self.fLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_221)
        self.fLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_212)
        self.fLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_222)

        self.label_231 = QtWidgets.QLabel(self.groupBox_2)
        self.label_231.setAlignment(QtCore.Qt.AlignCenter)
        self.label_231.setGeometry(QtCore.QRect(360, 20, 80, 20))
        self.label_231.setText("未检测")
        self.button_231 = QtWidgets.QPushButton(self.groupBox_2)
        self.button_231.setGeometry(QtCore.QRect(360, 50, 80, 23))
        self.button_231.setText("检测")

        self.button_11 = QtWidgets.QPushButton(self)
        self.button_11.setGeometry(QtCore.QRect(30, 230, 100, 23))
        self.button_11.setText("申请Key")
        self.button_12 = QtWidgets.QPushButton(self)
        self.button_12.setGeometry(QtCore.QRect(330, 230, 100, 23))
        self.button_12.setText("保存")

    def __init_actions(self):
        self.button_11.clicked.connect(self._get_baidu_ai_keys)
        self.button_12.clicked.connect(self._save_and_back)
        self.button_131.clicked.connect(self._check_key_131)
        self.button_231.clicked.connect(self._check_key_231)
        # self.lineEdit_121.textChanged.connect(self._auth1_changed)
        self.lineEdit_122.textChanged.connect(self._auth1_changed)
        self.lineEdit_123.textChanged.connect(self._auth1_changed)
        self.lineEdit_221.textChanged.connect(self._auth2_changed)
        self.lineEdit_222.textChanged.connect(self._auth2_changed)

    def __init_datas(self):
        # self.lineEdit_121.setText(self.auths["BAIDU_DEFAULT"]["appid"])
        self.lineEdit_122.setText(self.auths["BAIDU_DEFAULT"]["apikey"])
        self.lineEdit_123.setText(self.auths["BAIDU_DEFAULT"]["secretkey"])
        self.lineEdit_221.setText(self.auths["BAIDU_TRANSLATE"]["appid"])
        self.lineEdit_222.setText(self.auths["BAIDU_TRANSLATE"]["secretkey"])

    def _get_baidu_ai_keys(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(BAIDU_AI_KEYS_URL))

    def _save_and_back(self):
        # save ini
        # self.auths["BAIDU_DEFAULT"]["appid"] = self.lineEdit_121.text()
        self.auths["BAIDU_DEFAULT"]["apikey"] = self.lineEdit_122.text()
        self.auths["BAIDU_DEFAULT"]["secretkey"] = self.lineEdit_123.text()
        self.auths["BAIDU_TRANSLATE"]["appid"] = self.lineEdit_221.text()
        self.auths["BAIDU_TRANSLATE"]["secretkey"] = self.lineEdit_222.text()
        con = CONFIG(work_dir=self.work_dir)
        con.save(self.auths)
        # back
        self.close()

    def _auth1_changed(self):
        self.label_131.setText("待检测")

    def _auth2_changed(self):
        self.label_231.setText("待检测")

    def _check_key_131(self):
        # self.auths["BAIDU_DEFAULT"]["appid"] = self.lineEdit_121.text()
        self.auths["BAIDU_DEFAULT"]["apikey"] = self.lineEdit_122.text()
        self.auths["BAIDU_DEFAULT"]["secretkey"] = self.lineEdit_123.text()
        if BaiduConnect.connect1(self.auths["BAIDU_DEFAULT"]):
            self.label_131.setText("有效")
        else:
            self.label_131.setText("无效")

    def _check_key_231(self):
        self.auths["BAIDU_TRANSLATE"]["appid"] = self.lineEdit_221.text()
        self.auths["BAIDU_TRANSLATE"]["secretkey"] = self.lineEdit_222.text()
        if BaiduConnect.connect2(self.auths["BAIDU_TRANSLATE"]):
            self.label_231.setText("有效")
        else:
            self.label_231.setText("无效")

    def closeEvent(self, event):
        self.signal_close.emit()
