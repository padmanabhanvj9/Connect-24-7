import requests
import json
import smtplib
from sqlwrapper import gensql,dbget
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def sendemailani(name,email,message,conf_no,arrival,depature,room_type,id1,book_date):
     print(name,email,type(email),message,conf_no,arrival,depature, room_type)
     sender = "infocuit.testing@gmail.com"
     for i in email:
          receiver = i
          #print(sender,type(sender),receiver,type(receiver))
          subject = "Hotel Booking"
          msg = MIMEMultipart()
          msg['from'] = sender
          msg['to'] = receiver
          msg['subject'] = subject
          ids = id1
          print(ids)
          hotel_det = json.loads(dbget("select * from ivr_hotel_list where id = "+str(ids)+""))
          print(hotel_det)
          html = """\
          <!DOCTYPE html>
          <html>
          <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
          <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
          <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
          </head>
          <body>
          <dl>
          <dt>
          <pre>
          <font size="4" color="black">"""+hotel_det[0]['hotel_name']+""",</font>
          <font size="4" color="black">"""+hotel_det[0]['address']+""",</font>
          <font size="4" color="black">"""+hotel_det[0]['mobile_no']+""",</font>
          <font size="4" color="black">"""+hotel_det[0]['email']+""",</font>
          <font size="4" color="black">"""+book_date+""".</font>
          
          <font size="4" color="black">Dear """+name+""",</font></p>
          <font size="4" color="black">        We are delighted that you have selected our """+hotel_det[0]['hotel_name']+""" On behalf of the entire team at the 
          """+hotel_det[0]['hotel_name']+""",extend you a very welcome and trust stay with us will be both enjoyable and comfortable
          """+hotel_det[0]['hotel_name']+""" offers a selection of business services and facilities.which are detailed in the booklet,
          placed on the writing table in your room.Should you require any assistance or have any specific
          requirements,please do not hesitate to contact me oextension(999).</font>
           </pre>
     <pre>
          <font size="4" color="blue">Confirmation Number: """+conf_no+"""</font>
          <font size="4" color="blue">Arrival Date: """+arrival+"""</font>
          <font size="4" color="blue">Depature Date0: """+depature+"""</font>
          <font size="4" color="blue">Room Type: """+room_type+"""</font>

          <font size="4" color="black">With best regards / Yours sincerely,</font>
          <font size="4" color="black">Hotel Manager</font></pre>
            
          </dl>        
          </body>
          </html>
          """

          msg.attach(MIMEText(html,'html'))
          
          gmailuser = 'infocuit.testing@gmail.com'
          password = 'infocuit@123'
          server = smtplib.SMTP('smtp.gmail.com',587)
          server.starttls()
          server.login(gmailuser,password)
          text = msg.as_string()
          server.sendmail(sender,receiver,text)
          print ("the message has been sent successfully")
          server.quit()
     return(json.dumps({'Return': 'Message Send Successfully',"Return_Code":"MSS","Status": "Success","Status_Code": "200"}, sort_keys=True, indent=4))



def callexternalapi(request):
     phone = request.json['mobile']
     d = {}
     d['customer_mobile'] = phone
     result = json.loads(gensql('select','ivr_room_customer_booked','*',d))
     re = result[0]
     print(re,type(re))     
     name = re['customer_name']
     email = ['infocuit.raja@gmail.com','infocuit.daisy@gmail.com','i.sidhanee@iss-consultancy.co.uk','jazizahmed@gmail.com','infocuit.banupriya@gmail.com','r.ahamed@iss-consultancy.co.uk','infocuit.padmanabhan@gmail.com']
     message = "Booking Confirmed"
     conf_no = re['customer_confirmation_number']
     #hotel_name = "SMARTMO"
     arrival = re['customer_arrival_date']
     depature = re['customer_depature_date']
     room_type = re['customer_room_type']
     id1 = re['id']
     book_date = re['customer_booked_date']
     return sendemailani(name,email,message,conf_no,arrival,depature,room_type,id1,book_date)
