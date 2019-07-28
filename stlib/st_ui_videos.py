import os
import sys

from PySide2 import QtCore, QtGui, QtWidgets

from .st_videos import VideoOverview


class VideoOverviewUI(QtWidgets.QWidget):
    version = "1.0.1"

    def __init__(self):
        super().__init__()
        self.video = ""
        self.output = ""

        self.__init_ui()
        self.__init_actions()
        self.__init_datas()

    def __init_ui(self):
        self.setFixedSize(600, 220)
        self.setWindowTitle("视频概览图")

        self.layout_1 = QtWidgets.QWidget(self)
        self.layout_1.setGeometry(QtCore.QRect(10, 10, 580, 60))
        self.layout_1.setObjectName("layout_1")
        self.gLayout_1 = QtWidgets.QGridLayout(self.layout_1)
        self.gLayout_1.setContentsMargins(0, 0, 0, 0)
        self.gLayout_1.setObjectName("gLayout_1")
        self.label_11 = QtWidgets.QLabel(self.layout_1)
        self.label_11.setObjectName("label_11")
        self.label_11.setText("视频文件")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.layout_1)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_11.setReadOnly(True)
        self.button_11 = QtWidgets.QPushButton(self.layout_1)
        self.button_11.setObjectName("button_11")
        self.button_11.setText("打开...")
        self.label_12 = QtWidgets.QLabel(self.layout_1)
        self.label_12.setObjectName("label_12")
        self.label_12.setText("图片输出")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.layout_1)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_12.setReadOnly(True)
        self.gLayout_1.addWidget(self.label_11, 0, 0, 1, 1)
        self.gLayout_1.addWidget(self.lineEdit_11, 0, 1, 1, 1)
        self.gLayout_1.addWidget(self.button_11, 0, 2, 1, 1)
        self.gLayout_1.addWidget(self.label_12, 1, 0, 1, 1)
        self.gLayout_1.addWidget(self.lineEdit_12, 1, 1, 1, 1)

        self.layout_2 = QtWidgets.QWidget(self)
        self.layout_2.setGeometry(QtCore.QRect(10, 80, 200, 120))
        self.layout_2.setObjectName("layout_2")
        self.gLayout_2 = QtWidgets.QGridLayout(self.layout_2)
        self.gLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gLayout_2.setObjectName("gLayout_2")
        self.label_21 = QtWidgets.QLabel(self.layout_2)
        self.label_21.setObjectName("label_21")
        self.label_21.setText("缩略图分辨率")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.comboBox_21 = QtWidgets.QComboBox(self.layout_2)
        self.comboBox_21.setObjectName("comboBox_21")
        self.label_22 = QtWidgets.QLabel(self.layout_2)
        self.label_22.setObjectName("label_22")
        self.label_22.setText("每行布局个数")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.comboBox_22 = QtWidgets.QComboBox(self.layout_2)
        self.comboBox_22.setObjectName("comboBox_22")
        self.label_23 = QtWidgets.QLabel(self.layout_2)
        self.label_23.setObjectName("label_23")
        self.label_23.setText("行数")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.comboBox_23 = QtWidgets.QComboBox(self.layout_2)
        self.comboBox_23.setObjectName("comboBox_23")
        self.checkBox_21 = QtWidgets.QCheckBox(self.layout_2)
        self.checkBox_21.setObjectName("checkBox_21")
        self.checkBox_21.setText("显示序号")
        self.checkBox_22 = QtWidgets.QCheckBox(self.layout_2)
        self.checkBox_22.setObjectName("checkBox_22")
        self.checkBox_22.setText("显示时刻")
        self.gLayout_2.addWidget(self.label_21, 0, 0, 1, 1)
        self.gLayout_2.addWidget(self.comboBox_21, 0, 1, 1, 1)
        self.gLayout_2.addWidget(self.label_22, 1, 0, 1, 1)
        self.gLayout_2.addWidget(self.comboBox_22, 1, 1, 1, 1)
        self.gLayout_2.addWidget(self.label_23, 2, 0, 1, 1)
        self.gLayout_2.addWidget(self.comboBox_23, 2, 1, 1, 1)
        self.gLayout_2.addWidget(self.checkBox_21, 3, 1, 1, 1)
        self.gLayout_2.addWidget(self.checkBox_22, 4, 1, 1, 1)

        self.button_1 = QtWidgets.QPushButton(self)
        self.button_1.setGeometry(QtCore.QRect(300, 150, 75, 25))
        self.button_1.setObjectName("button_1")
        self.button_1.setText("获取概览图")
        self.button_1.setEnabled(False)

    def __init_actions(self):
        self.button_1.clicked.connect(self._button_1_clicked)
        self.button_11.clicked.connect(self._button_11_clicked)

    def __init_datas(self):
        self.comboBox_21.addItems(["480 * 270", "384 * 216"])
        self.comboBox_21_desc = {0: (480, 270), 1: (384, 216), }
        self.comboBox_21.setCurrentIndex(0)
        self.comboBox_22.addItems(["3", "4", "5"])
        self.comboBox_22_desc = {0: 3, 1: 4, 2: 5, }
        self.comboBox_22.setCurrentIndex(1)
        self.comboBox_23.addItems(["3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"])
        self.comboBox_23_desc = {0: 3, 1: 4, 2: 5, 3: 6, 4: 7, 5: 8, 6: 9, 7: 10, 8: 11, 9: 12, 10: 13, 11: 14, 12: 15, }
        self.comboBox_23.setCurrentIndex(7)
        self.lineEdit_11.setText(self.video)
        self.lineEdit_12.setText(self.output)
        self.checkBox_22.setChecked(True)

    def _button_1_clicked(self):
        video = self.video
        output = self.output
        thumb_dpi = self.comboBox_21_desc[self.comboBox_21.currentIndex()]
        w = self.comboBox_22_desc[self.comboBox_22.currentIndex()]
        h = self.comboBox_23_desc[self.comboBox_23.currentIndex()]
        if self.checkBox_21.isChecked():
            show_number = True
        else:
            show_number = False
        if self.checkBox_22.isChecked():
            show_time = True
        else:
            show_time = False

        vo = VideoOverview(
                video=video,
                output=output,
                thumb_dpi=thumb_dpi,
                w=w,
                h=h,
                show_number=show_number,
                show_time=show_time
                )
        result = vo.run()
        del vo

        if not result:
            msgBox = QtWidgets.QMessageBox.question(self, "提示", "\n概览图制作完成！\n\n是否打开图片？\n")
            if msgBox == QtWidgets.QMessageBox.Yes:
                self._open_image()
        else:
            QtWidgets.QMessageBox.critical(self, "警告", "\n未完成！\n\n视频读取失败！\n")

    def _button_11_clicked(self):
        # 选择文件
        self.video, _ = QtWidgets.QFileDialog.getOpenFileName(self, "选择视频文件", "", "Video files (*.mp4;*.avi;*.mkv)")
        if os.path.isfile(self.video):
            self.__file_valid()
        else:
            self.__file_invalid()

    def __file_valid(self):
        # 文件有效
        # 激活各种关联组件，预览图像
        self.button_1.setEnabled(True)
        self.lineEdit_11.setText(self.video)
        self.output = self.video + ".overview.png"
        self.lineEdit_12.setText(self.output)

    def __file_invalid(self):
        # 文件无效
        # 灭活各种关联组件
        self.button_1.setEnabled(False)
        self.lineEdit_11.setText("")
        self.lineEdit_12.setText("")
        self.output = ""

    def _open_image(self):
        # 调用系统直接打开一个文件，并非在资源管理器中定位
        if self.output:
            target = "file:" + self.output  # 前边必须指定协议，file:
            QtGui.QDesktopServices.openUrl(QtCore.QUrl(target, QtCore.QUrl.TolerantMode))
