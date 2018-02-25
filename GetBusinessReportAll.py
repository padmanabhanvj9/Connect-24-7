import json
import datetime
import psycopg2
from flask import Flask,request,jsonify
app = Flask(__name__)
#@app.route('/GetBusinessReportAll',methods=['GET'])     
def getbusinessreportall(request):
     business_group = request.args['business_group']     
     if request.args.get('business_group') and request.args.get('date_from') and request.args.get('date_to'):
        date_from = request.args['date_from']
        date_to = request.args['date_to']
     elif request.args.get('business_group'):
        Today_date = datetime.datetime.utcnow().date().strftime('%Y-%m-%d')
        date_from = Today_date
        date_to = Today_date
     try:
      con = psycopg2.connect(user='quywvejawxhnse',password='065fe8ac62d76caa061d1e517b2f0107b5776f767037c2e29cad16c259a771cf',host='ec2-176-34-113-15.eu-west-1.compute.amazonaws.com',port='5432',database='d3opaj0jiqsm0h')
      cur = con.cursor()
     except psycopg2.Error :
       return (json.dumps({'Status': 'Failure','Message':'DB connection Error'}, sort_keys=True, indent=4))
     sql = "select business_id from business_primary where business_group= '"+business_group+"'"
     cur.execute(sql)
     result = cur.fetchall()
     business_id,count = [],[]
     for i in result:
       for a in i:
         business_id.append(a) 
     #return(json.dumps({"business_id":business_id}))
     for b_id in business_id:
         b_id = str(b_id) 
         sql1 = "select count(*) from customer_details where business_id='"+b_id+"' and customer_appointment_date between '"+date_from+"' and '"+date_to+"' and customer_current_status in ('checkedout')"
         print(sql1)
         cur.execute(sql1)
         result = cur.fetchone()
         for i in result:
              count.append(i)
         print(count)
     return(json.dumps({"count":count}))    
     con.close()    
#if __name__ == "__main__":
    #app.run(debug=True)
 #  app.run(host="192.168.1.35",port=5000)
