from sqlwrapper import gensql
import json
import datetime
#from datetime import datetime
def cancelcurrentbooking(request):
    no = request.args["conf_no"]
    d = {}
    d['customer_confirmation_number'] = no
    res = (gensql('select','ivr_room_customer_booked','*',d))
    if len(res) == 2 :
        return(json.dumps({"Return":"Invalid Confirmation Number","Return Code":"ICN","Status": "Success",
                      "Status Code": "200"},indent=2))  
    result  = json.loads(res)
    data = result[0]
    date = (data['customer_arrival_date'])
    arrival_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    #print(arrival_date,type(arrival_date))
    today_date = datetime.datetime.utcnow()
    #print(today_date,type(today_date))
    
    if arrival_date < today_date:
       return(json.dumps({"Return":"Can't Cancel Reservation","Return Code":"CCR","Status": "Success",
                      "Status Code": "200"},indent=2))
    s = {}
    s['customer_booked_status'] = "canceled" 
    print(gensql('update','ivr_room_customer_booked',s,d)) 
    return(json.dumps({"Return":"Reservation Canceled Successfully","Return Code":"RCS","Status": "Success",
                      "Status Code": "200"},indent=2))
  
   
    
