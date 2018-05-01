from sqlwrapper import gensql
import json
import datetime
#from datetime import datetime
def fetchexistingbookings(request):
    today_date = datetime.datetime.utcnow().date()
    no = request.args["conf_no"]
    d = {}
    d['customer_confirmation_number'] = no
    result = (gensql('select','ivr_room_customer_booked','*',d))
    result = json.loads(result)
    result = result[0]
    print(result)
    #return(json.dumps({"Return":"Record Retrieved Successfully","Return Code":"RRS", "Status": "Success",
     #                  "Status Code": "200", "Return Value":result},indent=2))
    dict1 = {"Return":"Record Retrieved Successfully","Return Code":"RRS", "Status": "Success",
                      "Status Code": "200"}
    print(dict1,type(dict1))
    dict1.update(result)
    print(dict1)
    return(json.dumps(dict1))
   
