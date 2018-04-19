from sqlwrapper import dbget
import json
def fetchroomsavailabilityandprice(request):
    result = dbget('select * from ivr_room_availability_rate')
    result = json.loads(result)
    #result = result[0]
    return(json.dumps({"Return":"Record Retrieved Successfully","Return Code":"RRS", "Status": "Success",
                      "Status Code": "200", "Return Value":result},indent=2))

    
def fetchpromotionalmessage(request):
    result = dbget('select * from ivr_promotional_cancellation_message')
    result = json.loads(result)
    result = result[0]
    return(json.dumps({"Return":"Record Retrieved Successfully","Return Code":"RRS", "Status": "Success",
                      "Status Code": "200", "Return Value":result},indent=2))

   
