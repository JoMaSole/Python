import smtplib 

#server = smtplib.SMTP(host='smtp.live.com',port=465)

# import necessary packages 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# create message object instance 
msg = MIMEMultipart()
message = "Thank you"

# setup the parameters of the message 
password = "Marcelo990-"
msg['From'] = "sole.joan.marce@hotmail.com"
msg['To'] = "sircalzones@gmail.com"
msg['Subject'] = "Correo desde Python"

# add in the message body 
msg.attach(MIMEText(message, 'plain'))

#create server 
server = smtplib.SMTP('smtp.live.com:465')
server.starttls()

# Login Credentials for sending the mail 
server.login(msg['From'], password)

# send the message via the server. 
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()

#print "successfully sent email to %s:" % (msg['To'])