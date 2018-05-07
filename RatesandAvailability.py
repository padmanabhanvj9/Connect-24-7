import json
import datetime
from sqlwrapper import gensql,dbfetch,dbget

def ratesandavailability(request):
    req = request.json
    for k,v in req.items():
        if k == 'date_range':
           from_date = datetime.datetime.now().date()
           to_date = from_date +datetime.timedelta(days=v)
           
        if k == 'from_date':
           from_date = request.json['from_date']
           to_date = request.json['to_date']
           from_date = datetime.datetime.strptime(from_date,'%Y-%m-%d').date()
           to_date = datetime.datetime.strptime(to_date,'%Y-%m-%d').date()
               
    business_id = request.json['business_id']
    room_type = request.json['room_type']
    #room_name = request.json['room_name']
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
    res = json.loads(dbget("select room_date,available_count,room_rate from extranet_availableroom where room_date in ("+str_date+") and id in (select id from extranet_room_list where business_id='"+business_id+"' and room_type='"+room_type+"')"))
    #print(res,type(res),len(res))
    length = len(res)
    date = []
    for data in res:
        print(data['room_date'],type(data['room_date']))
        date.append(datetime.datetime.strptime(data['room_date'],'%Y-%m-%d').date())
    #print(date,type(list))    
    for i in date_list:
        #print(i,type(i))
        if i in date:
              n = date.index(i)
              #print(n)
              d = {"Month": i.strftime('%B'),"Date":i.strftime('%d'),"Day":i.strftime("%A")[0:3],
                "Price":res[n]["room_rate"],
                "Available_Room_Count":res[n]["available_count"],
                "Room_Status":"Declared","date":str(i)}
              #print(d)
        else:
             d = {"Month": i.strftime('%B'),"Date":i.strftime('%d'),"Day":i.strftime("%A")[0:3],
                "Price":"",
                "Available_Room_Count":"",
                "Room_Status":"NotDeclared","date":str(i)}
             #print(d) 
        day.append(d)
    return(json.dumps({"ServiceStatus":"Success","ServiceMessage":"Success","Result":day},indent=2))
    


