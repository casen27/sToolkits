# pyqt5 菜单栏的全部配置

"""
menu_setting_keys    SettingKeys
menu_help_about      HelpAbout
"""

from PyQt5 import QtCore, QtGui, QtWidgets

from .st_config import CONFIG
from .st_baiduai import ConnectBaidu
from .st_settings import AboutHTML, BAIDU_AI_KEYS_URL, ProjectURL


class HelpAbout(QtWidgets.QWidget):
    version = "v1.0.0"

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.__initUI()

    def __initUI(self):
        self.setObjectName("HelpAbout")
        self.setFixedSize(440, 210)  # 固定大小
        # self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)  # 禁止最大化
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowTitle("关于")

        self.textBrowser_01 = QtWidgets.QTextBrowser(self)
        self.textBrowser_01.setGeometry(QtCore.QRect(20, 20, 400, 120))
        self.textBrowser_01.setObjectName("textBrowser_01")
        self.textBrowser_01.setHtml(AboutHTML)

        self.button_2 = QtWidgets.QPushButton(self)
        self.button_2.setGeometry(QtCore.QRect(150, 160, 100, 30))
        self.button_2.setObjectName("button_2")
        self.button_2.setText("项目主页")
        self.button_2.clicked.connect(self._open_project_url)
        self.button_1 = QtWidgets.QPushButton(self)
        self.button_1.setGeometry(QtCore.QRect(300, 160, 100, 30))
        self.button_1.setObjectName("button_1")
        self.button_1.setText("关闭")
        self.button_1.clicked.connect(self.close)

    def _open_project_url(self):
        # 项目主页
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(ProjectURL))


