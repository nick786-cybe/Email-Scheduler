from PyQt5 import QtCore, QtGui, QtWidgets
import time
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()  
port = 1255
s.connect((host,port))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 480)
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 801, 601))
        self.frame.setStyleSheet("background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 100, 255), stop:1 rgba(0, 180, 171, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 561, 491))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setMouseTracking(True)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setStyleSheet("background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 92, 120, 255), stop:1 rgba(11, 90, 127, 200))")
        self.tab1.setObjectName("tab1")
        self.lineEdit = QtWidgets.QLineEdit(self.tab1)
        self.lineEdit.setGeometry(QtCore.QRect(170, 110, 261, 31))
        self.lineEdit.setStyleSheet(".QLineEdit{background:rgb(0, 0, 125);\n"
"border:none;\n"
"color:rgb(255, 255, 255);\n"
"font-size:15px;}\n"
"\n"
".QLineEdit:hover{\n"
"border:1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 255, 196), stop:0.994318 rgba(0, 255, 0, 200));}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab1)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 180, 261, 31))
        self.lineEdit_2.setStyleSheet(".QLineEdit{background:rgb(0, 0, 125);\n"
"border:none;\n"
"color:rgb(255, 255, 255);\n"
"font-size:15px;}\n"
"\n"
".QLineEdit:hover{\n"
"border:1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 255, 196), stop:0.994318 rgba(0, 255, 0, 200));}")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.tab1)
        self.label.setGeometry(QtCore.QRect(170, 90, 131, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;\n"
"border:none;\n"
"border-radius:2px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab1)
        self.label_2.setGeometry(QtCore.QRect(170, 160, 161, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;\n"
"border:none;\n"
"border-radius:2px;")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.tab1)
        self.pushButton.setGeometry(QtCore.QRect(240, 280, 75, 31))
        self.pushButton.setStyleSheet(".QPushButton{border:1px solid;\n"
"border-radius:4px;\n"
"color:white;\n"
"font-size:15px rgb(0, 255, 127);\n"
"background:rgb(255, 85, 127);\n"
"}\n"
"\n"
".QPushButton:focus{\n"
"background:rgb(0, 255, 127);}\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.login)
        self.textBrowser1 = QtWidgets.QTextBrowser(self.tab1)
        self.textBrowser1.setGeometry(QtCore.QRect(10, 420, 551, 31))
        self.textBrowser1.setStyleSheet("border:none;\n"
"color:white;\n"
"font-size:12px;")
        self.textBrowser1.setObjectName("textBrowser")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab1, icon, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.375 rgba(0, 92, 120, 255), stop:1 rgba(0, 83, 118, 255))")
        self.tab_2.setObjectName("tab_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 70, 261, 31))
        self.lineEdit_3.setStyleSheet(".QLineEdit{background:rgb(0, 0, 125);\n"
"border:none;\n"
"color:rgb(255, 255, 255);\n"
"font-size:15px;}\n"
"\n"
".QLineEdit:hover{\n"
"border:1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 255, 196), stop:0.994318 rgba(0, 255, 0, 200));}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(0, 50, 161, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white;\n"
"border:none;\n"
"border-radius:2px;")
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 140, 531, 71))
        self.textEdit.setStyleSheet("color:rgb(255, 255, 255);\n"
"background:rgb(0, 0, 127)")
        self.textEdit.setPlaceholderText("Enter Title")
        self.textEdit.setObjectName("textEdit")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 220, 531, 171))
        self.plainTextEdit.setStyleSheet("color:rgb(255, 255, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 90, 75, 31))
        self.pushButton_2.setStyleSheet(".QPushButton{border:1px solid;\n"
"border-radius:4px;\n"
"color:white;\n"
"font-size:15px rgb(0, 255, 127);\n"
"background:rgb(255, 85, 127);\n"
"}\n"
"\n"
".QPushButton:focus{\n"
"background:rgb(0, 255, 127);}\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.schedule)

        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 90, 75, 31))
        self.pushButton_3.setStyleSheet(".QPushButton{border:1px solid;\n"
"border-radius:4px;\n"
"color:white;\n"
"font-size:15px rgb(0, 255, 127);\n"
"background:rgb(255, 85, 127);\n"
"}\n"
"\n"
".QPushButton:focus{\n"
"background:rgb(0, 255, 127);}\n"
"\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.send_message)
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 420, 551, 31))
        self.textBrowser.setStyleSheet("border:none;\n"
"color:white;\n"
"font-size:12px;")
        self.textBrowser.setObjectName("textBrowser")
        self.timeEdit = QtWidgets.QTimeEdit(self.tab_2)
        self.timeEdit.setGeometry(QtCore.QRect(390, 50, 121, 22))
        self.timeEdit.setStyleSheet("background:rgb(255, 255, 255);\n"
"font-size:19px;")
        self.timeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.timeEdit.setCalendarPopup(True)
        self.timeEdit.setObjectName("timeEdit")
        self.dateEdit = QtWidgets.QDateEdit(self.tab_2)
        self.dateEdit.setGeometry(QtCore.QRect(390, 20, 121, 22))
        self.dateEdit.setStyleSheet("background:rgb(255, 255, 255);\n"
"font-size:19px;")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        icon = QtGui.QIcon.fromTheme("gmail")
        self.tabWidget.addTab(self.tab_2, icon, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def login(self):
        s.send("login".encode("utf-8"))
        time.sleep(1)
        var =self.lineEdit.text()
        s.send(var.encode("utf-8"))
        var2 =self.lineEdit_2.text()
        s.send(var2.encode("utf-8"))
        returns = (s.recv(1024).decode("utf-8"))
        self.textBrowser1.setText(str(returns))
            
    def send_message(self):
        s.send("send message".encode("utf-8"))
        client_email = self.lineEdit_3.text()
        s.send(client_email.encode("utf-8"))
        time.sleep(1)
        title = self.textEdit.toPlainText()
        s.send(title.encode("utf-8"))
        message = self.plainTextEdit.toPlainText()
        s.send(message.encode("utf-8"))
        returns = (s.recv(1024).decode("utf-8"))
        self.textBrowser.setText(str(returns))

    def schedule(self):
        s.send("schedule".encode('utf-8'))
        client_email = self.lineEdit_3.text()
        s.send(client_email.encode("utf-8"))
        time.sleep(1)
        title = self.textEdit.toPlainText()
        s.send(title.encode("utf-8"))

        message = self.plainTextEdit.toPlainText()
        s.send(message.encode("utf-8"))
        time.sleep(1)
        date = self.dateEdit.text()
        s.send(date.encode("utf-8"))
        time.sleep(1)
        times = self.timeEdit.text()
        s.send(times.encode("utf-8"))
        print(times)
        #returns = (s.recv(1024).decode("utf-8"))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "   Enter your Email:"))
        self.label_2.setText(_translate("MainWindow", "   Enter your Password:"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Login"))
        self.label_3.setText(_translate("MainWindow", "   Enter client\'s  Email:"))
        self.plainTextEdit.setPlaceholderText(_translate("MainWindow", "Enter Your message"))
        self.pushButton_2.setText(_translate("MainWindow", "Shadule"))
        self.pushButton_3.setText(_translate("MainWindow", "Send now"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.timeEdit.setDisplayFormat(_translate("MainWindow", "hh:mm AP"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "MM/dd/yyyy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Mail"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
