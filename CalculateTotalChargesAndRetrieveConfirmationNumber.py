from sqlwrapper import gensql
import json
import random
import datetime
def calculatetotalchargesandretrieveconfirmationnumber(request):
    a = request.json
    l = { k : v for k,v in a.items() if k in ('customer_mobile','customer_room_type')}
    if request.args.get('business_id'): 
       customer_name = request.json["customer_name"]
    else:
       customer_name  = "Null"
    l['customer_name'] = customer_name   
    customer_mobile = request.json["customer_mobile"]        
    customer_arrival_date = request.json["customer_arrival_date"]
    customer_depature_date = request.json["customer_depature_date"]
    customer_room_type = request.json["customer_room_type"]
    d,e,d1,d2 = {},[],{},{}
    print(customer_arrival_date,customer_depature_date)
    today_date = datetime.datetime.utcnow().date()
    year = str(today_date.year)
    if int(customer_arrival_date[0:2]) == today_date.month :
        if int(customer_arrival_date[2:]) < today_date.day :
           year = str(today_date.year+1)
           print("year",year,type(year))
    elif int(customer_arrival_date[0:2]) < today_date.month :
        year = str(today_date.year+1)
    customer_arrival_date = year+'-'+customer_arrival_date[0:2]+'-'+customer_arrival_date[2:]
    l['customer_arrival_date'] = customer_arrival_date
    if int(customer_depature_date[0:2]) == today_date.month :
        if int(customer_depature_date[2:]) < today_date.day :
           year = str(today_date.year+1)
           print("year",year,type(year))
    elif int(customer_depature_date[0:2]) < today_date.month :
        year = str(today_date.year+1)
    customer_depature_date = year+'-'+customer_depature_date[0:2]+'-'+customer_depature_date[2:]
    l['customer_depature_date'] = customer_depature_date
    print(customer_arrival_date,customer_depature_date)    
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
        return(json.dumps({"Return":"RoomType Not Available ","Return_Code":"RTNA","Status": "Success",
                      "Status_Code": "200"},indent=2))
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
    print(gensql('insert','ivr_room_customer_booked',l))    
    return(json.dumps({"Total_Amount":Total_amt,"currency":currency,"Confirmation_Number":conf_no},indent=2))
