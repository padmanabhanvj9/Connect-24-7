import sys
#from urllib2 import *
#from urllib2 import urlopen
from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError
#from urllib.request import urlopen
import json
import urllib
from flask import Flask,request,jsonify
app = Flask(__name__)

#@app.route('/pushnotificationall',methods=['POST'])
def pushnotificationall(request):
    MY_API_KEY = "AIzaSyAQDQSMLhW0ihrRWaDASWPUi-U078lUn4c"
    print(MY_API_KEY)

    #messageTitle = sys.argv[1]
    #messageBody = sys.argv[2]
    messageTitle = request.json['message']
    messageBody = request.json['body']
    print(messageBody,messageTitle)
    data={
        "to" : "/topics/my_little_topic",
        "notification" : {
            "body" : messageBody,
            "title" : messageTitle,
            "icon" : "ic_cloud_white_48dp"
        }
    }
    print("hi ")
    return("hello")


