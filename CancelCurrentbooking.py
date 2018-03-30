from sqlwrapper import gensql
import json
import datetime

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
    date = data['customer_arrival_date']
    room_type = data['customer_room_type']
    print(room_type)
    arrival_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    today_date = datetime.datetime.utcnow()
    if arrival_date < today_date:
       return(json.dumps({"Return":"Can't Cancel Reservation","Return Code":"CCR","Status": "Success",
                      "Status Code": "200"},indent=2))
    s = {}
    s['customer_booked_status'] = "canceled"    
    print(gensql('update','ivr_room_customer_booked',s,d))

    r,s1 = {},{}
    r['room_type'] = room_type
    room_count = gensql('select','ivr_room_availability_rate','room_count_available',r)
    room_count = json.loads(room_count)
    room_count = room_count[0]
    room_count = (room_count['room_count_available'])
    print(room_count)
    room_count += 1 
    print(room_count)
    s1['room_count_available'] = room_count
    print(gensql('update','ivr_room_availability_rate',s1,r))
    return(json.dumps({"Return":"Reservation Canceled Sucessfully","Return Code":"RCS","Status": "Success",
                      "Status Code": "200"},indent=2))
  
   
    
