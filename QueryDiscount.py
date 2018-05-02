import json
import datetime
from sqlwrapper import gensql,dbfetch,dbget

def querydiscount(request):
    res = request.json
    d = { k : v for k,v in res.items() if k not in ('room_date')} 
    res_id = json.loads(gensql('select','extranet_room_list','id',d))
    res_id = str(res_id[0]['id'])
    print(res_id)
    result = json.loads(dbget("select room_date,discount_type,discount_rate,discount_in,discount_on  from extranet_discount where id in ('"+res_id+"') and room_date = '"+res['room_date']+"'"))
    print(result,type(result))
    return(json.dumps({"ServiceStatus":"Success","ServiceMessage":"Success","Result":result},indent=2))
