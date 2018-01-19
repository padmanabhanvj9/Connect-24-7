import datetime
import json
import psycopg2
from flask import Flask,request
app = Flask(__name__)
#@app.route('/QueryBusinessLoginData',methods=['GET'])
def QueryBusinessLoginData():
    con = psycopg2.connect(user='quywvejawxhnse',password='065fe8ac62d76caa061d1e517b2f0107b5776f767037c2e29cad16c259a771cf',host='ec2-176-34-113-15.eu-west-1.compute.amazonaws.com',port='5432',database='d3opaj0jiqsm0h')
    cur = con.cursor()

    if request.args.get('business_login_id') and request.args.get('business_login_email'):
        business_login_id = request.args['business_login_id']
        business_login_email = request.args['business_login_email'] 
        sql = ("select count(*) from  business_login where business_login_id="+business_login_id+" and business_login_emil='"+business_login_email+"'")
        cur.execute(sql)
        result=cur.fetchone()
        count = result[0]
        print(type(count),count)
        if count > 0:
           return(json.dumps({'Status': 'Success'}, sort_keys=True, indent=4))
        else:
           return(json.dumps({'Status': 'Failure'}, sort_keys=True, indent=4))
    elif request.args.get('business_login_id'):
        business_login_id = request.args['business_login_id']
        sql = ("select * from business_login where business_login_id="+business_login_id+"")
        print(sql)
        #return(callfn(sql)) 
        cur.execute(sql)
        def myconverter(o):
            if isinstance(o, datetime.date):
                return o.__str__()  
        columns = cur.description
        result = [{columns[index][0]:column for index, column in enumerate(value)}   for value in cur.fetchall()]
        return( json.dumps(result,indent=3,default=myconverter))
    con.close()          
#if __name__ == "__main__":
 #   app.run(debug=True)
 #app.run(host="192.168.1.7",port="5000")
