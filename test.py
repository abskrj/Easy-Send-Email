import ssl, time
import mimetypes
import os
import smtplib

from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Interface_CMD_Terminal():

    def __init__(self):
        #create variables need
        self.sender_email =None
        self.sender_pass = None
        self.port = 0
        self.smtp = None
        self.receiver_email = None
        self.subject = None
        self.text_message = None
        self.path_image = None

    def Setting(self,rewriting_setting = False): # taking data for send a email |Email - password - port - smtp server 
        try:
            file = open('./.setting.txt','r')  #open file settings data 
            data = file.read() #read file and save into data
            print(file.read())
            file.close()#Close the file
        except:
            data = '' #create a varibale for 'if'
        
        if rewriting_setting == True:
            os.remove('./.setting.txt') # removing file setting 
            data = open('./.setting.txt','a')
            data.write(input('* Enter Your Email : ')+'^|^\n') # Write Email + ^|^\n for spilt file 
            data.write(input('* Enter Your Password Email : ')+'^|^\n') # Write password + ^|^\n for spilt file 
            data.write(input('Enter a Port [Defult Port : 465 [press Enter to skip]] : ')+'^|^\n') # Write port + ^|^\n for spilt file 
            data.write(input('Enter Smtp server [Defulat Smtp : smtp.gmail.com [press Enter to skip]] : ')+'^|^\n') # Write Smtp + ^|^\n for spilt file 
            data.close()

        elif len(data) >=10 :#checking the file for data
            data_setting =data.split('^|^\n')

            self.sender_email = data_setting[0] # Email Sender Index
            # print(self.sender_email) #check value

            self.sender_pass = data_setting[1]  # Password Email Sender Index
            # print(self.sender_pass) #check value

            self.port = int(data_setting[3]) if len(data_setting[3]) >=1 else 465 #Check Port Index
            # print(self.port) #check value

            self.smtp = data_setting[4] if len(data_setting[4]) >=10 else 'smtp.gmail.com' # check for smtp server 
            # print(self.smtp) #check value
            
        else:
            data = open('./.setting.txt','a')
            data.write(input('* Enter Your Email : ')+'^|^\n') # Write Email + ^|^\n for spilt file 
            data.write(input('* Enter Your Password Email : ')+'^|^\n') # Write password + ^|^\n for spilt file 
            data.write(input('Enter a Port [Defult Port : 465 [press Enter to skip]] : ')+'^|^\n') # Write port + ^|^\n for spilt file 
            data.write(input('Enter Smtp server [Defulat Smtp : smtp.gmail.com [press Enter to skip] ] : ')+'^|^\n') # Write smtp + ^|^\n for spilt file 
            data.close()

    def Infromation_email(self) :#taking information for send email
        self.receiver_email = input('\n* Enter Receiver Email : ') #Enter  Receiver Email
        self.subject = input('* Subject : ') #Enter Subject Email
        self.text_message = input('* Text Message :') #Enter Text Message
        self.path_image = input('Enter path a image : ') #Enter Path image 
    
    def Add_attachment(self,msg, filename):
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
        msg.attach(mime)

    def Send_Email(self):
        '''
        This file takes the SMTP Sender Email address, Receiver Email address as inputs and 
        sends a mail with a specific message using Gmail as the SMTP server.

        This file is useful to send mails from the commandline or programmatically without opening a browser

        '''
        port = self.port
        smtp_server = self.smtp
        sender_email = self.sender_email
        receiver_email = self.receiver_email
        password = self.sender_pass
        date = time.ctime()
        message = MIMEMultipart()
        text = MIMEText(f"Subject: {self.subject}\nCurrent Time/Date: {date}\n{self.text_message}")
        message.attach(text) #attaches text to the email
        img_data = open(self.path_image, 'rb').read() #Enter image filename
        image = MIMEImage(img_data, name=os.path.basename(self.path_image)) #Enter image filename
        message.attach(image) #attaches image to the email

        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL(smtp_server, port)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, str(message))
        server.quit()

def Main():
    main = Interface_CMD_Terminal()
    print('Welcome to Script')
    print('-'*20)
    print('''1 - Send Email
2 - Setting ''')
    operator = input('Select a operator : ')
    if operator == '1':
        main.Setting()
        main.Infromation_email()
        main.Send_Email()

    elif operator == '2' :
        main.Setting(True)
    else:
        print('Erorr : invalid input')
        
Main()
