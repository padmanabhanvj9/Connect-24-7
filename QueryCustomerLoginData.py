import datetime
import json
import psycopg2
from flask import Flask,request
app = Flask(__name__)
#@app.route('/QueryCustomerLoginData',methods=['GET'])
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
def QueryCustomerLoginData():    
     if request.args.get('customer_email') and request.args.get('customer_mobile'):
        customer_email = request.args['customer_email']
        customer_mobile = request.args['customer_mobile'] 
        sql = ("select * from customer_login where customer_login_email='"+customer_email+"' and customer_login_mobile='"+customer_mobile+"'")
        print(sql)
        return(callfn(sql))
     elif request.args.get('customer_email'):
        customer_email = request.args['customer_email']
        sql = ("select * from customer_login where customer_login_email='"+customer_email+"'")
        print(sql)
        return(callfn(sql))
     elif request.args.get('customer_mobile'):
        customer_mobile = request.args['customer_mobile'] 
        sql = ("select * from customer_login where customer_login_mobile='"+customer_mobile+"'")
        print(sql)
        return(callfn(sql))
    
     else:
        sql = ("select * from customer_login")
        print(sql)
        return(callfn(sql))
     con.close()
#if __name__ == "__main__":
  # app.run(debug=True)
 # app.run(host="192.168.1.6",port=5000)  


