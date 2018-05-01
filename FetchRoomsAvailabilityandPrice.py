from sqlwrapper import dbget
import json
def fetchroomsavailabilityandprice(request):
    result = dbget('select * from ivr_room_availability_rate')
    print(result,type(result))
    result = json.loads(result)
    #result = result[0]
    print(result,type(result))
    #return(json.dumps({"Return":"Record Retrieved Successfully","Return Code":"RRS", "Status": "Success",
    #                  "Status Code": "200", "Return Value":result},indent=2))

    dict1 = [{"Return":"Record Retrieved Successfully","Return Code":"RRS", "Status": "Success",
                      "Status Code": "200"}]
    print(dict1,type(dict1))
    result = result+dict1
    print(result,type(result))
    #dict1.update(result)
    #print(dict1)
    return(json.dumps(result))
    
def fetchpromotionalmessage(request):
    result = dbget('select * from ivr_promotional_cancellation_message')
    result = json.loads(result)
    result = result[0]
    #return(json.dumps({"Return":"Record Retrieved Successfully","Return Code":"RRS", "Status": "Success",
     #                 "Status Code": "200", "Return Value":result},indent=2))
    dict1 = {"Return":"Record Retrieved Successfully","Return Code":"RRS", "Status": "Success",
                      "Status Code": "200"}
    print(dict1,type(dict1))
    dict1.update(result)
    print(dict1)
    return(json.dumps(dict1))
   
