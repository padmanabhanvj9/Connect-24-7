import json
import datetime
import psycopg2
from flask import Flask,request,jsonify
app = Flask(__name__)
def insertbusinesslogindata(request):
     business_login_id = request.json['business_login_id']
     business_login_mobile = request.json['business_login_mobile']
     business_login_email = request.json['business_login_email']
     business_login_user =  request.json['business_login_user']
     login_datetime = request.json['login_datetime']
     login_activity = request.json['login_activity'] 
     con = psycopg2.connect(user='quywvejawxhnse',password='065fe8ac62d76caa061d1e517b2f0107b5776f767037c2e29cad16c259a771cf',host='ec2-176-34-113-15.eu-west-1.compute.amazonaws.com',port='5432',database='d3opaj0jiqsm0h')
     cur = con.cursor()
     psql = "insert into business_login VALUES ("+business_login_id+",'"+business_login_mobile+"','"+business_login_email+"','"+business_login_user+"','"+login_datetime+"','"+login_activity+"')"
     print(psql)
     cur.execute(psql)
     con.commit()     
     return(json.dumps({'Status': 'Success', 'StatusCode': '200','Message': 'Business Login or Logout record inserted successfully'}, sort_keys=True, indent=4))
     con.close()
     


    
