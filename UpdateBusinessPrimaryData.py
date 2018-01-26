import json
import psycopg2
from flask import Flask,request,jsonify
app = Flask(__name__)

def callfn(sql):
     print("callfn")
     con = psycopg2.connect(user='quywvejawxhnse',password='065fe8ac62d76caa061d1e517b2f0107b5776f767037c2e29cad16c259a771cf',host='ec2-176-34-113-15.eu-west-1.compute.amazonaws.com',port='5432',database='d3opaj0jiqsm0h')
     cur = con.cursor()
     cur.execute(sql)
     con.commit()
     print("fine")
     return("sucess")
     #return(json.dumps({'Status': 'Success', 'StatusCode': '200','Message': 'Business primary record update successfully'}, sort_keys=True, indent=4))
     
 #,business_break_time_start='"+business_break_time_start+"',business_break_time_end='"+business_break_time_end+"',business_avg_wait_time_min="+business_avg_wait_time_min+"    
def updatebusinessprimary(request):
          
     #a = request.get_json().get('business_id')
     #print(a['business_id'])
     #print(a)
     if request.get_json().get('business_id') and request.get_json().get('business_hour_start') and request.get_json().get('business_hour_end') and request.get_json().get('business_break_time_start') and request.get_json().get('business_break_time_end') and request.get_json().get('business_avg_wait_time_min'):
          business_id = request.json['business_id']
          business_hour_start = request.json['business_hour_start']
          business_hour_end = request.json['business_hour_end']
          business_break_time_start = request.json['business_break_time_start']
          business_break_time_end = request.json['business_break_time_end']
          business_avg_wait_time_min = request.json['business_avg_wait_time_min']
          sql = ("update business_primary set business_hour_start='"+business_hour_start+"',business_hour_end='"+business_hour_end+"',business_break_time_start='"+business_break_time_start+"',business_break_time_end='"+business_break_time_end+"',business_avg_wait_time_min="+business_avg_wait_time_min+" where business_id = "+business_id+"")
          print(sql)
          return(json.dumps({'Status': callfn(sql), 'StatusCode': '200','Message': 'Business primary record update successfully'}, sort_keys=True, indent=4))

     elif request.get_json().get('business_id') and  request.get_json().get('business_hour_start') and request.get_json().get('business_hour_end'):
        business_id = request.json['business_id']
        business_hour_start = request.json['business_hour_start']
        business_hour_end = request.json['business_hour_end']
        #print(business_id,business_hour_start,business_hour_end)
        sql = ("update business_primary set business_hour_start='"+business_hour_start+"',business_hour_end='"+business_hour_end+"' where business_id = "+business_id+"")
        print(sql)
        return(json.dumps({'Status': callfn(sql), 'StatusCode': '200','Message': 'Business primary record update successfully'}, sort_keys=True, indent=4))
     elif request.get_json().get('business_id') and request.get_json().get('business_break_time_start') and request.get_json().get('business_break_time_end'):
        business_id = request.json['business_id']
        business_break_time_start = request.json['business_break_time_start']
        business_break_time_end = request.json['business_break_time_end']
        sql = ("update business_primary set business_break_time_start='"+business_break_time_start+"',business_break_time_end='"+business_break_time_end+"' where business_id = "+business_id+"")
        print(sql)
        return(json.dumps({'Status': callfn(sql), 'StatusCode': '200','Message': 'Business primary record update successfully'}, sort_keys=True, indent=4))
     elif request.get_json().get('business_id') and request.get_json().get('business_hour_start'):
        business_id = request.json['business_id']
        business_hour_start = request.json['business_hour_start']
        sql = ("update business_primary set business_hour_start='"+business_hour_start+"' where business_id = "+business_id+"")
        print(sql)
        return(json.dumps({'Status': callfn(sql), 'StatusCode': '200','Message': 'Business primary record update successfully'}, sort_keys=True, indent=4))
     elif request.get_json().get('business_id') and request.get_json().get('business_hour_end'):
        business_id = request.json['business_id']
        business_hour_end = request.json['business_hour_end']
        sql = ("update business_primary set business_hour_end='"+business_hour_end+"' where business_id = "+business_id+"")
        print(sql)
        return(json.dumps({'Status': callfn(sql), 'StatusCode': '200','Message': 'Business primary record update successfully'}, sort_keys=True, indent=4))
     elif request.get_json().get('business_id') and request.get_json().get('business_break_time_start'):
        business_id = request.json['business_id']
        business_break_time_start = request.json['business_break_time_start']
        sql = ("update business_primary set business_break_time_start='"+business_break_time_start+"' where business_id = "+business_id+"")
        print(sql)
        return(json.dumps({'Status': callfn(sql), 'StatusCode': '200','Message': 'Business primary record update successfully'}, sort_keys=True, indent=4))
     elif request.get_json().get('business_id') and request.get_json().get('business_break_time_end'):
        business_id = request.json['business_id']
        business_break_time_end = request.json['business_break_time_end']
        sql = ("update business_primary set business_break_time_end='"+business_break_time_end+"' where business_id = "+business_id+"")
        print(sql)
        return(json.dumps({'Status': callfn(sql), 'StatusCode': '200','Message': 'Business primary record update successfully'}, sort_keys=True, indent=4))
     elif request.get_json().get('business_id') and request.get_json().get('business_avg_wait_time_min'):
        business_id = request.json['business_id']
        business_avg_wait_time_min = request.json['business_avg_wait_time_min']
        sql = ("update business_primary set business_avg_wait_time_min="+business_avg_wait_time_min+" where business_id = "+business_id+"")
        print(sql)
        return(json.dumps({'Status': callfn(sql), 'StatusCode': '200','Message': 'Business primary record update successfully'}, sort_keys=True, indent=4))
     else:
          return("done")
  




    
