import urllib.request
import json
import psycopg2
from flask import Flask,request,jsonify
app = Flask(__name__)
@app.route('/SendSms',methods=['GET'])
def sendsms(request):
       if request.args.get('business_id') and request.args.get('message') and request.args.get('date_from') and request.args.get('date_to'):
           message = request.args['message']
           date_from = request.args['date_from']
           date_to = request.args['date_to']
           business_id = request.args['business_id']
           count = []
           try:
             con = psycopg2.connect(user='quywvejawxhnse',password='065fe8ac62d76caa061d1e517b2f0107b5776f767037c2e29cad16c259a771cf',host='ec2-176-34-113-15.eu-west-1.compute.amazonaws.com',port='5432',database='d3opaj0jiqsm0h')
             cur = con.cursor()
           except psycopg2.Error :
             return (json.dumps({'Status': 'Failure','Message':'DB connection Error'}, sort_keys=True, indent=4))
           
           sql = "select customer_mobile from customer_details where business_id="+business_id+" and customer_appointment_date between  '"+date_from+"' and '"+date_to+"' and customer_current_status in ('checkedout')"
           print(sql)
           cur.execute(sql)
           results = cur.fetchall()
           for result in results:
               for i in result:
                  count.append(i)
           print(count)
           for mobile in count:
               print(mobile)
               url = "https://control.msg91.com/api/sendhttp.php?authkey=195833ANU0xiap5a708d1f&mobiles="+mobile+"&message="+message+"&sender=Info&route=4&country=91"
               req = urllib.request.Request(url)
               with urllib.request.urlopen(req) as response:
                  the_page = response.read()
                  the_page = the_page[1:]
                  print(the_page)
                  the_page = str(the_page)                 
           return(json.dumps({"Message":"SMS Sent Sucessfully"},indent =2))
       elif request.args.get('mobile') and request.args.get('message'):
          mobile = request.args['mobile']
          message = request.args['message']
          url = "https://control.msg91.com/api/sendhttp.php?authkey=195833ANU0xiap5a708d1f&mobiles="+mobile+"&message="+message+"&sender=Info&route=4&country=91"
          req = urllib.request.Request(url)
          with urllib.request.urlopen(req) as response:
             the_page = response.read()
             the_page = the_page[1:]
             print(the_page)
             the_page = str(the_page)    
          return(json.dumps({"Message":"SMS Sent Sucessfully","Key":the_page},indent =2))
  
        
       
       
#if __name__ == "__main__":
    #app.run(debug=True)
 #  app.run(host="192.168.1.5",port=5000)
