import json
import psycopg2
from flask import Flask,request,jsonify
app = Flask(__name__)
#@app.route('/getbusiness',methods=['GET'])
def QueryBusinessPrimaryall():

 try:
     try:
         con = psycopg2.connect(user='quywvejawxhnse',password='065fe8ac62d76caa061d1e517b2f0107b5776f767037c2e29cad16c259a771cf',host='ec2-176-34-113-15.eu-west-1.compute.amazonaws.com',port='5432',database='d3opaj0jiqsm0h')
         cur = con.cursor()
     except:
         print("QueryBusinessPrimaryAll::QueryBusinessPrimaryall()::sql is not connected")
     if request.args.get('business_id'):
        business_id = request.args['business_id']    
        sql = ("select * from business_primary where business_id="+business_id+"")
        cur.execute(sql)
        columns = cur.description
        result = [{columns[index][0]:column for index, column in enumerate(value)}   for value in cur.fetchall()]
        return json.dumps(result,indent=3)
     else:
        sql = ("select * from business_primary")
        cur.execute(sql)
        columns = cur.description
        result = [{columns[index][0]:column for index, column in enumerate(value)}   for value in cur.fetchall()]
        return json.dumps(result,indent=3)
        
 except:
     print("QueryBusinessPrimaryAll::QueryBusinessPrimaryall()::sql operation error")
 finally:    
     con.close()
#if __name__ == "__main__":
    #app.run(debug=True)
 #  app.run(host="192.168.1.7",port="5000")      

 
    
