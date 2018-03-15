
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(805, 616)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.sourcemeter_tab = QtGui.QWidget()
        self.sourcemeter_tab.setObjectName(_fromUtf8("sourcemeter_tab"))
        self.pushButton = QtGui.QPushButton(self.sourcemeter_tab)
        self.pushButton.setGeometry(QtCore.QRect(660, 160, 85, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.sourcemeter_tab)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 400, 81, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.sourcemeter_tab)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 400, 99, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.lineEdit = QtGui.QLineEdit(self.sourcemeter_tab)
        self.lineEdit.setGeometry(QtCore.QRect(420, 280, 51, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.sourcemeter_tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 340, 51, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_4 = QtGui.QLabel(self.sourcemeter_tab)
        self.label_4.setGeometry(QtCore.QRect(530, 340, 101, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_4 = QtGui.QPushButton(self.sourcemeter_tab)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 450, 111, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label_5 = QtGui.QLabel(self.sourcemeter_tab)
        self.label_5.setGeometry(QtCore.QRect(30, 110, 291, 191))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("github/Group-F/GUI/sourcerer.png")))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalScrollBar = QtGui.QScrollBar(self.sourcemeter_tab)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(500, 50, 231, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setMaximum(15)
        self.horizontalScrollBar.setPageStep(1)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName(_fromUtf8("horizontalScrollBar"))
        self.label_2 = QtGui.QLabel(self.sourcemeter_tab)
        self.label_2.setGeometry(QtCore.QRect(450, 50, 16, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(self.sourcemeter_tab)
        self.label.setGeometry(QtCore.QRect(330, 50, 81, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_9 = QtGui.QLabel(self.sourcemeter_tab)
        self.label_9.setGeometry(QtCore.QRect(200, 380, 68, 17))
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_3 = QtGui.QLabel(self.sourcemeter_tab)
        self.label_3.setGeometry(QtCore.QRect(520, 280, 131, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.radioButton = QtGui.QRadioButton(self.sourcemeter_tab)
        self.radioButton.setGeometry(QtCore.QRect(420, 110, 141, 23))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.sourcemeter_tab)
        self.radioButton_2.setGeometry(QtCore.QRect(420, 150, 112, 23))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.sourcemeter_tab)
        self.radioButton_3.setGeometry(QtCore.QRect(420, 190, 112, 23))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.progressBar = QtGui.QProgressBar(self.sourcemeter_tab)
        self.progressBar.setGeometry(QtCore.QRect(90, 370, 211, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.pushButton.raise_()
        self.horizontalScrollBar.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.label_4.raise_()
        self.pushButton_4.raise_()
        self.label_5.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.label_9.raise_()
        self.label_3.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.radioButton_3.raise_()
        self.progressBar.raise_()
        self.tabWidget.addTab(self.sourcemeter_tab, _fromUtf8(""))
        self.arduino_tab = QtGui.QWidget()
        self.arduino_tab.setObjectName(_fromUtf8("arduino_tab"))
        self.pushButton_5 = QtGui.QPushButton(self.arduino_tab)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 60, 71, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.arduino_tab)
        self.pushButton_6.setGeometry(QtCore.QRect(250, 60, 71, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.arduino_tab)
        self.pushButton_7.setGeometry(QtCore.QRect(370, 200, 99, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.lineEdit_3 = QtGui.QLineEdit(self.arduino_tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 140, 61, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_6 = QtGui.QLabel(self.arduino_tab)
        self.label_6.setGeometry(QtCore.QRect(100, 60, 68, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.arduino_tab)
        self.label_7.setGeometry(QtCore.QRect(180, 140, 101, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.line = QtGui.QFrame(self.arduino_tab)
        self.line.setGeometry(QtCore.QRect(0, 90, 751, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_8 = QtGui.QLabel(self.arduino_tab)
        self.label_8.setGeometry(QtCore.QRect(90, 110, 68, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lineEdit_4 = QtGui.QLineEdit(self.arduino_tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 200, 61, 25))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_10 = QtGui.QLabel(self.arduino_tab)
        self.label_10.setGeometry(QtCore.QRect(180, 260, 81, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.lineEdit_5 = QtGui.QLineEdit(self.arduino_tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 260, 61, 25))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.label_11 = QtGui.QLabel(self.arduino_tab)
        self.label_11.setGeometry(QtCore.QRect(180, 200, 81, 17))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.tabWidget.addTab(self.arduino_tab, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.horizontalScrollBar, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_2.setNum)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Apply", None))
        self.pushButton_2.setText(_translate("MainWindow", "Start", None))
        self.pushButton_3.setText(_translate("MainWindow", "Stop", None))
        self.label_4.setText(_translate("MainWindow", "Total readings", None))
        self.pushButton_4.setText(_translate("MainWindow", "Export reading", None))
        self.label_2.setText(_translate("MainWindow", "0", None))
        self.label.setText(_translate("MainWindow", "Amplitude", None))
        self.label_3.setText(_translate("MainWindow", "Time duration", None))
        self.radioButton.setText(_translate("MainWindow", "Constant Voltage", None))
        self.radioButton_2.setText(_translate("MainWindow", "Sine pulse", None))
        self.radioButton_3.setText(_translate("MainWindow", "Cosine pulse", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sourcemeter_tab), _translate("MainWindow", "Sourcemeter", None))
        self.pushButton_5.setText(_translate("MainWindow", "On", None))
        self.pushButton_6.setText(_translate("MainWindow", "Off", None))
        self.pushButton_7.setText(_translate("MainWindow", "Apply", None))
        self.label_6.setText(_translate("MainWindow", "LED", None))
        self.label_7.setText(_translate("MainWindow", "Time duration", None))
        self.label_8.setText(_translate("MainWindow", "Pulse", None))
        self.label_10.setText(_translate("MainWindow", "Duty Cycle", None))
        self.label_11.setText(_translate("MainWindow", "Time period", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.arduino_tab), _translate("MainWindow", "Arduino", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Page", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

