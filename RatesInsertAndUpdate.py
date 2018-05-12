import json
import datetime
from sqlwrapper import gensql,dbget,dbput
def ratesinsertandupdate(request):
    d = request.json
    e = { k : v for k,v in d.items() if k in ('business_id','room_type')}
    f = { k : v for k,v in d.items() if k in ('rooms')}
    res = json.loads(gensql('select','extranet_room_list','id',e))
    print(res[0]['id'],type(res[0]['id']))
    f = f['rooms']
    for i in f:
      print(i)  
      sql = json.loads(dbget("select count(*) from extranet_availableroom where id = '"+str(res[0]['id'])+"'\
                             and room_date = '"+i['date']+"' "))
      print(sql[0]['count'])
      if sql[0]['count'] == 0:
         dbput("INSERT INTO public.extranet_availableroom(\
	        id, room_date, available_count, room_rate)\
	        VALUES ("+str(res[0]['id'])+", '"+i['date']+"', "+str(i['Available_Room_Count'])+", "+str(i['Price'])+")")
      else:
         dbput("UPDATE public.extranet_availableroom\
	        set available_count="+str(i['Available_Room_Count'])+", room_rate="+str(i['Price'])+"\
	        WHERE  id="+str(res[0]['id'])+" and room_date='"+i['date']+"'") 
           
         print(i['date'])    
    return(json.dumps({"ServiceStatus":"Success","ServiceMessage":"Success"},indent=2))
