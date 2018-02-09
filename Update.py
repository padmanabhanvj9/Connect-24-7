import json
import psycopg2
import datetime
from flask import Flask,request,jsonify
app = Flask(__name__)

#@app.route('/update',methods=['POST'])
def updatecustomerinfo(request):
    try:
     con = psycopg2.connect(user='quywvejawxhnse',password='065fe8ac62d76caa061d1e517b2f0107b5776f767037c2e29cad16c259a771cf',host='ec2-176-34-113-15.eu-west-1.compute.amazonaws.com',port='5432',database='d3opaj0jiqsm0h')
     cursor = con.cursor()
    except psycopg2.Error :
       return (json.dumps({'Status': 'Failure','Message':'DB connection Error'}, sort_keys=True, indent=4)) 

    if request.method == 'GET':
        business_id = request.args['business_id']
        customer_email = request.args['customer_email']
        customer_appointment_date = request.args['customer_appointment_date']
        reson_code = request.args['reson_code'] 
        upsql = "update customer_details set reason_code='"+reson_code+"' where business_id="+business_id+" and customer_email='"+customer_email+"' and  customer_appointment_date='"+customer_appointment_date+"'"
        print(upsql)
        cursor.execute(upsql)
        con.commit()
        return(json.dumps({'Status': 'Success', 'StatusCode': '200','Message': 'customer details updated successfully'}, sort_keys=True, indent=4))
        
    current_time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    current_time = current_time.strftime('%H:%M')
    Today_date = datetime.datetime.utcnow().date().strftime('%Y-%m-%d') 
    print(Today_date)
    business_id = request.json['business_id']
    customer_checkin_date = request.json['customer_checkin_date']
    customer_access_datetime = request.json['customer_access_datetime']
    customer_name = request.json['customer_name']
    customer_mobile = request.json['customer_mobile']
    customer_email = request.json['customer_email']
    customer_token_num = request.json['customer_token_num']
    customer_current_status = request.json['customer_current_status']
    customer_appointment_time = request.json['customer_appointment_time']
    customer_latlong = request.json['customer_latlong']
    customer_gender = request.json['customer_gender']
    customer_photo_url = request.json['customer_photo_url']
    customer_deviceid = request.json['customer_deviceid']
    customer_consolidated_activities = request.json['customer_consolidated_activities']
    customer_appointment_date = request.json['customer_appointment_date']
    sqlend = ("select business_hour_end ,business_appointment_type from business_primary where  business_id = "+business_id+" ")
    print(sqlend)
    cursor.execute(sqlend)
    result=cursor.fetchone()
    business_end_time = result[0]
    b_type = result[1]
    print(business_end_time)
    print( b_type)
    if b_type in ['token']:
      if customer_appointment_date != Today_date:
          return (json.dumps({'Status': 'Success', 'StatusCode': '200','Message':"Token can't be generated other than today"}, sort_keys=True, indent=4)) 
      if business_end_time <= current_time :
          return (json.dumps({'Status': 'Success', 'StatusCode': '200','Message':'AOH'}, sort_keys=True, indent=4))
      else:
        result =''
        sqlselect = ("select customer_current_status,customer_token_num from customer_details where customer_appointment_date = '"+customer_appointment_date+"' and business_id = '"+business_id+"' and customer_email='"+customer_email+"'")
        print(sqlselect)
        cursor.execute(sqlselect)
        result = cursor.fetchone()
        print(result)                
        if result is None: 
           sql = "insert into customer_details VALUES ("+business_id+",'"+customer_checkin_date+"', '"+customer_access_datetime+"','"+customer_name+"','"+customer_mobile+"','"+customer_email+"',"+customer_token_num+",'"+customer_current_status+"','"+customer_appointment_time+"','"+customer_latlong+"','"+customer_gender+"','"+customer_photo_url+"','"+customer_deviceid+"','"+customer_consolidated_activities+"','"+customer_appointment_date+"')"
           cursor.execute(sql)
           con.commit()
           return(json.dumps({'Status': 'Success', 'StatusCode': '200','Message': 'customer details inserted successfully'}, sort_keys=True, indent=4))
        else:

            #for field in result:
             #   print(field)
            field = result[0]
            token = result[1]
            print(field,token)
            if field in ['booked','checkedout']:
                return(json.dumps({'Status': 'Success', 'StatusCode': '200','Message': 'AlreadyExists','Token':token}, sort_keys=True, indent=4))
            elif field in ['checkedin']:
                print('i am in checked')
                pass
                return(json.dumps({'Status': 'Success', 'StatusCode': '200','Message': 'Already Checkedin Today'}, sort_keys=True, indent=4))
            elif field in ['cancelled']:
                sqlupdate = ("update customer_details set customer_access_datetime='"+customer_access_datetime+"',customer_current_status='"+field+"',customer_token_num='0' where business_id='"+business_id+"' and customer_name='"+customer_name+"' and customer_email='"+customer_email+"'and customer_appointment_date='"+customer_appointment_date+"'")
                print(sqlupdate)
                cursor.execute(sqlupdate)
                con.commit()       
                return(json.dumps({'Status': 'Success', 'StatusCode': '200','Message': 'customer details updated successfully'}, sort_keys=True, indent=4))				
    else:
        if b_type in ['slot']:
            if customer_appointment_date < Today_date:
                return(json.dumps({'Status': 'Success', 'StatusCode': '200','Message': 'Unable to generate slot for yesterday'}, sort_keys=True, indent=4))
            else:
                result =''
                sqlselect = ("select customer_current_status,customer_appointment_time from customer_details where customer_appointment_date = '"+customer_appointment_date+"' and business_id = '"+business_id+"' and customer_email='"+customer_email+"'")
                print(sqlselect)
                cursor.execute(sqlselect)
                result = cursor.fetchone()
                print(result)                
                if result is None: 
                   sql = "insert into customer_details VALUES ("+business_id+",'"+customer_checkin_date+"', '"+customer_access_datetime+"','"+customer_name+"','"+customer_mobile+"','"+customer_email+"',"+customer_token_num+",'"+customer_current_status+"','"+customer_appointment_time+"','"+customer_latlong+"','"+customer_gender+"','"+customer_photo_url+"','"+customer_deviceid+"','"+customer_consolidated_activities+"','"+customer_appointment_date+"')"
                   cursor.execute(sql)
                   con.commit()
                   return(json.dumps({'Status': 'Success', 'StatusCode': '200','Message': 'customer details inserted successfully'}, sort_keys=True, indent=4))
                else:
                    #for field in result:
                     #print(field)
                    field = result[0]
                    slot = result[1]
                    print(field,slot)
                    if field in ['booked','checkedout']:
                      return(json.dumps({'Status': 'Success', 'StatusCode': '200','Message': 'AlreadyExists','Slot':slot}, sort_keys=True, indent=4))
                    elif field in ['checkedin_appointment']:
                        pass
                        return(json.dumps({'Status': 'Success', 'StatusCode': '200','Message': 'Already Checkedin Today'}, sort_keys=True, indent=4))
                    elif field in ['cancelled']:
                        sqlupdate = ("update customer_details set customer_access_datetime='"+customer_access_datetime+"',customer_current_status='"+customer_current_status+"',customer_appointment_time='"+customer_appointment_time+"' where business_id='"+business_id+"' and customer_name='"+customer_name+"' and customer_email='"+customer_email+"'and customer_appointment_date='"+customer_appointment_date+"'")
                        print(sqlupdate)
                        cursor.execute(sqlupdate)
                        con.commit()
                        return(json.dumps({'Status': 'Success', 'StatusCode': '200','Message': 'customer details updated successfully'}, sort_keys=True, indent=4))


    con.close()
 
#if __name__ == "__main__":
        #app.run(debug=True)
 #  app.run(host='192.168.1.7',port='5000')
