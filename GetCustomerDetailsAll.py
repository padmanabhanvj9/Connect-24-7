import json
import datetime
import psycopg2
from flask import Flask,request,jsonify
app = Flask(__name__)
#@app.route('/GetCustomerDetailsAll',methods=['GET'])
def callfn(sql):
     try:
      con = psycopg2.connect(user='quywvejawxhnse',password='065fe8ac62d76caa061d1e517b2f0107b5776f767037c2e29cad16c259a771cf',host='ec2-176-34-113-15.eu-west-1.compute.amazonaws.com',port='5432',database='d3opaj0jiqsm0h')
      cur = con.cursor()
     except psycopg2.Error :
       return (json.dumps({'Status': 'Failure','Message':'DB connection Error'}, sort_keys=True, indent=4))
     cur.execute(sql)
     def myconverter(o):
            if isinstance(o, datetime.date):
                return o.__str__()  
     columns = cur.description
     result = [{columns[index][0]:column for index, column in enumerate(value)}   for value in cur.fetchall()]
     fresult= json.dumps(result,indent=3,default=myconverter)
     return(fresult)     
def getcustomerdetailsall():
     print("getcustomerdetailsall")
     if request.args.get('business_id') and request.args.get('appointment_date'):
        business_id = request.args['business_id']
        customer_appointment_date = request.args['appointment_date']
        print("1")
        sql = ("select * from customer_details where business_id="+business_id+" and customer_appointment_date='"+customer_appointment_date+"' order by case when substring(customer_token_num from '^\d+$') is null then 9999 else cast(customer_token_num as integer) end,customer_token_num")
        print(sql)
        return(callfn(sql)) 
     elif  request.args.get('business_id'):
        business_id = request.args['business_id']
        print("2")
        sql = ("select * from customer_details where business_id="+business_id+" order by customer_appointment_date,case when substring(customer_token_num from '^\d+$') is null then 9999 else cast(customer_token_num as integer) end,customer_token_num")
        print(sql)
        return(callfn(sql)) 
     elif  request.args.get('appointment_date'):
        customer_appointment_date = request.args['appointment_date']
        sql = ("select * from customer_details where customer_appointment_date='"+customer_appointment_date+"' order by case when substring(customer_token_num from '^\d+$') is null then 9999 else cast(customer_token_num as integer) end,customer_token_num")
        print(sql)
        return(callfn(sql)) 
     else:
        sql = ("select * from customer_details order by case when substring(customer_token_num from '^\d+$') is null then 9999 else cast(customer_token_num as integer) end,customer_token_num")
        print(sql)
        return(callfn(sql))
     con.close()    
#if __name__ == "__main__":
    #app.run(debug=True)
 #  app.run(host="192.168.1.4",port="5000")
