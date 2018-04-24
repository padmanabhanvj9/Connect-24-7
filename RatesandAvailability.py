import json
import datetime
from sqlwrapper import gensql,dbfetch,dbget

def ratesandavailability(request):
    req = request.json
    for k,v in req.items():
        if k == 'date_range':
           from_date = datetime.datetime.now().date()
           to_date = from_date +datetime.timedelta(days=v)
           print(from_date,to_date)
        if k == 'from_date':
           from_date = request.json['from_date']
           to_date = request.json['to_date']
           from_date = datetime.datetime.strptime(from_date,'%Y-%m-%d').date()
           print(from_date,type(from_date))
           to_date = datetime.datetime.strptime(to_date,'%Y-%m-%d').date()
           print(to_date)
           
    business_id = request.json['business_id']
    room_type = request.json['room_type']
    date_list = []
    str_date = ''
    while from_date <= to_date:
        if len(str_date) != 0:
           str_date += ','+"'"+str(from_date)+"'"
        else:   
           str_date += "'"+str(from_date)+"'"   
        date_list.append(from_date)
        from_date += datetime.timedelta(days=1)
    print(str_date)    
    day,days,a = [],{},{"business_id":business_id}
    res = dbget("select room_rate_declared,room_available from extranet_room_available where business_id = '"+business_id+"' and rm_date in ("+str_date+")")
    print(res)
    res = json.loads(res)
    n = 0 
    for i in date_list:   
           a['rm_date'] = i
           d = {"Month": i.strftime('%B'),"Date":i.strftime('%d'),"Price":res[n]["room_rate_declared"],"Available_Room_Count":res[n]["room_available"],
             "Room_Status":"Yellow","Day":i.strftime("%A")}
           day.append(d)
           days['Countdates'] = day
           n += 1
    print(days)    
    return(json.dumps({"ServiceStatus":"Success","ServiceMessage":"Success","resut":days},indent=2))


