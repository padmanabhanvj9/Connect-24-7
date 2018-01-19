import json
from flask import Flask,request,jsonify
app = Flask(__name__)
#@app.route('/AppointmentChatbots',methods=['POST'])
def test(request):
       #request.args.get('message')
       #speech = request.args['message']
       speech = request.json['text']
       if speech == 'hello':
          #print(message)
           print("Success")
           #return("Success")
           return json.dumps({"speech": speech,"displayText": speech,"source": "postgresheroku"})
       else:
           print("Failure")
           #return("failure")
           return json.dumps({"speech": "Failure","displayText": "Failure","source": "postgresheroku"})
		   


        
#if __name__ == "__main__":
    #app.run(debug=True)
    #app.run(host="192.168.1.7",port="5000")
