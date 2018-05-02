from sqlwrapper import gensql
import json
import random
import datetime
def calculatetotalchargesandretrieveconfirmationnumber(request):
    customer_name = request.json["customer_name"]
    customer_mobile = request.json["customer_mobile"]        
    customer_arrival_date = request.json["customer_arrival_date"]
    customer_depature_date = request.json["customer_depature_date"]
    customer_room_type = request.json["customer_room_type"]
    d,e,d1,d2 = {},[],{},{}
    e = ['room_count_available','room_rate','currency']
    d['room_type'] =  customer_room_type
    result = (gensql('select','ivr_room_availability_rate',e,d))
    result = json.loads(result)
    print(result)
    res = result[0]
    room_available = res['room_count_available']
    room_rate = res['room_rate']
    print(room_rate,type(room_rate))
    currency = res['currency']
    if room_available == 0 :
        return(json.dumps({"Return":"RoomType_Not_Available ","Return_Code":"RTNA","Status": "Success",
                      "Status Code": "200"},indent=2))
    arrival_date = datetime.datetime.strptime(customer_arrival_date, '%Y-%m-%d')
    depature_date = datetime.datetime.strptime(customer_depature_date, '%Y-%m-%d')
    print(arrival_date,depature_date)
    night = (depature_date - arrival_date).days
    print(night,type(night))
    Total_amt = night * room_rate
    print(Total_amt,type(Total_amt))
    conf_no = (random.randint(1000000000,9999999999))
    room_available -= 1
    d1['room_count_available'] = room_available
    d2['room_type'] = customer_room_type
    print(gensql('update','ivr_room_availability_rate',d1,d2))
    return(json.dumps({"Total_Amount":Total_amt,"currency":currency,"Confirmation_Number":conf_no},indent=2))
