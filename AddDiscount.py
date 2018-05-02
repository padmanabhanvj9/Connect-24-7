import json
import datetime
from sqlwrapper import gensql,dbfetch,dbget

def adddiscount(request):
    res = request.json
    print(res)
    e = { k : v for k,v in res.items() if k in ('business_id','room_type','room_name')}
    d = { k : v for k,v in res.items() if k not in ('business_id','room_type','room_name')}
    
    id_data = json.loads(gensql('select','extranet_room_list','id',e))
    print(id_data,type(id_data))
    str_id = ''
    for i in id_data:
       sql = json.loads(dbget("select count(*) from extranet_discount where id in ("+str(i['id'])+") and room_date='"+d['room_date']+"' "))
       print(sql[0]['count'])
       if sql[0]['count'] == 0:
          try:
            d['id'] = i['id']   
            print(gensql('insert','extranet_discount',d))
            print("inserted")
            #return(json.dumps({"ServiceStatus":"Success","ServiceMessage":"Record Inserted"},indent=2))    
          except:
            return(json.dumps({"ServiceStatus":"Failure","ServiceMessage":"Failure"},indent=2))
       else:
           print("record already inserted")
    return(json.dumps({"ServiceStatus":"Success","ServiceMessage":"Record Inserted"},indent=2))   