class SettingKeys(QtWidgets.QWidget):
    version = "v1.0.0"
    signal = QtCore.pyqtSignal(int)

    def __init__(self, parent, workDir, auths):
        super().__init__()
        self.parent = parent
        self.workDir = workDir
        self.auths = auths
        self.__initUI()
        self.__initDatas()

    def __initUI(self):
        self.setObjectName("SettingKeys")
        self.setFixedSize(520, 320)  # 固定大小
        # self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)  # 禁止最大化
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowTitle("Keys设置")

        self.groupBox_1 = QtWidgets.QGroupBox(self)
        self.groupBox_1.setGeometry(QtCore.QRect(10, 10, 500, 120))
        self.groupBox_1.setFlat(False)
        self.groupBox_1.setCheckable(False)
        self.groupBox_1.setObjectName("groupBox_1")
        self.groupBox_1.setTitle("语音转文字、文字转语音、截图文字识别")

        self.layoutWidget_11 = QtWidgets.QWidget(self.groupBox_1)
        self.layoutWidget_11.setGeometry(QtCore.QRect(10, 20, 60, 80))
        self.layoutWidget_11.setObjectName("layoutWidget_11")
        self.vLayout_11 = QtWidgets.QVBoxLayout(self.layoutWidget_11)
        self.vLayout_11.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.vLayout_11.setContentsMargins(0, 0, 0, 0)
        self.vLayout_11.setObjectName("vLayout_11")
        self.label_111 = QtWidgets.QLabel(self.layoutWidget_11)
        self.label_111.setObjectName("label_111")
        self.label_111.setText("appId")
        self.label_112 = QtWidgets.QLabel(self.layoutWidget_11)
        self.label_112.setObjectName("label_112")
        self.label_112.setText("apiKey")
        self.label_113 = QtWidgets.QLabel(self.layoutWidget_11)
        self.label_113.setObjectName("label_113")
        self.label_113.setText("secretKey")
        self.vLayout_11.addWidget(self.label_111)
        self.vLayout_11.addWidget(self.label_112)
        self.vLayout_11.addWidget(self.label_113)

        self.layoutWidget_12 = QtWidgets.QWidget(self.groupBox_1)
        self.layoutWidget_12.setGeometry(QtCore.QRect(80, 20, 300, 90))
        self.layoutWidget_12.setObjectName("layoutWidget_12")
        self.vLayout_12 = QtWidgets.QVBoxLayout(self.layoutWidget_12)
        self.vLayout_12.setContentsMargins(0, 0, 0, 0)
        self.vLayout_12.setObjectName("vLayout_12")
        self.lineEdit_121 = QtWidgets.QLineEdit(self.layoutWidget_12)
        self.lineEdit_121.setObjectName("lineEdit_121")
        self.lineEdit_121.textChanged.connect(self._auth1_changed)
        self.lineEdit_122 = QtWidgets.QLineEdit(self.layoutWidget_12)
        self.lineEdit_122.setObjectName("lineEdit_122")
        self.lineEdit_122.textChanged.connect(self._auth1_changed)
        self.lineEdit_123 = QtWidgets.QLineEdit(self.layoutWidget_12)
        self.lineEdit_123.setObjectName("lineEdit_123")
        self.lineEdit_123.textChanged.connect(self._auth1_changed)
        self.vLayout_12.addWidget(self.lineEdit_121)
        self.vLayout_12.addWidget(self.lineEdit_122)
        self.vLayout_12.addWidget(self.lineEdit_123)

        self.layoutWidget_13 = QtWidgets.QWidget(self.groupBox_1)
        self.layoutWidget_13.setGeometry(QtCore.QRect(410, 30, 80, 60))
        self.layoutWidget_13.setObjectName("layoutWidget_13")
        self.vLayout_13 = QtWidgets.QVBoxLayout(self.layoutWidget_13)
        self.vLayout_13.setContentsMargins(0, 0, 0, 0)
        self.vLayout_13.setObjectName("vLayout_13")
        self.label_131 = QtWidgets.QLabel(self.layoutWidget_13)
        self.label_131.setAlignment(QtCore.Qt.AlignCenter)
        self.label_131.setObjectName("label_131")
        self.label_131.setText("（状态）")
        self.button_131 = QtWidgets.QPushButton(self.layoutWidget_13)
        self.button_131.setObjectName("button_131")
        self.button_131.setText("重新检测")
        self.button_131.clicked.connect(self._check_key_131)
        self.vLayout_13.addWidget(self.label_131)
        self.vLayout_13.addWidget(self.button_131)

        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 150, 500, 100))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setTitle("翻译")

        self.layoutWidget_21 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget_21.setGeometry(QtCore.QRect(10, 20, 60, 60))
        self.layoutWidget_21.setObjectName("layoutWidget_21")
        self.vLayout_21 = QtWidgets.QVBoxLayout(self.layoutWidget_21)
        self.vLayout_21.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.vLayout_21.setContentsMargins(0, 0, 0, 0)
        self.vLayout_21.setObjectName("vLayout_21")
        self.label_211 = QtWidgets.QLabel(self.layoutWidget_21)
        self.label_211.setObjectName("label_211")
        self.label_211.setText("apiKey")
        self.label_212 = QtWidgets.QLabel(self.layoutWidget_21)
        self.label_212.setObjectName("label_212")
        self.label_212.setText("secretKey")
        self.vLayout_21.addWidget(self.label_211)
        self.vLayout_21.addWidget(self.label_212)

        self.layoutWidget_22 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget_22.setGeometry(QtCore.QRect(80, 20, 300, 70))
        self.layoutWidget_22.setObjectName("layoutWidget_22")
        self.vLayout_22 = QtWidgets.QVBoxLayout(self.layoutWidget_22)
        self.vLayout_22.setContentsMargins(0, 0, 0, 0)
        self.vLayout_22.setObjectName("vLayout_22")
        self.lineEdit_221 = QtWidgets.QLineEdit(self.layoutWidget_22)
        self.lineEdit_221.setObjectName("lineEdit_221")
        self.lineEdit_221.textChanged.connect(self._auth2_changed)
        self.lineEdit_222 = QtWidgets.QLineEdit(self.layoutWidget_22)
        self.lineEdit_222.setObjectName("lineEdit_222")
        self.lineEdit_222.textChanged.connect(self._auth2_changed)
        self.vLayout_22.addWidget(self.lineEdit_221)
        self.vLayout_22.addWidget(self.lineEdit_222)

        self.layoutWidget_23 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget_23.setGeometry(QtCore.QRect(410, 20, 80, 60))
        self.layoutWidget_23.setObjectName("layoutWidget_23")
        self.vLayout_23 = QtWidgets.QVBoxLayout(self.layoutWidget_23)
        self.vLayout_23.setContentsMargins(0, 0, 0, 0)
        self.vLayout_23.setObjectName("vLayout_23")
        self.label_231 = QtWidgets.QLabel(self.layoutWidget_23)
        self.label_231.setAlignment(QtCore.Qt.AlignCenter)
        self.label_231.setObjectName("label_231")
        self.label_231.setText("（状态）")
        self.button_231 = QtWidgets.QPushButton(self.layoutWidget_23)
        self.button_231.setObjectName("button_231")
        self.button_231.setText("重新检测")
        self.button_231.clicked.connect(self._check_key_231)
        self.vLayout_23.addWidget(self.label_231)
        self.vLayout_23.addWidget(self.button_231)

        self.layoutWidget_31 = QtWidgets.QWidget(self)
        self.layoutWidget_31.setGeometry(QtCore.QRect(120, 260, 270, 40))
        self.layoutWidget_31.setObjectName("layoutWidget_31")
        self.hLayout_01 = QtWidgets.QHBoxLayout(self.layoutWidget_31)
        self.hLayout_01.setContentsMargins(0, 0, 0, 0)
        self.hLayout_01.setObjectName("hLayout_01")
        self.button_11 = QtWidgets.QPushButton(self.layoutWidget_31)
        self.button_11.setObjectName("button_11")
        self.button_11.setText("申请Key")
        self.button_11.clicked.connect(self._get_baidu_ai_keys)
        self.button_12 = QtWidgets.QPushButton(self.layoutWidget_31)
        self.button_12.setObjectName("button_12")
        self.button_12.setText("保存&&返回")
        self.button_12.clicked.connect(self._save_and_back)
        self.hLayout_01.addWidget(self.button_11)
        self.hLayout_01.addWidget(self.button_12)

    def __initDatas(self):
        self.lineEdit_121.setText(self.auths["BAIDU_DEFAULT"]["appid"])
        self.lineEdit_122.setText(self.auths["BAIDU_DEFAULT"]["apikey"])
        self.lineEdit_123.setText(self.auths["BAIDU_DEFAULT"]["secretkey"])
        self.lineEdit_221.setText(self.auths["BAIDU_TRANSLATE"]["appid"])
        self.lineEdit_222.setText(self.auths["BAIDU_TRANSLATE"]["secretkey"])

    def _get_baidu_ai_keys(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(BAIDU_AI_KEYS_URL))

    def _save_and_back(self):
        # save ini
        self.auths["BAIDU_DEFAULT"]["appid"] = self.lineEdit_121.text()
        self.auths["BAIDU_DEFAULT"]["apikey"] = self.lineEdit_122.text()
        self.auths["BAIDU_DEFAULT"]["secretkey"] = self.lineEdit_123.text()
        self.auths["BAIDU_TRANSLATE"]["appid"] = self.lineEdit_221.text()
        self.auths["BAIDU_TRANSLATE"]["secretkey"] = self.lineEdit_222.text()
        con = CONFIG(workDir=self.workDir)
        con.save(self.auths)
        # back
        self.close()

    def _auth1_changed(self):
        self.label_131.setText("待检测")

    def _auth2_changed(self):
        self.label_231.setText("待检测")

    def _check_key_131(self):
        self.auths["BAIDU_DEFAULT"]["appid"] = self.lineEdit_121.text()
        self.auths["BAIDU_DEFAULT"]["apikey"] = self.lineEdit_122.text()
        self.auths["BAIDU_DEFAULT"]["secretkey"] = self.lineEdit_123.text()
        if ConnectBaidu.connect1(self.auths["BAIDU_DEFAULT"]):
            self.label_131.setText("有效")
        else:
            self.label_131.setText("无效")

    def _check_key_231(self):
        self.auths["BAIDU_TRANSLATE"]["appid"] = self.lineEdit_221.text()
        self.auths["BAIDU_TRANSLATE"]["secretkey"] = self.lineEdit_222.text()
        if ConnectBaidu.connect2(self.auths["BAIDU_TRANSLATE"]):
            self.label_231.setText("有效")
        else:
            self.label_231.setText("无效")

    def closeEvent(self, event):
        self.signal.emit(1)
