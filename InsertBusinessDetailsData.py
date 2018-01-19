import json
import datetime
import psycopg2
from flask import Flask,request,jsonify
app = Flask(__name__)

def insertbusinessdetails(request):
     business_id = request.json['business_id']
     business_first_name = request.json['business_first_name']
     business_last_name = request.json['business_last_name']
     business_checkin_date = request.json['business_checkin_date']
     business_checkout_date = request.json['business_checkout_date']
     business_latlong = request.json['business_latlong']
     business_mobile = request.json['business_mobile']
        
     con = psycopg2.connect(user='quywvejawxhnse',password='065fe8ac62d76caa061d1e517b2f0107b5776f767037c2e29cad16c259a771cf',host='ec2-176-34-113-15.eu-west-1.compute.amazonaws.com',port='5432',database='d3opaj0jiqsm0h')
     cur = con.cursor()
     sql = ("select count(*) from business_details where business_id = "+business_id+"")
     cur.execute(sql)
     result = cur.fetchall()
     for field in result:
       for rowcount in field:
            
            print(rowcount)
     #data = cur.fetchall()
     #for field in data:
          #for result in field:
               #print(result)
     if rowcount == 1:
          return json.dumps({'Status': 'Success', 'StatusCode': '200','Message': 'Record Already Exists'}, sort_keys=True, indent=4)
     else:
          psql = "insert into business_details VALUES ("+business_id+",'"+business_first_name+"', '"+business_last_name+"','"+business_checkin_date+"','"+business_checkout_date+"','"+business_latlong+"','"+business_mobile+"')"
       
          cur.execute(psql)
          con.commit()
          print(psql)
          return(json.dumps({'Status': 'Success', 'StatusCode': '200','Message': 'Business Details record inserted successfully'}, sort_keys=True, indent=4))
     con.close()
     cur.close()


    
