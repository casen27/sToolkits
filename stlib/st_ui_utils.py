# 扩展工具等的界面

import os

from PySide2 import QtCore, QtGui, QtWidgets

from .st_utils import CalcFileHash, PicMixZip


class CalcFileHashUI(QtWidgets.QWidget):
    # 计算文件的哈希值
    version = "1.0.0"

    def __init__(self):
        super().__init__()
        self.file = ""

        self.__initUI()
        self.__initActions()
        self.__initDatas()

    def __initUI(self):
        self.setObjectName("CalcFileHashUI")
        self.setFixedSize(600, 480)
        self.setWindowTitle("哈希值计算")

        self.groupBox_1 = QtWidgets.QGroupBox(self)
        self.groupBox_1.setGeometry(QtCore.QRect(10, 10, 580, 190))
        self.groupBox_1.setObjectName("groupBox_1")
        self.groupBox_1.setTitle("基础信息")
        self.layout_1 = QtWidgets.QWidget(self.groupBox_1)
        self.layout_1.setGeometry(QtCore.QRect(10, 20, 560, 165))
        self.layout_1.setObjectName("layout_1")
        self.fLayout_1 = QtWidgets.QFormLayout(self.layout_1)
        self.fLayout_1.setContentsMargins(0, 0, 0, 0)
        self.fLayout_1.setObjectName("fLayout_1")
        self.label_11 = QtWidgets.QLabel(self.layout_1)
        self.label_11.setObjectName("label_11")
        self.label_11.setText("路径")
        self.label_12 = QtWidgets.QLabel(self.layout_1)
        self.label_12.setObjectName("label_12")
        self.label_12.setText("名称")
        self.label_13 = QtWidgets.QLabel(self.layout_1)
        self.label_13.setObjectName("label_13")
        self.label_13.setText("大小")
        self.label_14 = QtWidgets.QLabel(self.layout_1)
        self.label_14.setObjectName("label_14")
        self.label_14.setText("创建时间")
        self.label_15 = QtWidgets.QLabel(self.layout_1)
        self.label_15.setObjectName("label_15")
        self.label_15.setText("访问时间")
        self.label_16 = QtWidgets.QLabel(self.layout_1)
        self.label_16.setObjectName("label_16")
        self.label_16.setText("修改时间")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.layout_1)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.layout_1)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.layout_1)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.layout_1)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.layout_1)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.layout_1)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_16.setReadOnly(True)
        self.fLayout_1.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.fLayout_1.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_11)
        self.fLayout_1.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.fLayout_1.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_12)
        self.fLayout_1.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.fLayout_1.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_13)
        self.fLayout_1.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.fLayout_1.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_14)
        self.fLayout_1.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.fLayout_1.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_15)
        self.fLayout_1.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.fLayout_1.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_16)

        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 210, 580, 160))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setTitle("哈希值")
        self.layout_2 = QtWidgets.QWidget(self.groupBox_2)
        self.layout_2.setGeometry(QtCore.QRect(10, 20, 560, 130))
        self.layout_2.setObjectName("layout_2")
        self.fLayout_2 = QtWidgets.QFormLayout(self.layout_2)
        self.fLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fLayout_2.setObjectName("fLayout_2")
        self.checkBox_21 = QtWidgets.QCheckBox(self.layout_2)
        self.checkBox_21.setObjectName("checkBox_21")
        self.checkBox_21.setText("MD5")
        self.checkBox_22 = QtWidgets.QCheckBox(self.layout_2)
        self.checkBox_22.setObjectName("checkBox_22")
        self.checkBox_22.setText("sha1")
        self.checkBox_23 = QtWidgets.QCheckBox(self.layout_2)
        self.checkBox_23.setObjectName("checkBox_23")
        self.checkBox_23.setText("sha256")
        self.checkBox_24 = QtWidgets.QCheckBox(self.layout_2)
        self.checkBox_24.setObjectName("checkBox_24")
        self.checkBox_24.setText("sha384")
        self.checkBox_25 = QtWidgets.QCheckBox(self.layout_2)
        self.checkBox_25.setObjectName("checkBox_25")
        self.checkBox_25.setText("sha512")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.layout_2)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_21.setReadOnly(True)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.layout_2)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_22.setReadOnly(True)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.layout_2)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.lineEdit_23.setReadOnly(True)
        self.lineEdit_24 = QtWidgets.QLineEdit(self.layout_2)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.lineEdit_24.setReadOnly(True)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.layout_2)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.lineEdit_25.setReadOnly(True)
        self.fLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.checkBox_21)
        self.fLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_21)
        self.fLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkBox_22)
        self.fLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_22)
        self.fLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.checkBox_23)
        self.fLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_23)
        self.fLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.checkBox_24)
        self.fLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_24)
        self.fLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.checkBox_25)
        self.fLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_25)

        self.layout_3 = QtWidgets.QWidget(self)
        self.layout_3.setGeometry(QtCore.QRect(10, 380, 580, 90))
        self.layout_3.setObjectName("layout_3")
        self.label_31 = QtWidgets.QLabel(self.layout_3)
        self.label_31.setGeometry(QtCore.QRect(10, 20, 30, 20))
        self.label_31.setObjectName("label_31")
        self.label_31.setText("文件")
        self.lineEdit_31 = QtWidgets.QLineEdit(self.layout_3)
        self.lineEdit_31.setGeometry(QtCore.QRect(40, 20, 430, 20))
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.lineEdit_31.setReadOnly(True)
        self.button_31 = QtWidgets.QPushButton(self.layout_3)
        self.button_31.setGeometry(QtCore.QRect(480, 20, 100, 23))
        self.button_31.setObjectName("button_31")
        self.button_31.setText("打开文件")
        self.button_32 = QtWidgets.QPushButton(self.layout_3)
        self.button_32.setGeometry(QtCore.QRect(480, 60, 100, 23))
        self.button_32.setObjectName("button_32")
        self.button_32.setText("计算哈希值")
        self.button_33 = QtWidgets.QPushButton(self.layout_3)
        self.button_33.setGeometry(QtCore.QRect(120, 60, 120, 23))
        self.button_33.setObjectName("button_33")
        self.button_33.setText("复制json到剪切板")
        self.button_34 = QtWidgets.QPushButton(self.layout_3)
        self.button_34.setGeometry(QtCore.QRect(280, 60, 120, 23))
        self.button_34.setObjectName("button_34")
        self.button_34.setText("复制text到剪切板")

    def __initDatas(self):
        self.lineEdit_11.setText("")
        self.lineEdit_12.setText("")
        self.lineEdit_13.setText("")
        self.lineEdit_14.setText("")
        self.lineEdit_15.setText("")
        self.lineEdit_16.setText("")
        self.checkBox_21.setChecked(True)
        self.checkBox_22.setChecked(True)
        self.checkBox_23.setChecked(False)
        self.checkBox_24.setChecked(False)
        self.checkBox_25.setChecked(False)
        self.lineEdit_21.setText("")
        self.lineEdit_22.setText("")
        self.lineEdit_23.setText("")
        self.lineEdit_24.setText("")
        self.lineEdit_25.setText("")
        self.lineEdit_31.setText("")
        self.button_32.setEnabled(False)
        self.button_33.setEnabled(False)
        self.button_34.setEnabled(False)

    def __initActions(self):
        self.button_31.clicked.connect(self._button_31_clicked)
        self.button_32.clicked.connect(self._button_32_clicked)
        self.button_33.clicked.connect(self._button_33_clicked)
        self.button_34.clicked.connect(self._button_34_clicked)

    def _button_31_clicked(self):
        # 选择文件
        self.file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "选择文件", "", "All files (*.*)")
        # print(self.file)
        if os.path.isfile(self.file):
            self.__file_valid()  # 文件有效
        else:
            self.__file_invalid()  # 文件无效

    def __file_valid(self):
        # 文件有效
        self.lineEdit_31.setText(self.file)
        self.button_32.setEnabled(True)
        self.button_33.setEnabled(False)
        self.button_34.setEnabled(False)
        self.info = CalcFileHash(file=self.file)
        basic = self.info.basic()
        self.lineEdit_11.setText(basic.get("path", ""))
        self.lineEdit_12.setText(basic.get("name", ""))
        self.lineEdit_13.setText(basic.get("size", ""))
        self.lineEdit_14.setText(basic.get("ctime", ""))
        self.lineEdit_15.setText(basic.get("atime", ""))
        self.lineEdit_16.setText(basic.get("mtime", ""))
        self.lineEdit_21.setText("")
        self.lineEdit_22.setText("")
        self.lineEdit_23.setText("")
        self.lineEdit_24.setText("")
        self.lineEdit_25.setText("")

    def __file_invalid(self):
        # 文件无效
        self.__initDatas()

    def _button_32_clicked(self):
        needhash = set()
        if self.checkBox_21.isChecked():
            needhash.add("md5")
        if self.checkBox_22.isChecked():
            needhash.add("sha1")
        if self.checkBox_23.isChecked():
            needhash.add("sha256")
        if self.checkBox_24.isChecked():
            needhash.add("sha384")
        if self.checkBox_25.isChecked():
            needhash.add("sha512")
        hashes = self.info.hashes(needhash)
        self.lineEdit_21.setText(hashes.get("md5", ""))
        self.lineEdit_22.setText(hashes.get("sha1", ""))
        self.lineEdit_23.setText(hashes.get("sha256", ""))
        self.lineEdit_24.setText(hashes.get("sha384", ""))
        self.lineEdit_25.setText(hashes.get("sha512", ""))
        self.button_33.setEnabled(True)
        self.button_34.setEnabled(True)

    def _button_33_clicked(self):
        self.info.copyjson()
        QtWidgets.QMessageBox.about(self, "提示", "\n结果已经按json格式复制到剪切板中！\n")

    def _button_34_clicked(self):
        self.info.copytext()
        QtWidgets.QMessageBox.about(self, "提示", "\n结果已经按text格式复制到剪切板中！\n")


