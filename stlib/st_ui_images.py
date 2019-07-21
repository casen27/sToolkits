# gif处理子功能的界面

import os

from PySide2 import QtCore, QtGui, QtWidgets

from .st_images import GIFSpliter


class ColorBoardUI(QtWidgets.QWidget):
    # 颜色板
    version = "1.0.0"

    def __init__(self, r=0, g=0, b=0):
        super().__init__()
        self._r = self._clean_rgb(r)
        self._g = self._clean_rgb(g)
        self._b = self._clean_rgb(b)
        self._string = "#"

        self.__initUI()
        self.__initActions()
        self.__initDatas()

    def __initUI(self):
        self.setFixedSize(320, 300)
        self.setWindowTitle("RGB色彩筛选板")

        self.mdiArea = QtWidgets.QMdiArea(self)
        self.mdiArea.setGeometry(QtCore.QRect(10, 10, 300, 120))
        self.mdiArea.setStyleSheet("border: 1px solid black;")

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 120, 30))
        self.lineEdit.setFont(QtGui.QFont("", 16))
        self.lineEdit.setReadOnly(True)

        self.widget_1 = QtWidgets.QWidget(self)
        self.widget_1.setGeometry(QtCore.QRect(10, 140, 300, 150))
        self.gLayout_1 = QtWidgets.QGridLayout(self.widget_1)
        self.gLayout_1.setContentsMargins(0, 0, 0, 0)

        self.label_r = QtWidgets.QLabel(self.widget_1)
        self.label_g = QtWidgets.QLabel(self.widget_1)
        self.label_b = QtWidgets.QLabel(self.widget_1)
        self.slider_r = QtWidgets.QSlider(self.widget_1)
        self.slider_r.setMinimum(0)
        self.slider_r.setMaximum(255)
        self.slider_r.setOrientation(QtCore.Qt.Horizontal)
        self.slider_g = QtWidgets.QSlider(self.widget_1)
        self.slider_g.setMinimum(0)
        self.slider_g.setMaximum(255)
        self.slider_g.setOrientation(QtCore.Qt.Horizontal)
        self.slider_b = QtWidgets.QSlider(self.widget_1)
        self.slider_b.setMinimum(0)
        self.slider_b.setMaximum(255)
        self.slider_b.setOrientation(QtCore.Qt.Horizontal)
        self.lcd_r = QtWidgets.QLCDNumber(self.widget_1)
        self.lcd_r.setSegmentStyle(QtWidgets.QLCDNumber.Flat)  # Mac系统需要加上，否则下面的color不生效。
        self.lcd_r.setStyleSheet("border: 1px solid black; color:red;")
        self.lcd_g = QtWidgets.QLCDNumber(self.widget_1)
        self.lcd_g.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_g.setStyleSheet("border: 1px solid black; color:green;")
        self.lcd_b = QtWidgets.QLCDNumber(self.widget_1)
        self.lcd_b.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_b.setStyleSheet("border: 1px solid black; color:blue;")
        self.checkBox_1 = QtWidgets.QCheckBox(self.widget_1)
        self.checkBox_1.setText("灰度锁定")
        self.checkBox_1.setChecked(False)
        self.label_1 = QtWidgets.QLabel(self.widget_1)
        self.label_1.setText("（提示：拖动滑块到大概位置，按方向键可以微调）")
        self.gLayout_1.addWidget(self.label_r,  0, 0, 1, 1)
        self.gLayout_1.addWidget(self.slider_r, 0, 1, 1, 5)
        self.gLayout_1.addWidget(self.lcd_r,    0, 6, 1, 1)
        self.gLayout_1.addWidget(self.label_g,  1, 0, 1, 1)
        self.gLayout_1.addWidget(self.slider_g, 1, 1, 1, 5)
        self.gLayout_1.addWidget(self.lcd_g,    1, 6, 1, 1)
        self.gLayout_1.addWidget(self.label_b,  2, 0, 1, 1)
        self.gLayout_1.addWidget(self.slider_b, 2, 1, 1, 5)
        self.gLayout_1.addWidget(self.lcd_b,    2, 6, 1, 1)
        self.gLayout_1.addWidget(self.checkBox_1, 3, 1, 1, 2)
        self.gLayout_1.addWidget(self.label_1, 4, 0, 1, 7)

    def __initActions(self):
        self.slider_r.valueChanged[int].connect(self._slider_r_changed)
        self.slider_g.valueChanged[int].connect(self._slider_g_changed)
        self.slider_b.valueChanged[int].connect(self._slider_b_changed)
        self.checkBox_1.stateChanged.connect(self._lock_gray)

    def __initDatas(self):
        self.lineEdit.setText(self._string)
        self.label_r.setText("Red")
        self.label_g.setText("Green")
        self.label_b.setText("Blue")
        self.slider_r.setValue(self._r)
        self.slider_g.setValue(self._g)
        self.slider_b.setValue(self._b)
        self.lcd_r.display(self._r)
        self.lcd_g.display(self._g)
        self.lcd_b.display(self._b)
        self._change_board()

    def _lock_gray(self):
        if self.checkBox_1.isChecked():
            # 锁定灰度 r = g = b
            self.slider_g.setEnabled(False)
            self.slider_b.setEnabled(False)
            self._g = self._r
            self._b = self._r
            self.slider_g.setValue(self._g)
            self.slider_b.setValue(self._b)
            self._change_board()
        else:
            # 解锁
            self.slider_g.setEnabled(True)
            self.slider_b.setEnabled(True)

    def _slider_r_changed(self, value):
        self._r = value
        self.lcd_r.display(self._r)
        if self.checkBox_1.isChecked():
            self._lock_gray()
        else:
            self._change_board()

    def _slider_g_changed(self, value):
        self._g = value
        self.lcd_g.display(self._g)
        if not self.checkBox_1.isChecked():
            self._change_board()

    def _slider_b_changed(self, value):
        self._b = value
        self.lcd_b.display(self._b)
        if not self.checkBox_1.isChecked():
            self._change_board()

    def _change_board(self):
        self._string = "#" + hex(self._r)[2::].upper().rjust(2, "0") + hex(self._g)[2::].upper().rjust(2, "0") + hex(self._b)[2::].upper().rjust(2, "0")
        self.lineEdit.setText(self._string)
        self.brush = QtGui.QBrush(QtGui.QColor(self._r, self._g, self._b))
        self.mdiArea.setBackground(self.brush)

    def _clean_rgb(self, data):
        if isinstance(data, int):
            if data >= 0 and data <= 255:
                return data
        elif isinstance(data, float):
            if data >= 0.0 and data <= 1.0:
                return int(data * 255)
        return 0


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

    def __initUI(self):
        self.setFixedSize(620, 600)
        self.setWindowTitle("GIF分割器")

        self.label_01 = QtWidgets.QLabel(self)
        self.label_01.setGeometry(QtCore.QRect(10, 10, 600, 450))
        self.label_01.setScaledContents(False)
        self.label_01.setAlignment(QtCore.Qt.AlignCenter)
        self.label_01.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_01.setText("（预览窗口）")
        self.label_01.setStyleSheet("border: 1px solid black;")

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
        self.comboBox_1.addItems(["*.png", "*.bmp", "*.tif"])
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
        self.file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "选择GIF动图", "", "GIF files (*.gif)")
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
        work_dir_default = self.lineEdit_12.text()
        work_dir = QtWidgets.QFileDialog.getExistingDirectory(self, "修改存储目录", work_dir_default)
        if work_dir:
            self.__new_dir_valid(work_dir)
        else:
            # self.__new_dir_invalid()  # 点了取消导致新文件为空
            pass

    def __new_dir_valid(self, work_dir):
        name = os.path.basename(self.file)
        fullpath = os.path.join(work_dir, name)
        self.lineEdit_12.setText(self._get_output_dir(fullpath))

    def _get_output_dir(self, fullpath):
        new_dir, _ = os.path.splitext(fullpath)
        self.output = new_dir
        return new_dir

    def _button_1_clicked(self):
        # 拆分GIF
        gif = self.lineEdit_11.text()
        work_dir = self.lineEdit_12.text()
        format = self.comboBox_1.currentText().replace("*", "")
        gs = GIFSpliter(gif=gif, work_dir=work_dir, format=format)
        result = gs.run()
        if result:
            msgBox = QtWidgets.QMessageBox.question(self, "提示", "\n图片分割完成！\n\n是否打开输出目录？\n")
            if msgBox == QtWidgets.QMessageBox.Yes:
                self._show_dir()
        else:
            QtWidgets.QMessageBox.critical(self, "警告", "\n未完成！\n\n图片读取失败！\n")

    def _show_dir(self):
        # 在资源管理器打开一个目录
        # 调用系统直接打开一个文件，并非在资源管理器中定位
        if self.output:
            target = "file:" + self.output  # 前边必须指定协议，file:
            QtGui.QDesktopServices.openUrl(QtCore.QUrl(target, QtCore.QUrl.TolerantMode))
