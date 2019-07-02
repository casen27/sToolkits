# 颜色板

from PyQt5 import QtCore, QtGui, QtWidgets


class ColorBoard(QtWidgets.QWidget):
    version = "v1.0.0"

    def __init__(self, parent=None, r=0, g=0, b=0):
        super().__init__()
        self.parent = parent
        self._r = self._clean_rgb(r)
        self._g = self._clean_rgb(g)
        self._b = self._clean_rgb(b)
        self._string = ""

        self.__initUI()
        self.__initDatas()

    def __initUI(self):
        self.setObjectName("ColorBoard")
        self.setFixedSize(300, 240)
        self.setWindowTitle("24bit真彩色")

        self.mdiArea = QtWidgets.QMdiArea(self)
        self.mdiArea.setGeometry(QtCore.QRect(10, 10, 280, 120))
        self.mdiArea.setObjectName("mdiArea")
        self.mdiArea.setStyleSheet("border: 1px solid black;")

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 80, 30))
        font1 = QtGui.QFont()
        font1.setPointSize(16)
        self.lineEdit.setFont(font1)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")

        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(10, 140, 280, 90))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.label_r = QtWidgets.QLabel(self.widget)
        self.label_r.setObjectName("label_r")
        self.label_g = QtWidgets.QLabel(self.widget)
        self.label_g.setObjectName("label_g")
        self.label_b = QtWidgets.QLabel(self.widget)
        self.label_b.setObjectName("label_b")

        self.slider_r = QtWidgets.QSlider(self.widget)
        self.slider_r.setMinimum(0)
        self.slider_r.setMaximum(255)
        self.slider_r.setObjectName("slider_r")
        self.slider_r.setOrientation(QtCore.Qt.Horizontal)
        self.slider_r.valueChanged[int].connect(self._slider_r_changed)
        self.slider_g = QtWidgets.QSlider(self.widget)
        self.slider_g.setMinimum(0)
        self.slider_g.setMaximum(255)
        self.slider_g.setObjectName("slider_g")
        self.slider_g.setOrientation(QtCore.Qt.Horizontal)
        self.slider_g.valueChanged[int].connect(self._slider_g_changed)
        self.slider_b = QtWidgets.QSlider(self.widget)
        self.slider_b.setMinimum(0)
        self.slider_b.setMaximum(255)
        self.slider_b.setObjectName("slider_b")
        self.slider_b.setOrientation(QtCore.Qt.Horizontal)
        self.slider_b.valueChanged[int].connect(self._slider_b_changed)

        self.lcd_r = QtWidgets.QLCDNumber(self.widget)
        self.lcd_r.setObjectName("lcd_r")
        self.lcd_r.setSegmentStyle(QtWidgets.QLCDNumber.Flat)  # Mac系统需要加上，否则下面的color不生效。
        self.lcd_r.setStyleSheet("border: 1px solid black; color:red;")
        self.lcd_g = QtWidgets.QLCDNumber(self.widget)
        self.lcd_g.setObjectName("lcd_g")
        self.lcd_g.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_g.setStyleSheet("border: 1px solid black; color:green;")
        self.lcd_b = QtWidgets.QLCDNumber(self.widget)
        self.lcd_b.setObjectName("lcd_b")
        self.lcd_b.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_b.setStyleSheet("border: 1px solid black; color:blue;")
        self.gridLayout.addWidget(self.label_r, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.label_g, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.label_b, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.slider_r, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.slider_g, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.slider_b, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.lcd_r, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.lcd_g, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.lcd_b, 2, 2, 1, 1)

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
        self._string = hex(self._r)[2::].upper().rjust(2, "0") + hex(self._g)[2::].upper().rjust(2, "0") + hex(self._b)[2::].upper().rjust(2, "0")
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
