# -*- coding: utf-8 -*-

import ssl, time, mimetypes, os, smtplib
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(526, 451)
        Dialog.setAccessibleName("")        
        Dialog.setStyleSheet("background-color:rgb(24,24,24)")
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 526, 451))
        self.widget_2.setObjectName("widget_2")
        self.username = QtWidgets.QLineEdit(self.widget_2)
        self.username.setGeometry(QtCore.QRect(10, 104, 181, 31))
        self.username.setStyleSheet("background-color:rgb(34,34,34);color:green")
        self.username.setObjectName("username")
        self.clear = QtWidgets.QPushButton(self.widget_2)
        self.clear.setGeometry(QtCore.QRect(112, 241, 78, 25))
        self.clear.setAccessibleName("")
        self.clear.setStyleSheet("background-color:white")
        self.clear.setObjectName("clear")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(13, 81, 60, 20))
        self.label.setStyleSheet("color:white")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(13, 138, 60, 20))
        self.label_2.setStyleSheet("color:white")
        self.label_2.setObjectName("label_2")
        self.password = QtWidgets.QLineEdit(self.widget_2)
        self.password.setGeometry(QtCore.QRect(10, 161, 181, 31))
        self.password.setStyleSheet("background-color:rgb(34,34,34);color:green")
        self.password.setObjectName("password")
        self.open_file = QtWidgets.QPushButton(self.widget_2)
        self.open_file.setGeometry(QtCore.QRect(59, 286, 80, 22))
        self.open_file.setStyleSheet("background-color:white")
        self.open_file.setObjectName("open_file")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(200, 14, 320, 31))
        self.lineEdit_6.setStyleSheet("background-color:rgb(24,24,24);color:white")
        self.lineEdit_6.setInputMask("")
        self.lineEdit_6.setFrame(False)
        self.lineEdit_6.setDragEnabled(False)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setPlaceholderText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.recipient = QtWidgets.QLineEdit(self.widget_2)
        self.recipient.setGeometry(QtCore.QRect(200, 45, 320, 35))
        self.recipient.setStyleSheet("background-color:rgb(68,68,68);color:white")
        self.recipient.setInputMask("")
        self.recipient.setText("")
        self.recipient.setMaxLength(42)
        self.recipient.setFrame(True)
        self.recipient.setDragEnabled(False)
        self.recipient.setReadOnly(False)
        self.recipient.setObjectName("recipient")
        self.widget = QtWidgets.QWidget(self.widget_2)
        self.widget.setGeometry(QtCore.QRect(201, 115, 319, 301))
        self.widget.setStyleSheet("background-color:rgb(68,68,68);color:white")
        self.widget.setObjectName("widget")
        self.text = QtWidgets.QTextEdit(self.widget)
        self.text.setGeometry(QtCore.QRect(0, 0, 320, 301))
        self.text.setStyleSheet("")
        self.text.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.text.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.text.setMidLineWidth(0)
        self.text.setObjectName("text")
        self.send = QtWidgets.QPushButton(self.widget_2)
        self.send.setGeometry(QtCore.QRect(11, 241, 78, 25))
        self.send.setAccessibleName("")
        self.send.setStyleSheet("background-color:white")
        self.send.setObjectName("send")
        self.subject = QtWidgets.QLineEdit(self.widget_2)
        self.subject.setGeometry(QtCore.QRect(200, 80, 320, 35))
        self.subject.setStyleSheet("background-color:rgb(68,68,68);color:white")
        self.subject.setInputMask("")
        self.subject.setText("")
        self.subject.setMaxLength(200)
        self.subject.setCursorPosition(0)
        self.subject.setDragEnabled(False)
        self.subject.setObjectName("subject")
        

        self.retranslateUi(Dialog)
        self.clear.clicked.connect(self.clear_data)
        self.send.clicked.connect(self.send_email)
        self.open_file.clicked.connect(self.choose_file)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def clear_data(self):    #clear data
        self.subject.clear()
        self.text.clear()

    def choose_file(self):  #Import any file and save its address
        global Path_file      
        fileName = QtWidgets.QFileDialog.getOpenFileName()
        Path_file= fileName[0] 


    global MessageBox
    def MessageBox():
        msg=QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle(' Error')            
        msg.setText('<body><h3> Plase Give My The User name and Password<h3></body>')
        msg.setStyleSheet("background-color:rgb(32,32,32);color:white")        
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ignore)
        reply=msg.exec_()                       

    def send_email(self):       
        try:            
            app.processEvents()
            response = os.system("ping -c 1 smtp.gmail.com")
            if response != 0:
                msg=QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle(' Network Error ')            
                msg.setText('<body><h3> Please Check Your Connection And Try Again <h3></body>')
                msg.setStyleSheet("background-color:rgb(32,32,32);color:white")        
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ignore)
                reply=msg.exec_()            

            def add_attachment(msg, filename):
                app.processEvents()
                if not os.path.isfile(filename):
                    return

                ctype, encoding = mimetypes.guess_type(filename)

                if ctype is None or encoding is not None:
                    ctype = 'application/octet-stream'

                maintype, subtype = ctype.split('/', 1)

                if maintype == 'text':
                    with open(filename) as f:
                        mime = MIMEText(f.read(), _subtype=subtype)
                elif maintype == 'image':
                    with open(filename, 'rb') as f:
                        mime = MIMEImage(f.read(), _subtype=subtype)
                elif maintype == 'audio':
                    with open(filename, 'rb') as f:
                        mime = MIMEAudio(f.read(), _subtype=subtype)
                else:
                    with open(filename, 'rb') as f:
                        mime = MIMEBase(maintype, subtype)
                        mime.set_payload(f.read())

                    encoders.encode_base64(mime)

                mime.add_header('Content-Disposition', 'attachment', filename=filename)
                message.attach(mime)
            
            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email =self.username.text() 
            receiver_email =self.recipient.text()
            password =self.password.text()
            if not self.username.text() or not self.password.text() or not self.recipient.text():                #Checking The Values                
                MessageBox()
                            
            date = time.ctime()
            message = MIMEMultipart()                
            message['Subject'] = self.subject.text()
            message['To'] = self.recipient.text()
            message.attach(MIMEText(f'{date}\n,{self.text.toPlainText()}\n')) #set text for email                
            add_attachment(message,Path_file)     # Check input file type to send                
            try :
                app.processEvents()
                context = ssl.create_default_context()
                server = smtplib.SMTP_SSL(smtp_server, port)
                server.login(sender_email, password)                 
                app.processEvents()
                server.sendmail(sender_email, receiver_email, message.as_string())
                server.quit()
        
                msg=QMessageBox()                       # Message  successfully
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle(' Info ')            
                msg.setText('<body><h3> Message sent successfully.  <h3></body>')
                msg.setStyleSheet("background-color:rgb(32,32,32);color:white")        
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ignore)
                reply=msg.exec_()                       

            except Exception:                
                msg=QMessageBox()                       #Error for username or password
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle(' Error')     
                msg.setText('<body><h3> Invalid Username or Password. <h3></body>')       
                msg.setStyleSheet("background-color:rgb(32,32,32);color:white")        
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ignore)
                reply=msg.exec_()                       
        except Exception:
            msg=QMessageBox()                       #Error for not importing the file
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle(' Error')            
            msg.setText('<body><h3> Please Import a File <h3></body>')
            msg.setStyleSheet("background-color:rgb(32,32,32);color:white")        
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ignore)
            reply=msg.exec_()                       

    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Linux-Email-Automation"))
        self.username.setAccessibleName(_translate("Dialog", "username"))
        self.clear.setText(_translate("Dialog", "clear"))
        self.label.setText(_translate("Dialog", "Username "))
        self.label_2.setText(_translate("Dialog", "Password "))
        self.password.setAccessibleName(_translate("Dialog", "password"))
        self.open_file.setAccessibleName(_translate("Dialog", "open_file"))
        self.open_file.setText(_translate("Dialog", "Open..."))
        self.lineEdit_6.setText(_translate("Dialog", "New Message"))
        self.recipient.setAccessibleName(_translate("Dialog", "recipient"))
        self.recipient.setPlaceholderText(_translate("Dialog", "Recipient: "))
        self.text.setAccessibleName(_translate("Dialog", "text"))
        self.text.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text.setPlaceholderText(_translate("Dialog", "Text: "))
        self.send.setText(_translate("Dialog", "send"))
        self.subject.setAccessibleName(_translate("Dialog", "subject"))
        self.subject.setPlaceholderText(_translate("Dialog", "Subject: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
