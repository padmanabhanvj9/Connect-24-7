from sqlwrapper import dbget
import json
def fetchroomsavailabilityandprice(request):
    try:
        result = json.loads(dbget('select * from ivr_room_availability_rate'))
        #print(result,type(result))
        #print(result[0])
        print(len(result))
        f_res = {}
        for res in result:
            print(res)
            print(res['room_count_available'])
            print(result.index(res),type(result.index(res)))
            f_res["room_count_available"+""+str(result.index(res))+""] = res['room_count_available']
            f_res["room_rate"+""+str(result.index(res))+""] = res['room_rate']
            f_res["currency"+""+str(result.index(res))+""] = res['currency']
            f_res["room_type"+""+str(result.index(res))+""] = res['room_type']
        #return(json.dumps({"Return":"Record Retrieved Successfully","Return Code":"RRS", "Status": "Success",
        #                  "Status Code": "200", "Return Value":result},indent=2))
        f_res["count"] = len(result)
        print(f_res)
        #dict1 = [{"Return":"Record Retrieved Successfully","Return_Code":"RRS", "Status": "Success",
                          #"Status_Code": "200"}]
        #print(dict1,type(dict1))
        #result = result+dict1
        #print(result,type(result))
        return(json.dumps(f_res))
    except:
        return(json.dumps({"Status": "Failure"},indent=2))
    
def fetchpromotionalmessage(request):
    result = dbget('select * from ivr_promotional_cancellation_message')
    result = json.loads(result)
    result = result[0]
    #return(json.dumps({"Return":"Record Retrieved Successfully","Return Code":"RRS", "Status": "Success",
     #                 "Status Code": "200", "Return Value":result},indent=2))
    dict1 = {"Return":"Record Retrieved Successfully","Return_Code":"RRS", "Status": "Success",
                      "Status_Code": "200"}
    print(dict1,type(dict1))
    dict1.update(result)
    print(dict1)
    return(json.dumps(dict1))
   
