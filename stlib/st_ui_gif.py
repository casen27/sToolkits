# pyqt5  gif处理子功能的界面

import os

from PyQt5 import QtCore, QtGui, QtWidgets

from .st_gif import GIFSpliter


class GIFSpliterUI(QtWidgets.QWidget):
    version = "1.0.2"

    def __init__(self):
        super().__init__()
        self.file = ""
        self.output = ""
        self.rank = 1

        self.__initUI()
        self.__initActions()
        self.__initDatas()
        QtCore.QMetaObject.connectSlotsByName(self)

    def __initUI(self):
        self.setFixedSize(620, 600)
        self.setWindowTitle("GIF分割器")

        self.label_01 = QtWidgets.QLabel(self)
        self.label_01.setGeometry(QtCore.QRect(10, 10, 600, 450))
        self.label_01.setScaledContents(False)
        self.label_01.setAlignment(QtCore.Qt.AlignCenter)
        self.label_01.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_01.setText("（预览窗口）")

        self.layout_1 = QtWidgets.QWidget(self)
        self.layout_1.setGeometry(QtCore.QRect(10, 470, 600, 120))
        self.gLayout_1 = QtWidgets.QGridLayout(self.layout_1)
        self.gLayout_1.setContentsMargins(0, 0, 0, 0)

        self.label_11 = QtWidgets.QLabel(self.layout_1)
        self.label_11.setText("GIF文件")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.layout_1)
        self.lineEdit_11.setReadOnly(True)
        self.button_11 = QtWidgets.QPushButton(self.layout_1)
        self.button_11.setText("选择文件")

        self.label_12 = QtWidgets.QLabel(self.layout_1)
        self.label_12.setText("输出目录")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.layout_1)
        self.lineEdit_12.setReadOnly(True)
        self.button_12 = QtWidgets.QPushButton(self.layout_1)
        self.button_12.setText("更改目录")
        self.button_12.setEnabled(False)
        self.gLayout_1.addWidget(self.label_11, 0, 0, 1, 1)
        self.gLayout_1.addWidget(self.lineEdit_11, 0, 1, 1, 4)
        self.gLayout_1.addWidget(self.button_11, 0, 5, 1, 1)
        self.gLayout_1.addWidget(self.label_12, 1, 0, 1, 1)
        self.gLayout_1.addWidget(self.lineEdit_12, 1, 1, 1, 4)
        self.gLayout_1.addWidget(self.button_12, 1, 5, 1, 1)

        self.label_13 = QtWidgets.QLabel(self.layout_1)
        self.label_13.setText("输出格式")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.comboBox_1 = QtWidgets.QComboBox(self.layout_1)
        self.comboBox_1.addItems(["*.png","*.bmp","*.tif"])
        self.button_1 = QtWidgets.QPushButton(self.layout_1)
        self.button_1.setText("拆分")
        self.button_1.setEnabled(False)
        self.button_0 = QtWidgets.QPushButton(self.layout_1)
        self.button_0.setText("关闭")

        self.gLayout_1.addWidget(self.label_13, 2, 0, 1, 1)
        self.gLayout_1.addWidget(self.comboBox_1, 2, 4, 1, 1)
        self.gLayout_1.addWidget(self.button_1, 2, 5, 1, 1)
        self.gLayout_1.addWidget(self.button_0, 3, 5, 1, 1)

    def __initActions(self):
        self.button_1.clicked.connect(self._button_1_clicked)
        self.button_11.clicked.connect(self._button_11_clicked)
        self.button_12.clicked.connect(self._button_12_clicked)
        self.button_0.clicked.connect(self.close)

    def __initDatas(self):
        self.lineEdit_11.setText(self.file)

    def _button_11_clicked(self):
        # 选择文件
        self.file, _ = QtWidgets.QFileDialog.getOpenFileName(self,"选择GIF动图","","GIF files (*.gif)")
        # print(self.file)
        if os.path.isfile(self.file):
            self.__file_valid()
        else:
            self.__file_invalid()

    def __file_valid(self):
        # gif有效
        # 激活各种关联组件，预览图像
        self.button_12.setEnabled(True)
        self.button_1.setEnabled(True)
        self.lineEdit_11.setText(self.file)
        self.lineEdit_12.setText(self._get_output_dir(self.file))
        self.__file_preview(status=True)  # 播放gif动画

    def __file_invalid(self):
        # gif无效
        # 灭活各种关联组件
        self.button_12.setEnabled(False)
        self.button_1.setEnabled(False)
        self.lineEdit_11.setText("")
        self.lineEdit_12.setText("")
        self.output = ""
        self.__file_preview(status=False)

    def __file_preview(self, status=False):
        if status:
            self.gif = QtGui.QMovie(self.file)
            self.label_01.setMovie(self.gif)
            self.gif.start()
        else:
            self.gif = None
            self.label_01.setText("（预览窗口）")

    def _button_12_clicked(self):
        # 修改输出目录
        # 由于分割后的图片数量较多，在选定的目录下，新建一个空的同名目录
        workDir_default = self.lineEdit_12.text()
        workDir = QtWidgets.QFileDialog.getExistingDirectory(self, "修改存储目录", workDir_default)
        if workDir:
            self.__new_dir_valid(workDir)
        else:
            # self.__new_dir_invalid()  # 点了取消导致新文件为空
            pass

    def __new_dir_valid(self, workDir):
        _, name = os.path.split(self.file)
        fullpath = os.path.join(workDir,name)
        self.lineEdit_12.setText(self._get_output_dir(fullpath))

    def _get_output_dir(self, fullpath):
        new_dir, _ = os.path.splitext(fullpath)
        self.output = new_dir
        return new_dir

    def _button_1_clicked(self):
        # 拆分GIF
        gif = self.lineEdit_11.text()
        workDir = self.lineEdit_12.text()
        format = self.comboBox_1.currentText().replace("*","")
        gs = GIFSpliter(gif=gif, workDir=workDir, format=format)
        result = gs.run()
        if result:
            msgBox = QtWidgets.QMessageBox.question(self, "提示", "\n图片分割完成！\n\n是否打开输出目录？\n")
            if msgBox == QtWidgets.QMessageBox.Yes:
                self._show_dir()
        else:
            msgBox = QtWidgets.QMessageBox.critical(self, "警告", "\n未完成！\n\n图片读取失败！\n")

    def _show_dir(self):
        # 在资源管理器打开一个目录
        # 调用系统直接打开一个文件，并非在资源管理器中定位
        if self.output:
            target = "file:" + self.output  # 前边必须指定协议，file:
            QtGui.QDesktopServices.openUrl(QtCore.QUrl(target, QtCore.QUrl.TolerantMode))
