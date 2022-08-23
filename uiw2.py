# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, QtWebKitWidgets


class Ui_Pannello(object):
    def setupUi(self, Pannello):
        Pannello.setObjectName("Pannello")
        Pannello.resize(1093, 660)
        Pannello.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(Pannello)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(930, 570, 161, 51))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(10, 140, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 80, 171, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(820, 20, 121, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(960, 20, 121, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 310, 371, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.webView = QtWebKitWidgets.QWebView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(420, 90, 661, 461))
        self.webView.setUrl(QtCore.QUrl("https://www.google.it/maps/@41.9087812,12.5642266,15z?hl=it&ucbcb=1"))
        self.webView.setObjectName("webView")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 190, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 230, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 270, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 301, 61))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(550, 570, 371, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.statusbar = QtWidgets.QStatusBar(Pannello)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(Pannello)
        QtCore.QMetaObject.connectSlotsByName(Pannello)

    def retranslateUi(self, Pannello):
        _translate = QtCore.QCoreApplication.translate
        Pannello.setWindowTitle(_translate("Pannello", "Pannello di controllo [userdebug beta 0.1.3 - rc1]"))
        self.pushButton.setText(_translate("Pannello", "Quit"))
        self.label.setText(_translate("Pannello", "Unità collegata e attiva"))
        self.pushButton_2.setText(_translate("Pannello", "Connect"))
        self.pushButton_3.setText(_translate("Pannello", "Slow Walk"))
        self.pushButton_4.setText(_translate("Pannello", "Run"))
        self.pushButton_5.setText(_translate("Pannello", "Navigate using AI"))
        self.checkBox.setText(_translate("Pannello", "Aggressive switching to bluetooth on lost packet"))
        self.checkBox_2.setText(_translate("Pannello", "Force log level to VeryVerbose (might load more data)"))
        self.checkBox_3.setText(_translate("Pannello", "Bluetooth?!?!"))
        self.pushButton_6.setText(_translate("Pannello", "Emergency Stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pannello = QtWidgets.QMainWindow()
    ui = Ui_Pannello()
    ui.setupUi(Pannello)
    Pannello.show()
    sys.exit(app.exec_())
