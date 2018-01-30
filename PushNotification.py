from urllib import *
import urllib
import json
import sys
import urllib.request
from flask import Flask,request,jsonify
app = Flask(__name__)
@app.route('/pushnotification',methods=['POST'])
def pushnotification():
    print('my first pytho script')

    MY_API_KEY="AtsbgtsqwN6RaghTXVzblL9It_LHu7OcAdZ"
    messageTitle = request.json['message']
    messageBody = request.json['body']
    #messageTitle = sys.argv[1]
    #messageBody = sys.argv[2]

    values={
    "to" : "/topics/my_little_topic",
    "notification" : {
    "body" : messageBody,
    "title" : messageTitle,
    "icon" : "ic_launcher"
    }
    }

    dataAsJSON = json.dumps(values).encode('utf-8')

    request1 = urllib.request.Request(
    "https://gcm-http.googleapis...",
    dataAsJSON ,
    { "Authorization" : "key="+MY_API_KEY,
    "Content-type" : "application/json"
    }
    )

    print(urllib.request.urlopen(request1).read())
    return(urllib.request.urlopen(request1).read())
