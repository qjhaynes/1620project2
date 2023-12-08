# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(220, 230)
        MainWindow.setMinimumSize(QtCore.QSize(220, 230))
        MainWindow.setMaximumSize(QtCore.QSize(220, 230))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_volume_up = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_volume_up.setGeometry(QtCore.QRect(120, 60, 91, 23))
        self.button_volume_up.setObjectName("button_volume_up")
        self.button_volume_down = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_volume_down.setGeometry(QtCore.QRect(120, 120, 91, 23))
        self.button_volume_down.setObjectName("button_volume_down")
        self.label_volume = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_volume.setGeometry(QtCore.QRect(140, 90, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_volume.setFont(font)
        self.label_volume.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_volume.setObjectName("label_volume")
        self.label_channel = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_channel.setGeometry(QtCore.QRect(30, 90, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_channel.setFont(font)
        self.label_channel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_channel.setObjectName("label_channel")
        self.button_channel_up = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_channel_up.setGeometry(QtCore.QRect(10, 60, 91, 23))
        self.button_channel_up.setObjectName("button_channel_up")
        self.button_channel_down = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_channel_down.setGeometry(QtCore.QRect(10, 120, 91, 23))
        self.button_channel_down.setObjectName("button_channel_down")
        self.button_power = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_power.setGeometry(QtCore.QRect(70, 10, 81, 23))
        self.button_power.setObjectName("button_power")
        self.button_mute = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_mute.setGeometry(QtCore.QRect(74, 170, 81, 23))
        self.button_mute.setObjectName("button_mute")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 220, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TV Remote"))
        self.button_volume_up.setText(_translate("MainWindow", "Volume Up"))
        self.button_volume_down.setText(_translate("MainWindow", "Volume Down"))
        self.label_volume.setText(_translate("MainWindow", "0"))
        self.label_channel.setText(_translate("MainWindow", "0"))
        self.button_channel_up.setText(_translate("MainWindow", "Channel Up"))
        self.button_channel_down.setText(_translate("MainWindow", "Channel Down"))
        self.button_power.setText(_translate("MainWindow", "Power"))
        self.button_mute.setText(_translate("MainWindow", "Mute"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
