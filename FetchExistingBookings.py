from sqlwrapper import gensql,dbget
import json
import datetime
#from datetime import datetime
def fetchexistingbookings(request):
    today_date = datetime.datetime.utcnow().date()
    #no = request.args["conf_no"]
    no = request.json['mobile']
    d = {}
    d['customer_mobile'] = no
    result = (dbget("select * from ivr_room_customer_booked  where customer_mobile='"+no+"' order by customer_arrival_date limit 1"))
    result = json.loads(result)
    result = result[0]
    print(result)
    #return(json.dumps({"Return":"Record Retrieved Successfully","Return Code":"RRS", "Status": "Success",
     #                  "Status Code": "200", "Return Value":result},indent=2))
    dict1 = {"Return":"Record Retrieved Successfully","Return_Code":"RRS", "Status": "Success",
                      "Status_Code": "200"}
    print(dict1,type(dict1))
    dict1.update(result)
    print(dict1)
    return(json.dumps(dict1))
   

   
