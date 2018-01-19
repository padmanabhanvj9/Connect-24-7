import json
import datetime
import psycopg2
from flask import Flask,request,jsonify
app = Flask(__name__)

def insertbusinessprimary(request):
     business_id = request.json['business_id']
     business_first_name = request.json['business_first_name']
     business_last_name = request.json['business_last_name']
     business_type = request.json['business_type']
     business_category1 = request.json['business_category1']
     business_category2 = request.json['business_category2']
     business_mobile = request.json['business_mobile']
     business_hour_start = request.json['business_hour_start']
     business_hour_end = request.json['business_hour_end']
     business_break_time_start = request.json['business_break_time_start']
     business_break_time_end = request.json['business_break_time_end']
     business_avg_wait_time_min = request.json['business_avg_wait_time_min']
     business_address = request.json['business_address']
     business_photo_url = request.json['business_photo_url']
     business_rating = request.json['business_rating']
     business_group = request.json['business_group']
     business_id_range = request.json['business_id_range']
     business_mode = request.json['business_mode']
     business_appointment_type = request.json['business_appointment_type']
        
     con = psycopg2.connect(user='quywvejawxhnse',password='065fe8ac62d76caa061d1e517b2f0107b5776f767037c2e29cad16c259a771cf',host='ec2-176-34-113-15.eu-west-1.compute.amazonaws.com',port='5432',database='d3opaj0jiqsm0h')
     cur = con.cursor()
     sql = ("select count(*) from business_primary where business_id = "+business_id+"")
     cur.execute(sql)
     result = cur.fetchall()
     for field in result:
       for rowcount in field:
            print(rowcount)
     rowcount_mode  = ''
     type_filed = []
     sql = ("select business_mode from business_primary where business_id = "+business_id+"")
     cur.execute(sql)
     result_business_mode = cur.fetchall()
     for field_mode in result_business_mode:
       for rowcount_mode in field_mode:
            print("business_mode",rowcount_mode)
     sql = ("select business_type from business_primary")
     cur.execute(sql)
     result_business_mode = cur.fetchall()
     for field_mode in result_business_mode:
       for rowcount_type in field_mode:
            type_filed.append(rowcount_type)
     print(type_filed)
     print(business_type)
     if business_mode == 'single' and business_type in type_filed:
          return json.dumps({'Status': 'Success', 'StatusCode': '200','Message': 'Unable to insert for single'}, sort_keys=True, indent=4)            
     if rowcount > 0 :
          return json.dumps({'Status': 'Success', 'StatusCode': '200','Message': 'Already Exists'}, sort_keys=True, indent=4)
     psql = "insert into business_primary VALUES ("+business_id+",'"+business_first_name+"', '"+business_last_name+"','"+business_type+"','"+business_category1+"','"+business_category2+"','"+business_mobile+"','"+business_hour_start+"','"+business_hour_end+"','"+business_break_time_start+"','"+business_break_time_end+"',"+business_avg_wait_time_min+",'"+business_address+"','"+business_photo_url+"','"+business_rating+"','"+business_group+"','"+business_id_range+"','"+business_mode+"','"+business_appointment_type+"')"
     cur.execute(psql)
     con.commit()
     print(psql)
     return(json.dumps({'Status': 'Success', 'StatusCode': '200','Message': 'Business primary record inserted successfully'}, sort_keys=True, indent=4))
     con.close()
     cur.close()




    
