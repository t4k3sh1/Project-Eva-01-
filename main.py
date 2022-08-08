from uiw import *
import sys
import serial
#porta sees 
with serial.Serial() as ser:
    ser.baudrate = 19200
    ser.port = '/dev/ttyUSB1'


class Test(Ui_Pannello):
    def __init__(self, window):
        self.setupUi(window)
        self.pushButton_2.clicked.connect(self.Serialstart)
        self.pushButton.clicked.connect(self.Quit)

    def Serialstart(self):
        ser.open()
        print(ser.name)
        hs = ser.readline()
        print(hs)

    def Quit(self):
        sys.exit()

app = QtWidgets.QApplication(sys.argv)
Pannello = QtWidgets.QWidget()

ui = Test(Pannello)

Pannello.show()
app.exec_()