class PicMixZipUI(QtWidgets.QWidget):
    # 图片种子文件合成
    version = "1.0.0"

    def __init__(self):
        super().__init__()
        self.pic = ""
        self.zip = ""
        self.outpic = ""

        self.__initUI()
        self.__initActions()
        self.__initDatas()

    def __initUI(self):
        self.setObjectName("PicMixZipUI")
        self.setFixedSize(600, 300)
        self.setWindowTitle("图片种子文件合成")

        self.groupBox_1 = QtWidgets.QGroupBox(self)
        self.groupBox_1.setGeometry(QtCore.QRect(10, 10, 580, 70))
        self.groupBox_1.setObjectName("groupBox_1")
        self.groupBox_1.setTitle("第一步：准备工作")
        self.label_1 = QtWidgets.QLabel(self.groupBox_1)
        self.label_1.setGeometry(QtCore.QRect(30, 20, 400, 15))
        self.label_1.setObjectName("label_1")
        self.label_1.setText("1、准备好图片（*.png；*.jpg；*.bmp）")
        self.label_2 = QtWidgets.QLabel(self.groupBox_1)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 400, 15))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("2、将种子文件用压缩工具打包（*.zip；*.rar）")

        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 90, 580, 70))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setTitle("第二步：选择图片文件")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 25, 470, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setReadOnly(True)
        self.button_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.button_2.setGeometry(QtCore.QRect(490, 25, 80, 25))
        self.button_2.setObjectName("button_2")
        self.button_2.setText("浏览...")

        self.groupBox_3 = QtWidgets.QGroupBox(self)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 180, 580, 70))
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setTitle("第三步：选择压缩包")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 25, 470, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setReadOnly(True)
        self.button_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.button_3.setGeometry(QtCore.QRect(490, 25, 80, 25))
        self.button_3.setObjectName("button_3")
        self.button_3.setText("浏览...")

        self.button_0 = QtWidgets.QPushButton(self)
        self.button_0.setFont(QtGui.QFont("", 16))
        self.button_0.setGeometry(QtCore.QRect(250, 260, 120, 30))
        self.button_0.setObjectName("button_0")
        self.button_0.setText("生成文件")
        self.button_0.setEnabled(False)

    def __initActions(self):
        self.button_2.clicked.connect(self._button_2_clicked)
        self.button_3.clicked.connect(self._button_3_clicked)
        self.button_0.clicked.connect(self._button_0_clicked)

    def __initDatas(self):
        pass

    def _button_2_clicked(self):
        # 选择图片文件
        self.pic, _ = QtWidgets.QFileDialog.getOpenFileName(self, "选择图片文件", "", "Image files (*.png;*.jpg;*jpeg;*.bmp)")
        # print(self.pic)
        if os.path.isfile(self.pic):
            self.lineEdit_2.setText(self.pic)
            self.__both_valid()
        else:
            self.lineEdit_2.setText("")
            self.__both_valid()

    def _button_3_clicked(self):
        # 选择压缩文件
        self.zip, _ = QtWidgets.QFileDialog.getOpenFileName(self, "选择压缩文件", "", "Zipped files (*.zip;*.rar)")
        # print(self.zip)
        if os.path.isfile(self.zip):
            self.lineEdit_3.setText(self.zip)
            self.__both_valid()
        else:
            self.lineEdit_3.setText("")
            self.__both_valid()

    def __both_valid(self):
        if self.pic and self.zip:
            self.button_0.setEnabled(True)
        else:
            self.button_0.setEnabled(False)

    def __check_pic(self):
        pic_base = os.path.basename(self.pic)
        pic_name = pic_base.split(".")[0]

        zip_base = os.path.basename(self.zip)
        zip_name = zip_base.split(".")[0]

        ext = os.path.splitext(self.pic)[1]
        if ext.lower() == ".png":
            type = "Image file (*.png)"
        elif ext.lower() == ".jpg":
            type = "Image file (*.jpg)"
        elif ext.lower() == ".jpeg":
            type = "Image file (*.jpg)"
        elif ext.lower() == ".bmp":
            type = "Image file (*.bmp)"
        else:
            type = "All files (*.*)"

        output_default = pic_name + "_" + zip_name + ext
        return output_default, type

    def _button_0_clicked(self):
        name, type = self.__check_pic()
        self.outpic, _ = QtWidgets.QFileDialog.getSaveFileName(self, "保存文件", name, type)
        if self.outpic:
            self.__save_output()
        if os.path.isfile(self.outpic):
            QtWidgets.QMessageBox.about(self, "提示", "\n合成成功！\n")
        else:
            QtWidgets.QMessageBox.critical(self, "警告", "\n合成失败！\n")

    def __save_output(self):
        pmz = PicMixZip(pic=self.pic, zip=self.zip, store=self.outpic)
        pmz.run()
