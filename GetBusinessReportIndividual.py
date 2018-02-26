import json
import datetime
import psycopg2
from flask import Flask,request,jsonify
app = Flask(__name__)
#@app.route('/GetBusinessReportIndividual',methods=['GET'])
def getbusinessreport():
    try:
      con = psycopg2.connect(user='quywvejawxhnse',password='065fe8ac62d76caa061d1e517b2f0107b5776f767037c2e29cad16c259a771cf',host='ec2-176-34-113-15.eu-west-1.compute.amazonaws.com',port='5432',database='d3opaj0jiqsm0h')
      cur = con.cursor()
    except psycopg2.Error :
       return (json.dumps({'Status': 'Failure','Message':'DB connection Error'}, sort_keys=True, indent=4))
     
    i=0
    if  request.args.get('business_id') and request.args.get('appointment_date_from') and request.args.get('appointment_date_to'):
        business_id = request.args['business_id']
        customer_appointment_date_from = request.args['appointment_date_from'] 
        customer_appointment_date_to = request.args['appointment_date_to']
       
    elif request.args.get('business_id'):
       business_id = request.args['business_id']
       Today_date = datetime.datetime.utcnow().date().strftime('%Y-%m-%d')
       customer_appointment_date_from = Today_date
       customer_appointment_date_to = Today_date
    list1 = ['checkedout','cancelled','checkedin']
    var = []
    print(list1[0],list1[1],list1[2])
    while i < 3:
        print(list1[i])
        sql = ("select count(*) from customer_details where business_id="+business_id+" and customer_appointment_date between  '"+customer_appointment_date_from+"' and  '"+customer_appointment_date_to+"' and customer_current_status in('"+list1[i]+"')")
        print(sql)
        cur.execute(sql)
        result = cur.fetchone()
        for j in result:
            pass
        print(j)
        var.append(j)
        i+=1
    print(var)      
    return(json.dumps({"checkedout":var[0],"cancelled":var[1],"checkedin":var[2]}))

        
         
#if __name__ == "__main__":
    #app.run(host="192.168.1.6",port=5000)
