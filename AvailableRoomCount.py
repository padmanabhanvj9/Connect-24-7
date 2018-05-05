import json
from sqlwrapper import gensql,dbfetch,dbget

def availableroomcount(request):
    d = request.json
    print(d)
    print(d['business_id'])
    res = json.loads(dbget("select available_count,room_name,room_type from extranet_availableroom join extranet_room_list on extranet_room_list.id = extranet_availableroom.id where room_date = '"+d['available_date']+"'"))
    print(res,type(res))
    return(json.dumps({"ServiceStatus":"Success","ServiceMessage":"Success","Available_Rooms":res},indent=2))
