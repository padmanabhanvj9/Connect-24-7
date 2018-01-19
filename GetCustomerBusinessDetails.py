import json
import datetime
#import logging
import psycopg2
from flask import Flask,request,jsonify
app = Flask(__name__)

#@app.route('/getcustomer',methods=['GET'])
def getcustomerbusinessdetails():
     if request.args.get('business_id'):
        business_id = request.args['business_id']
     if request.args.get('appointment_date'):
           customer_appointment_date = request.args['appointment_date']
     try:
      con = psycopg2.connect(user='quywvejawxhnse',password='065fe8ac62d76caa061d1e517b2f0107b5776f767037c2e29cad16c259a771cf',host='ec2-176-34-113-15.eu-west-1.compute.amazonaws.com',port='5432',database='d3opaj0jiqsm0h')
      cur = con.cursor()
     except psycopg2.Error :
       return (json.dumps({'Status': 'Failure','Message':'DB connection Error'}, sort_keys=True, indent=4)) 
     sql = ("select * from customer_details where business_id="+business_id+" and customer_appointment_date = '"+customer_appointment_date+"'")
     cur.execute(sql)
     def myconverter(o):
            if isinstance(o, datetime.date):
                #d = datetime.date()
                return o.__str__()
            #if isinstance(p, datetime.date):
               #return p.__str__()

  
     columns = cur.description
     result = [{columns[index][0]:column for index, column in enumerate(value)}   for value in cur.fetchall()]
     return json.dumps(result,indent=3,default=myconverter)
     con.close()
 
 

#if __name__ == "__main__":
    #app.run(debug=True)
   #app.run(host="192.168.1.3",port="5000") 
    
