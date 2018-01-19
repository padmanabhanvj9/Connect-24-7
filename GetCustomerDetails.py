import json
import datetime
#import logging
import psycopg2
from flask import Flask,request
app = Flask(__name__)

def CustomerDetails():

   
    if request.args.get('customer_email'):
           customer_email = request.args['customer_email']
    if request.args.get('business_id'):
           business_id = request.args['business_id']       
    
    try:
     con = psycopg2.connect(user='quywvejawxhnse',password='065fe8ac62d76caa061d1e517b2f0107b5776f767037c2e29cad16c259a771cf',host='ec2-176-34-113-15.eu-west-1.compute.amazonaws.com',port='5432',database='d3opaj0jiqsm0h')
     cur = con.cursor()
    except psycopg2.Error :
       return (json.dumps({'Status': 'Failure','Message':'DB connection Error'}, sort_keys=True, indent=4))         
    sql = ("select * from  customer_details where customer_email='"+customer_email+"' and business_id="+business_id+"")
    cur.execute(sql)
    def myconverter(o):
                if isinstance(o, datetime.date):
                    return o.__str__()
    columns = cur.description
    result = [{columns[index][0]:column for index, column in enumerate(value)}   for value in cur.fetchall()]
    return json.dumps(result,indent=3,default = myconverter)
    con.close()
 
 
 


 

