import json
import psycopg2
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask,request,jsonify
app = Flask(__name__)
#@app.route('/sendemailall',methods=['POST'])
def sendemailall():
 try:
      con = psycopg2.connect(user='quywvejawxhnse',password='065fe8ac62d76caa061d1e517b2f0107b5776f767037c2e29cad16c259a771cf',host='ec2-176-34-113-15.eu-west-1.compute.amazonaws.com',port='5432',database='d3opaj0jiqsm0h')
      cur = con.cursor()
 except psycopg2.Error :
      return (json.dumps({'Status': 'Failure','Message':'DB connection Error'}, sort_keys=True, indent=4))

 customer_appointment_date_from = request.json['appointment_date_from'] 
 customer_appointment_date_to = request.json['appointment_date_to']     
 sender = request.json['sender']
 business_id = request.json['business_id']
 if len(customer_appointment_date_from) is 0:
      Today_date = datetime.datetime.utcnow().date().strftime('%Y-%m-%d')
      customer_appointment_date_from = Today_date 
      customer_appointment_date_to = Today_date 

 
 mail = []
 sql = ("select customer_email from customer_details where business_id = "+business_id+"and customer_appointment_date between '"+customer_appointment_date_from+"' and '"+customer_appointment_date_to+"'")
 cur.execute(sql)
 result = cur.fetchall()
 for field in result:
     for test in field:
         if test  not in mail:
            mail.append(test)
 #print(mail)
 
 len_mail = len(mail)    
 #receiver = request.json['receiver']
 message = request.json['message']
 data = message.split("|")
 #print(data)
 subject = request.json['subject']
 msg = MIMEMultipart()
 msg['from'] = sender
 x=0
 #for receiver in email:
 while len_mail != x:
 #for  email in mail[x]:
     print(mail[x])
     msg['to'] = mail[x]
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
     
     #msg.attach(MIMEText(msg['subject'],'plain'))
     msg.attach(MIMEText(html,'html'))
     
     gmailuser = 'infocuit.aravindh@gmail.com'
     password = '0487nand'
     server = smtplib.SMTP('smtp.gmail.com',587)
     server.starttls()
     server.login(gmailuser,password)
     text = msg.as_string()
     server.sendmail(sender,mail[x],text)
     x+=1
     server.quit()
 print ("the message has been sent successfully")    
 return(json.dumps({'Message': 'Message Send Successfully'}, sort_keys=True, indent=4))
#if __name__ == "__main__":
 #   app.run(debug=True)
  #app.run(host="192.168.1.6",port=5000)
