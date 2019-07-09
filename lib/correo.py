 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 

def envioCorreo( _from, _pass, _to, _subject, _message ):

    # create message object instance
    msg = MIMEMultipart()

    # setup the parameters of the message
    #password = "CarolinaAndrea5"
    password = _pass
    #msg['From'] = "informa.bot@gmail.com"
    msg['From'] =  _from
    #msg['To'] = "informa.bot@gmail.com"
    msg['To'] =  _to
    #msg['Subject'] = "Mensaje de prueba - formato sencillo"
    msg['Subject'] = _subject
    
    message = _message
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    
    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    
    
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    print ("successfully sent email to %s:" % (msg['To']))
    pass