# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Pannello(object):
    def setupUi(self, Pannello):
        Pannello.setObjectName("Pannello")
        Pannello.resize(572, 330)
        self.pushButton = QtWidgets.QPushButton(Pannello)
        self.pushButton.setGeometry(QtCore.QRect(470, 290, 94, 36))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Pannello)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 120, 94, 36))
        self.pushButton_2.setObjectName("pushButton_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Pannello)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 76, 301, 41))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(Pannello)
        self.label.setGeometry(QtCore.QRect(20, 40, 181, 20))
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(Pannello)
        self.checkBox.setGeometry(QtCore.QRect(10, 170, 391, 24))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Pannello)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 200, 241, 24))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Pannello)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 230, 241, 24))
        self.checkBox_3.setObjectName("checkBox_3")

        self.retranslateUi(Pannello)
        QtCore.QMetaObject.connectSlotsByName(Pannello)

    def retranslateUi(self, Pannello):
        _translate = QtCore.QCoreApplication.translate
        Pannello.setWindowTitle(_translate("Pannello", "Pannello di controllo [userdebug beta 0.0.5]"))
        self.pushButton.setText(_translate("Pannello", "Quit"))
        self.pushButton_2.setText(_translate("Pannello", "Connect"))
        self.label.setText(_translate("Pannello", "Indirizzo IP o Porta Seriale"))
        self.checkBox.setText(_translate("Pannello", "[wifi] aggressive switching to bluetooth on lost packets"))
        self.checkBox_2.setText(_translate("Pannello", "Force log level to very verbose"))
        self.checkBox_3.setText(_translate("Pannello", "Bluetooth?!?!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pannello = QtWidgets.QWidget()
    ui = Ui_Pannello()
    ui.setupUi(Pannello)
    Pannello.show()
    sys.exit(app.exec_())
