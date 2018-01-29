import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask,request,jsonify
app = Flask(__name__)
#@app.route('/sendemail',methods=['POST'])
def sendemail(request):
 sender = request.json['sender']
 receiver = request.json['receiver']
 message = request.json['message']
 subject = request.json['subject']
 msg = MIMEMultipart()
 msg['from'] = sender
 msg['to'] = receiver
 msg['subject'] = subject
 msg.attach(MIMEText(message,'plain'))
 gmailuser = 'infocuit.aravindh@gmail.com'
 password = '0487nand'
 server = smtplib.SMTP('smtp.gmail.com',587)
 server.starttls()
 server.login(gmailuser,password)
 text = msg.as_string()
 server.sendmail(sender,receiver,text)
 print ("the message has been sent successfully")
 server.quit()
 return json.dumps('message:'Message Send Successfully))
#if __name__ == "__main__":
 #   app.run(debug=True)
 # app.run(host="192.168.1.5",port="5000")
