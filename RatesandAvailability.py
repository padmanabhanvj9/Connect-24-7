import json
import datetime
from sqlwrapper import gensql,dbfetch,dbget

def ratesandavailability(request):
    #req = request.json
    business_id = request.json['business_id']
    from_date = request.json['from_date']
    to_date = request.json['to_date']
    room_type = request.json['room_type']
    from_date = datetime.datetime.strptime(from_date,'%Y-%m-%d').date()
    print(from_date,type(from_date))
    to_date = datetime.datetime.strptime(to_date,'%Y-%m-%d').date()
    print(to_date)
    date_list = []
    while from_date <= to_date:
        date_list.append(from_date)
        from_date += datetime.timedelta(days=1)
        #print(from_date,type(from_date))
    #print(date_list,type(date_list))
    #month = date_list[0].strftime('%B')
    #print(month,type(month))
    #print(date_list[0].strftime("%A"))
    #print(date_list[0].strftime("%d"))
    #new_list = date_list.copy()
    #print(new_list)
    #new_list = str(new_list)
    #new_list = new_list[1:-1]
    #print(new_list,type(new_list))
    day,days,a = [],{},{"business_id":business_id}
    #res = dbget("select room_rate_declared,room_available from extranet_room_available where business_id = '"+business_id+"' and rm_date in ("+new_list+")")
    #print(res)    
    for i in date_list:
        a['rm_date'] = i
        result = gensql('select','extranet_room_available','room_rate_declared,room_available',a)
        #print(result,type(result))
        result = json.loads(result)
        #print(result,type(result))
        result = result[0]
        r_a = result["room_available"]
        r_r = result["room_rate_declared"]
        print(r_a,r_r)
        d = {"Month": i.strftime('%B'),"Date":i.strftime('%d'),"Price":r_r,"Available_Room_Count":r_a,
             "Room_Status":"Yellow","Day":i.strftime("%A")}
        day.append(d)
        days['Countdates'] = day 
    print(days)    
    return(json.dumps({"ServiceStatus":"Success","ServiceMessage":"Success","resut":days},indent=2))


