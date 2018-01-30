import sys
from urllib2 import *
import json
import urllib
import request
from flask import Flask,request,jsonify

app = Flask(__name__)
#@app.route('/pushnotification',methods=['POST'])
def pushnotification(request):
    MY_API_KEY = "AIzaSyB6r90CECFsLXq3bt8WZGTOHLvsJHqFGt4"
    
    messageTitle = request.json['message']
    messageBody = request.json['body']
    print(messageBody)
    #messageTitle = "PushNotification success..."
    #messageBody = "Appointment Confirmed"


    data={
        "to" : "/topics/my_little_topic",
        "notification" : {
            "body" : messageBody,
            "title" : messageTitle,
            "icon" : "ic_cloud_white_48dp"
        }
    }   

    dataAsJSON = json.dumps(data)

    request1 = Request(
        "https://gcm-http.googleapis.com/gcm/send",
        dataAsJSON,
        { "Authorization" : "key="+MY_API_KEY,
          "Content-type" : "application/json"
        }
    )

    print urlopen(request1).read()
    return(urlopen(request1).read())


#if __name__ == "__main__":
 #   app.run(debug=True)
 # app.run(host="192.168.1.5",port="5000")
