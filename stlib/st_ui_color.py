# pyqt5  颜色相关其他子功能的界面

import os

from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.setFixedSize(320, 280)
        self.setWindowTitle("24bit真彩色")

        self.mdiArea = QtWidgets.QMdiArea(self)
        self.mdiArea.setGeometry(QtCore.QRect(10, 10, 300, 120))
        self.mdiArea.setStyleSheet("border: 1px solid black;")

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 100, 30))
        self.lineEdit.setFont(QtGui.QFont("",16))
        self.lineEdit.setReadOnly(True)

        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(10, 140, 300, 90))
        self.gLayout = QtWidgets.QGridLayout(self.widget)
        self.gLayout.setContentsMargins(0, 0, 0, 0)

        self.label_r = QtWidgets.QLabel(self.widget)
        self.label_g = QtWidgets.QLabel(self.widget)
        self.label_b = QtWidgets.QLabel(self.widget)
        self.slider_r = QtWidgets.QSlider(self.widget)
        self.slider_r.setMinimum(0)
        self.slider_r.setMaximum(255)
        self.slider_r.setOrientation(QtCore.Qt.Horizontal)
        self.slider_g = QtWidgets.QSlider(self.widget)
        self.slider_g.setMinimum(0)
        self.slider_g.setMaximum(255)
        self.slider_g.setOrientation(QtCore.Qt.Horizontal)
        self.slider_b = QtWidgets.QSlider(self.widget)
        self.slider_b.setMinimum(0)
        self.slider_b.setMaximum(255)
        self.slider_b.setOrientation(QtCore.Qt.Horizontal)
        self.lcd_r = QtWidgets.QLCDNumber(self.widget)
        self.lcd_r.setSegmentStyle(QtWidgets.QLCDNumber.Flat)  # Mac系统需要加上，否则下面的color不生效。
        self.lcd_r.setStyleSheet("border: 1px solid black; color:red;")
        self.lcd_g = QtWidgets.QLCDNumber(self.widget)
        self.lcd_g.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_g.setStyleSheet("border: 1px solid black; color:green;")
        self.lcd_b = QtWidgets.QLCDNumber(self.widget)
        self.lcd_b.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_b.setStyleSheet("border: 1px solid black; color:blue;")
        self.gLayout.addWidget(self.label_r, 0, 0, 1, 1)
        self.gLayout.addWidget(self.slider_r, 0, 1, 1, 1)
        self.gLayout.addWidget(self.lcd_r, 0, 2, 1, 1)
        self.gLayout.addWidget(self.label_g, 1, 0, 1, 1)
        self.gLayout.addWidget(self.slider_g, 1, 1, 1, 1)
        self.gLayout.addWidget(self.lcd_g, 1, 2, 1, 1)
        self.gLayout.addWidget(self.label_b, 2, 0, 1, 1)
        self.gLayout.addWidget(self.slider_b, 2, 1, 1, 1)
        self.gLayout.addWidget(self.lcd_b, 2, 2, 1, 1)

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setGeometry(QtCore.QRect(10, 240, 300, 23))
        self.label_1.setText("（提示：拖动滑块到大概位置，按 ← → 键可以微调）")

    def __initActions(self):
        self.slider_r.valueChanged[int].connect(self._slider_r_changed)
        self.slider_g.valueChanged[int].connect(self._slider_g_changed)
        self.slider_b.valueChanged[int].connect(self._slider_b_changed)

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

    def _slider_r_changed(self, value):
        self._r = value
        self.lcd_r.display(self._r)
        self._change_board()

    def _slider_g_changed(self, value):
        self._g = value
        self.lcd_g.display(self._g)
        self._change_board()

    def _slider_b_changed(self, value):
        self._b = value
        self.lcd_b.display(self._b)
        self._change_board()

    def _change_board(self):
        self._string = "#" + hex(self._r)[2::].upper().rjust(2, "0") + hex(self._g)[2::].upper().rjust(2, "0") + hex(self._b)[2::].upper().rjust(2, "0")
        self.brush = QtGui.QBrush(QtGui.QColor(self._r, self._g, self._b))
        self.lineEdit.setText(self._string)
        self.mdiArea.setBackground(self.brush)

    def _clean_rgb(self, data):
        if isinstance(data, int):
            if data >= 0 and data <= 255:
                return data
        elif isinstance(data, float):
            if data >= 0.0 and data <= 1.0:
                return int(data * 255)
        return 0
