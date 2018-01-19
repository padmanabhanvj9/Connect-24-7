import json
import datetime
import psycopg2
from flask import Flask,request,jsonify
app = Flask(__name__)
#@app.route('/livefeed',methods=['GET'])
def getlivefeed():
   
     if request.args.get('business_id'):
        business_id = request.args['business_id']
     try:
      con = psycopg2.connect(user='quywvejawxhnse',password='065fe8ac62d76caa061d1e517b2f0107b5776f767037c2e29cad16c259a771cf',host='ec2-176-34-113-15.eu-west-1.compute.amazonaws.com',port='5432',database='d3opaj0jiqsm0h')
      cur = con.cursor()
     except psycopg2.Error :
       return (json.dumps({'Status': 'Failure','Message':'DB connection Error'}, sort_keys=True, indent=4)) 
     sql = ("select business_appointment_type from business_primary where business_id = "+business_id+"")
     cur.execute(sql)
     data = cur.fetchall()
     for field in data:
          for result in field:
               print(result)
     if result in ['slot']:
          psql = ("select customer_access_datetime,customer_appointment_time, customer_current_status from customer_details where DATE(customer_appointment_date) = DATE(NOW()) and business_id = "+business_id+" and customer_current_status in('cancelled','checkedout') order by   customer_access_datetime desc limit 4")
          print(psql)
          cur.execute(psql)
          print(cur.execute(psql))
          def myconverter(o):
                    if isinstance(o, datetime.datetime):
                         return o.__str__()  

          columns = cur.description
          final = [{columns[index][0]:column for index, column in enumerate(value)}   for value in cur.fetchall()]
          print(final)
          return json.dumps(final,indent=3,default=myconverter)
     else:
          sqltoken = ("select customer_token_num,customer_current_status,customer_access_datetime from customer_details where DATE(customer_appointment_date) = DATE(NOW()) and business_id = "+business_id+" and customer_current_status in('cancelled','checkedout') order by   customer_access_datetime desc limit 4")
          cur.execute(sqltoken)
          def myconverter(o):
                    if isinstance(o, datetime.datetime):
                         return o.__str__()  

          columns = cur.description
          tokenresult = [{columns[index][0]:column for index, column in enumerate(value)}   for value in cur.fetchall()]
          return json.dumps(tokenresult,indent=3,default=myconverter)
   
     con.close()
     



#if __name__ == "__main__":
    #app.run(debug=True)
    #app.run(host='192.168.1.5',port='5000')

    
