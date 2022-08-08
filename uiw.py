# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebKitWidgets


class Ui_Pannello(object):
    def setupUi(self, Pannello):
        Pannello.setObjectName("Pannello")
        Pannello.resize(797, 490)
        self.pushButton = QtWidgets.QPushButton(Pannello)
        self.pushButton.setGeometry(QtCore.QRect(700, 450, 94, 36))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Pannello)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 120, 94, 36))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Pannello)
        self.label.setGeometry(QtCore.QRect(20, 40, 181, 20))
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(Pannello)
        self.checkBox.setGeometry(QtCore.QRect(10, 170, 351, 24))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Pannello)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 200, 241, 24))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Pannello)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 230, 241, 24))
        self.checkBox_3.setObjectName("checkBox_3")
        self.pushButton_3 = QtWidgets.QPushButton(Pannello)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 10, 94, 36))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Pannello)
        self.pushButton_4.setGeometry(QtCore.QRect(690, 10, 94, 36))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Pannello)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 280, 201, 36))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Pannello)
        self.pushButton_6.setGeometry(QtCore.QRect(560, 450, 131, 36))
        self.pushButton_6.setObjectName("pushButton_6")
        self.webView = QtWebKitWidgets.QWebView(Pannello)
        self.webView.setGeometry(QtCore.QRect(360, 60, 431, 361))
        self.webView.setUrl(QtCore.QUrl("https://maps.google.it/maps?hl=it"))
        self.webView.setObjectName("webView")
        self.textEdit = QtWidgets.QTextEdit(Pannello)
        self.textEdit.setGeometry(QtCore.QRect(10, 70, 291, 41))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Pannello)
        QtCore.QMetaObject.connectSlotsByName(Pannello)

    def retranslateUi(self, Pannello):
        _translate = QtCore.QCoreApplication.translate
        Pannello.setWindowTitle(_translate("Pannello", "Pannello di controllo [userdebug beta 0.0.8]"))
        self.pushButton.setText(_translate("Pannello", "Quit"))
        self.pushButton_2.setText(_translate("Pannello", "Connect"))
        self.label.setText(_translate("Pannello", "Indirizzo IP o Porta Seriale"))
        self.checkBox.setText(_translate("Pannello", "aggressive switching to bluetooth on lost packets"))
        self.checkBox_2.setText(_translate("Pannello", "Force log level to very verbose"))
        self.checkBox_3.setText(_translate("Pannello", "Bluetooth?!?!"))
        self.pushButton_3.setText(_translate("Pannello", "Slow Walk"))
        self.pushButton_4.setText(_translate("Pannello", "Run"))
        self.pushButton_5.setText(_translate("Pannello", "Navigate using AI"))
        self.pushButton_6.setText(_translate("Pannello", "Emergency Stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pannello = QtWidgets.QWidget()
    ui = Ui_Pannello()
    ui.setupUi(Pannello)
    Pannello.show()
    sys.exit(app.exec_())
