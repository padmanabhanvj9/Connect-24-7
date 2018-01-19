#import mysql.connector
import json
#import logging
import psycopg2
from flask import Flask,request, jsonify
app = Flask(__name__)


def updatefeedback(request):
 try:   
    customer_comment_rating = request.json['customer_comment_rating']
    customer_name = request.json['customer_name']
    customer_mobile = request.json['customer_mobile']
    business_id = request.json['business_id']
    customer_email = request.json['customer_email']
    #logging.basicConfig(filename="C:\Python27\Appointment.log",
     #                   level=logging.DEBUG,
       #                 format='%(asctime)s %(filename)s %(message)s')
    
    try:
    
        con = psycopg2.connect(user='quywvejawxhnse',password='065fe8ac62d76caa061d1e517b2f0107b5776f767037c2e29cad16c259a771cf',host='ec2-176-34-113-15.eu-west-1.compute.amazonaws.com',port='5432',database='d3opaj0jiqsm0h')
        #con = mysql.connector.connect(user='root',password='root',host='192.168.1.3',port='3306',database='business')
        cursor = con.cursor()
    except:
        print("UpdateCustomerFeedback::UpdateFeedback()::SQL is not connected")
        #logging.warning("UpdateCustomerFeedback::UpdateFeedback()::SQL is not connected")
    sql = "insert into customer_feedback VALUES ('"+customer_name+"','"+customer_mobile+"','"+customer_comment_rating+"',"+business_id+",'"+customer_email+"')"
    #logging.info("UpdateCustomerFeedback::UpdateFeedback()::SQL Query " + sql)    
    cursor.execute(sql)
    con.commit()
    #logging.info(json.dumps({'Status': 'Success', 'StatusCode': '200','Message': 'feedback record inserted successfully'}, sort_keys=True, indent=4))
    #return  "{" + "Status" +":" + "Successfully update customer feedback" + "}"
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Message': 'feedback record inserted successfully'}, sort_keys=True, indent=4))
 except:
     print("UpdateCustomerFeedback::UpdateFeedback()::sql operation error")
     #logging.warning("UpdateCustomerFeedback::UpdateFeedback()::sql operation error")
 
 finally:
     con.close()


