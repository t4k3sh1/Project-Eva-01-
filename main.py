from uiw2 import *
import serial
import time
import sys
#porta sees 
with serial.Serial() as ser:
    ser.baudrate = 115200

class Test(Ui_Pannello):
    def __init__(self, window):
        self.setupUi(window)
        self.pushButton_2.clicked.connect(self.Serialstart)
        self.pushButton.clicked.connect(self.Quit)
        self.pushButton_6.clicked.connect(self.EmStop)
        self.pushButton_3.clicked.connect(self.wUnimplemented)#self.slowWalk
        self.pushButton_4.clicked.connect(self.wUnimplemented)#self.fastWalk
        self.pushButton_5.clicked.connect(self.wUnimplemented)#self.boringAI
        #self.checkBox.isChecked.connect(self.ForceBT)
    def ForceBT(self):
        if ser.lostParity():
            ser.close()
            serialPort = "j"
            ser.open()
            self.serialStart
        ()

    def Serialstart(self):
        fatalw = "0-0W"
        mWarn = "NFW-1180"
        fhs = "fhs"
        # forced hardware serial, used to force a start in development mode
        testkeys = "c5edb461-f726-4f12-bb6b-490897bfed75"
        print("loaded debug keypair")
        print(testkeys)
        prodkeys = "" #production keys have yet to be rolled out
        serialUID = self.textEdit.toPlainText()
        print(serialUID) #debug code :hahaball:
        ser.port = serialUID
        ser.open()
        print(ser.name)
        ser.write(b"s")
        time.sleep(1)
        buff = ser.readline()
        decbuf = buff.decode()
        resp = decbuf.strip()
        print (resp)
        if resp == fatalw:
            print("Warning: device operating in unsafe/incomplete mode, unable to connect to motor system")
            print("No I4C interface detected, consent plug not detected/key mismatch")
            print("proceding to activation may cause major trouble to the software and to the hardware")
        buff = ""
        buff = ser.readline()
        decbuf = buff.decode()
        resp = decbuf.strip()
        ser.write(b"dd")
        if resp == fhs:
            buff = ""
            buff = ser.readline()
            decbuf = buff.decode()
            resp = decbuf.strip()
            print(resp)
        if resp == testkeys:
            print("Setting hl to it/IT - UTF8")
            print("attivazione riuscita. Il programma sta eseguendo in modalità userdebug con una chiave di test caricata.")

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
        #for i in range 20
            #ser.write(b"\n")
            #ser.read
        #print("continuing walking loop, client reports no warning, check 3dUI for more information")
    #def fastWalk(self):
        #ser.write(b"\n")
        #ser.read
        #print("continuing walking loop, client reports no warning, check 3dUI for more information")
    #def boringAI(self):
        #future mercury will definitely love working on the ai backend :skull:

# draw main window and start event listener
app = QtWidgets.QApplication(sys.argv)
Pannello = QtWidgets.QWidget()
ui = Test(Pannello)
Pannello.show()
app.exec_()
