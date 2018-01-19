import json
import psycopg2
import datetime
import sys
#sys.stdout.flush()
from flask import Flask,request,jsonify
app = Flask(__name__)
#@app.route('/UpdateCustomerStatus',methods=['POST'])
def updatecustomerstatus(request):
    #today_date = datetime.datetime.now().date().strftime("%Y-%m-%d")
    business_id = request.json['business_id']
    customer_access_datetime = request.json['customer_access_datetime']
    customer_name = request.json['customer_name']
    customer_email = request.json['customer_email']
    customer_current_status = request.json['customer_current_status']
    customer_appointment_time = request.json['customer_appointment_time']
    customer_appointment_date = request.json['customer_appointment_date']
    try:
     con = psycopg2.connect(user='quywvejawxhnse',password='065fe8ac62d76caa061d1e517b2f0107b5776f767037c2e29cad16c259a771cf',host='ec2-176-34-113-15.eu-west-1.compute.amazonaws.com',port='5432',database='d3opaj0jiqsm0h')
     cur = con.cursor()
    except psycopg2.Error :
       return (json.dumps({'Status': 'Failure','Message':'DB connection Error'}, sort_keys=True, indent=4))
    sqlend = ("select business_appointment_type from business_primary where  business_id = "+business_id+"")
    print(sqlend)
    cur.execute(sqlend)
    result=cur.fetchone()
    b_type = result[0]
    print(b_type)
    if b_type in ['slot']:
        acc_time=''
        if customer_current_status in ['booked']:
          sql = "select customer_access_datetime from customer_details where business_id="+business_id+" and customer_email='"+customer_email+"' and customer_current_status IN ('checkedin_appointment') order by customer_access_datetime desc limit 1"
          print(sql)
          cur.execute(sql)
          time_val = cur.fetchone()
          for acc_time in time_val:
            #print(acc_time)
            acc_time=str(acc_time)
          print(type(acc_time),acc_time)
          sql=("update customer_details set customer_appointment_date='"+customer_appointment_date+"' where business_id="+business_id+" and customer_email='"+customer_email+"' and  customer_access_datetime='"+acc_time+"'")
          print(sql)
          cur.execute(sql)
          con.commit()
        elif customer_current_status in ['rescheduled','cancelled']:
            sqlupdate = ("update customer_details set customer_access_datetime='"+customer_access_datetime+"',customer_current_status='"+customer_current_status+"',customer_appointment_time='"+customer_appointment_time+"' where  business_id='"+business_id+"' and customer_name='"+customer_name+"' and customer_email='"+customer_email+"' and customer_appointment_date='"+customer_appointment_date+"'")
            print(sqlupdate)
            cur.execute(sqlupdate)
            con.commit()
            return(json.dumps({'Status': 'Success', 'StatusCode': '200','Message': 'customer details updated successfully'}, sort_keys=True, indent=4))
            cur.close()
            con.close()
            
        time=[]
        psqlselect = ("select customer_appointment_time from customer_details where business_id="+business_id+" and customer_appointment_date='"+customer_appointment_date+"'and  customer_current_status NOT IN ('checkedin_appointment','cancelled','rescheduled')")
        cur.execute(psqlselect)
        data = cur.fetchall()
         #print(data)
        for result in data:
          for field in result:
            time.append(field)
        print(time)
        if customer_appointment_time in time and customer_current_status not in ['checkedout','cancelled','rescheduled']:
            return(json.dumps({'Status': 'Success', 'StatusCode': '200','Message': 'Appointment time booked already'}, sort_keys=True, indent=4))

    sql = ("select customer_current_status from customer_details where business_id="+business_id+" and customer_email='"+customer_email+"' and customer_appointment_date='"+customer_appointment_date+"'")
    print(sql)
    cur.execute(sql)
    data = cur.fetchall()
    for field in data:
        for status in field: 
               print(status,type(status))
    print(status,type(status))       
    
        
    if status in ['booked']  and customer_current_status == status :
       return(json.dumps({'Status': 'Success', 'StatusCode': '200','Message': 'Appointment Booked Already'}, sort_keys=True, indent=4))
    if status in ['checkedout'] and customer_current_status == status :
       return(json.dumps({'Status': 'Success', 'StatusCode': '200','Message': 'Checkedout Already'}, sort_keys=True, indent=4))
    
    sqlupdate = ("update customer_details set customer_access_datetime='"+customer_access_datetime+"',customer_current_status='"+customer_current_status+"',customer_appointment_time='"+customer_appointment_time+"' where  business_id='"+business_id+"' and customer_name='"+customer_name+"' and customer_email='"+customer_email+"' and customer_appointment_date='"+customer_appointment_date+"'")
    print(sqlupdate)
    cur.execute(sqlupdate)
    con.commit()
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Message': 'customer details updated successfully'}, sort_keys=True, indent=4))
    cur.close()
    con.close()

 
 

#if __name__ == "__main__":
    #app.run(debug=True)
 # app.run(host='192.168.1.7',port='5000')     
