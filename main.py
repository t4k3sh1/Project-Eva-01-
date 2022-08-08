from uiw import *
import sys
import serial
#porta sees 
with serial.Serial() as ser:
    ser.baudrate = 19200
    


class Test(Ui_Pannello):
    def __init__(self, window):
        self.setupUi(window)
        self.pushButton_2.clicked.connect(self.Serialstart)
        self.pushButton.clicked.connect(self.Quit)
        self.pushButton_6.clicked.connect(self.EmStop)
        self.pushButton_3.clicked.connect(self.wUnimplemented)#self.slowWalk
        self.pushButton_4.clicked.connect(self.wUnimplemented)#self.fastWalk
        self.pushButton_5.clicked.connect(self.wUnimplemented)#self.boringAI

    def Serialstart(self):
        serialUID = self.textEdit.toPlainText()
        print(serialUID) #debug code :hahaball:
        ser.port = serialUID
        ser.open()
        print(ser.name)
        hs = ser.readline()
        print(hs)

    def Quit(self):
        sys.exit()
    
    def EmStop(self):
        #ser.write(b'EMS\n')
        print("Emergency stop called! Disabling motors and resetting to original pos")
        #ser.write(b"0xn -a -r -nrh\n") # pos 0 on all motors, removes power (-a), restores relative positioning (-r), doesn't home after resetting (-nrh)
        print("0xn called, you'll need to restore active connection using the connect button. it is highly advised to also flush connection stats before attempting sync")
        #disables serial port
        #ser.close()
        #need reconnection to restore stream
    def wUnimplemented(self):
        print("Uh Oh! it looks like the feature you're trying to use is still being worked on by our team, please wait patiently and check for repository updates often!")


    #def slowWalk(self):
        #ser.write(b"\n")
        #ser.read
        #print("continuing walking loop, client reports no warning, check 3dUI for more information")
    #def fastWalk(self):
        #ser.write(b"\n")
        #ser.read
        #print("continuing walking loop, client reports no warning, check 3dUI for more information")
    #def boringAI(self):
        #future mercury will definitely love working on the ai backend :skull:

app = QtWidgets.QApplication(sys.argv)
Pannello = QtWidgets.QWidget()

ui = Test(Pannello)

Pannello.show()
app.exec_()


