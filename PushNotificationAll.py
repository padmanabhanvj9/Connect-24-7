
import urllib.request

from flask import Flask,request,jsonify
app = Flask(__name__)

#@app.route('/pushnotificationall',methods=['POST'])
def pushnotificationall(request):


    req = urllib.request.Request('http://www.voidspace.org.uk')
    response = urllib.request.urlopen(req)
    the_page = response.read()
    print(the_page)
    return(the_page)
    

