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
 data = message.split("|")
 print(data)
 subject = request.json['subject']
 msg = MIMEMultipart()
 msg['from'] = sender
 msg['to'] = receiver
 msg['subject'] = subject
 # Create the body of the message (a plain-text and an HTML version)
 html = """\
 <html>
  <head></head>
  <body>
    <dl>
    <dt>
    <p><font size="2" color="black">"""+str(data[0])+"""</font></p>
    <p><font size="4" color="blue">"""+str(data[1])+"""</font></p>
    <dd>
    <p><font size="2" color="black">"""+str(data[2])+"""</font></p>
    <p><font size="2" color="black">"""+str(data[3])+"""</font></p>
    <p><font size="2" color="black">"""+str(data[4])+"""</font></p>
    <p><font size="2" color="black">"""+str(data[5])+"""</font></p>
    <p><i><font size="2" color="blue">"""+str(data[6])+"""</font></i></p>
    <p><font size="4" color="blue">"""+str(data[7])+"""</font></p>
    </dd>
    </dl>

  </body>
 </html>
 """
 
 msg.attach(MIMEText(msg['subject'],'plain'))
 msg.attach(MIMEText(html,'html'))
 
 gmailuser = 'infocuit.aravindh@gmail.com'
 password = '0487nand'
 server = smtplib.SMTP('smtp.gmail.com',587)
 server.starttls()
 server.login(gmailuser,password)
 text = msg.as_string()
 server.sendmail(sender,receiver,text)
 print ("the message has been sent successfully")
 server.quit()
 return(json.dumps({'Message': 'Message Send Successfully'}, sort_keys=True, indent=4))
#if __name__ == "__main__":
 #   app.run(debug=True)
 # app.run(host="192.168.1.5",port="5000")
