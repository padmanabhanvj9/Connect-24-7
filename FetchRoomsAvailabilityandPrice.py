from sqlwrapper import dbget,gensql
import json
import flask
def fetchroomsavailabilityandprice(request):
    if flask.request.method == 'POST':
       b_id = request.json
       result = gensql('select','ivr_room_availability_rate','*',b_id)
       result = json.loads(result)
       return(json.dumps({"ServiceStatus": "Success",
                      "ServiceMessage": "Success", "Return Value":result},indent=2))
    else:
      result = dbget('select * from ivr_room_availability_rate')
      result = json.loads(result)
      return(json.dumps({"Return":"Record Retrieved Successfully","Return Code":"RRS", "Status": "Success",
                      "Status Code": "200", "Return Value":result},indent=2)) 
    
def fetchpromotionalmessage(request):
    result = dbget('select * from ivr_promotional_cancellation_message')
    result = json.loads(result)
    result = result[0]
    return(json.dumps({"Return":"Record Retrieved Successfully","Return Code":"RRS", "Status": "Success",
                      "Status Code": "200", "Return Value":result},indent=2))

   
