import urllib.request
import json
import datetime
import schedule
import time
import psycopg2
from flask import Flask,request,jsonify
app = Flask(__name__)
#@app.route('/schedulesms',methods=['GET'])
def schedulesms():
       
 try:
    con = psycopg2.connect(user='quywvejawxhnse',password='065fe8ac62d76caa061d1e517b2f0107b5776f767037c2e29cad16c259a771cf',host='ec2-176-34-113-15.eu-west-1.compute.amazonaws.com',port='5432',database='d3opaj0jiqsm0h')
    cur = con.cursor()
 except psycopg2.Error :
    return (json.dumps({'Status': 'Failure','Message':'DB connection Error'}, sort_keys=True, indent=4))
 today = datetime.date.today()
 tomrrow_date = today + datetime.timedelta(days=1)
 tomrrow_date = tomrrow_date.strftime('%Y-%m-%d')
 mobilenumer = []
 smssend = []
 #if request.args.get('business_id') and request.args.get('tomrrow_date'):
     #business_id  =  request.args['business_id']
     #customer_appointment_date = request.args['tomrrow_date']
 sql = ("select customer_mobile from customer_details where customer_appointment_date = '"+tomrrow_date+"'")
 cur.execute(sql)
 result = cur.fetchall()
 for field in result:
    for mobile in field:
        if mobile in smssend:
            pass
        else:
         mobilenumer.append(mobile)
 print(smssend)
 print(mobilenumer)
 #return(json.dumps({'mobile_tomrrow_date':mobilenumer},sort_keys=True, indent = 3))
 
 for mobile in mobilenumer:
               #print(mobile)
        if mobile in smssend:
            pass
        else:       
               smssend.append(mobile)
               print(smssend)               
               message = "appointment confirmed"
               url = "https://control.msg91.com/api/sendhttp.php?authkey=195833ANU0xiap5a708d1f&mobiles="+mobile+"&message="+message+"&sender=Doctor&route=4&country=91"
               req = urllib.request.Request(url)
               with urllib.request.urlopen(req) as response:
                  the_page = response.read()
                  the_page = the_page[1:]
                  print(the_page)
                  the_page = str(the_page)
                
 return(json.dumps({"Message":"SMS Sent Sucessfully"},indent =2)) 
schedule.every().day.at("13:35").do(schedulesms)
while 1:
    schedule.run_pending()
    time.sleep(1)
   
       
#if __name__ == "__main__":
    #app.run(debug=True)
   #app.run(host="192.168.1.5",port=5000)
