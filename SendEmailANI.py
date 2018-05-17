import requests
import json
import smtplib
from sqlwrapper import gensql,dbget
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def sendemailani(name,email,message,conf_no,arrival,depature,room_type,id1,book_date):
     print(name,email,message,conf_no,arrival,depature, room_type)
     sender = "infocuit.testing@gmail.com"
     receiver = email
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
     <html>
     <head></head>
     <body>
       <dl>
       <dt>
       <p><font size="4" color="black">"""+hotel_det[0]['hotel_name']+""",</font></p>
        <p><font size="4" color="black">"""+hotel_det[0]['address']+""",</font></p>
        <p><font size="4" color="black">"""+hotel_det[0]['mobile_no']+""",</font></p>
        <p><font size="4" color="black">"""+hotel_det[0]['email']+""",</font></p>
       <p><font size="4" color="black">"""+book_date+""".</font></p>

        
        <p><font size="4" color="black">Dear """+name+""",</font></p>
        <p><font size="4" color="black">We are delighted that you have selected our """+hotel_det[0]['hotel_name']+"""</font></p>
       <p><font size="4" color="black">On behalf of the entire team at the Hotel Name, I extend you a very welcome and trust stay with us will be both enjoyable and comfortable</font></p>
       <p><font size="4" color="black">Hotel Name offers a selection of business services and facilities which are detailed in the booklet, placed on the writing table in your room.</font></p>
       <p><font size="4" color="black">Should you require any assistance or have any specific requirements,please do not hesitate to contact me on extension(999)</font></p>
        
       <p><font size="4" color="blue">Confirmation Number:"""+conf_no+"""</font></p>
       <p><font size="4" color="blue">Arrival Date:"""+arrival+"""</font></p>
       <p><font size="4" color="blue">Depature Date0: """+depature+"""</font></p>
       <p><font size="4" color="blue">Room Type: """+room_type+"""</font></p>

       <p><font size="4" color="black">With best regards / Yours sincerely,</font></p>
        <p><font size="4" color="black">Hotel Manager</font></p>
       
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
     email = "infocuit.raja@gmail.com"
     message = "Booking Confirmed"
     conf_no = re['customer_confirmation_number']
     #hotel_name = "SMARTMO"
     arrival = re['customer_arrival_date']
     depature = re['customer_depature_date']
     room_type = re['customer_room_type']
     id1 = re['id']
     book_date = re['customer_booked_date']
     return sendemailani(name,email,message,conf_no,arrival,depature,room_type,id1,book_date)
