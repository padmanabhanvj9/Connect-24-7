import sys
from urllib2 import *
from urllib2 import urlopen
import json
import urllib
from flask import Flask,request,jsonify
app = Flask(__name__)

#@app.route('/pushnotification',methods=['POST'])
def pushnotification(request):
    MY_API_KEY = "AIzaSyAQDQSMLhW0ihrRWaDASWPUi-U078lUn4c"

    #messageTitle = sys.argv[1]
    #messageBody = sys.argv[2]
    messageTitle = "PushNotification success..."
    messageBody = "Appointment Confirmed"
#"to" : "/topics/my_little_topic",
    data={
        "to" : "erfSJuB-PAE:APA91bFK-hHU17WreM8YAJBHC_RONgpZ96f4AglKYuy48x1h7wSmdggl4f2a_JdwB84rId1D7qb-NnKna4zQtZEY6tyKmDclwQOHAg1Ue9aRjB2Q8OhqjrJFJJ9Wmw8_OE98YfXBbDey",
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

    print (urlopen(request1).read())
    return(urlopen(request1).read())

#pushnotification()
#if __name__ == "__main__":
 #   app.run(debug=True)
 # app.run(host="192.168.1.2",port=5000)
