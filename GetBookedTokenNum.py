import json
import datetime
import psycopg2
from flask import Flask,request,jsonify
app = Flask(__name__)


def bookedtokennumber():
 try:
     if request.args.get('business_id'):
           business_id = request.args['business_id']
     try:
         con = psycopg2.connect(user='quywvejawxhnse',password='065fe8ac62d76caa061d1e517b2f0107b5776f767037c2e29cad16c259a771cf',host='ec2-176-34-113-15.eu-west-1.compute.amazonaws.com',port='5432',database='d3opaj0jiqsm0h')
         cur = con.cursor()
     except:
         print("GetbookedTokenNum::bookedtokennumber()::sql is not connected")
     sql = ("SELECT customer_token_num FROM customer_details where business_id="+business_id+" and DATE(customer_appointment_date) = DATE(NOW()) order by customer_token_num desc LIMIT 5")
     cur.execute(sql)
     def myconverter(o):
            if isinstance(o, datetime.datetime):
                    return o.__str__()  

     columns = cur.description
     result = [{columns[index][0]:column for index, column in enumerate(value)}   for value in cur.fetchall()]
     return json.dumps(result,indent=3,default=myconverter)
 except:
     print("GetbookedTokenNum::bookedtokennumber()::sql operation error")
 finally:
     con.close()

 

    
