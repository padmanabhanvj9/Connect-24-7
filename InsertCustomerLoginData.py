import json
import datetime
import psycopg2
from flask import Flask,request,jsonify
app = Flask(__name__)
#@app.route('/InsertCustomerLoginData',methods=['POST'])
def insertcustomerlogindata(request):

     customer_login_id = request.json['customer_login_id']
     customer_login_mobile = request.json['customer_login_mobile']
     customer_login_user = request.json['customer_login_user']
     customer_login_datetime = request.json['customer_login_datetime']
     customer_login_email = request.json['customer_login_email']
     customer_login_activity = request.json['customer_login_activity']
    
     con = psycopg2.connect(user='quywvejawxhnse',password='065fe8ac62d76caa061d1e517b2f0107b5776f767037c2e29cad16c259a771cf',host='ec2-176-34-113-15.eu-west-1.compute.amazonaws.com',port='5432',database='d3opaj0jiqsm0h')
     cur = con.cursor()
     print("jhjguj")
     sql = "insert into customer_login values("+customer_login_id+",'"+customer_login_mobile+"','"+customer_login_user+"','"+customer_login_datetime+"','"+customer_login_email+"','"+customer_login_activity+"')"
     cur.execute(sql)
     con.commit()     
     return(json.dumps({'Status': 'Success', 'StatusCode': '200','Message': 'Customer Login or Logout record inserted successfully'}, sort_keys=True, indent=4))
     con.close()
     
#if __name__ == "__main__":
  # app.run(debug=True)
  #app.run(host="192.168.1.8",port=5000)
