import json
from sqlwrapper import gensql,dbfetch,dbget

def roomlist(request):
    business_id = request.json['business_id']
    res = json.loads(dbget("select room_name,room_code,room_type,standard_rate,totel_room,facilitie1,facilitie2,facilitie3 from extranet_room_list where business_id='"+business_id+"' "))
    return(json.dumps({"ServiceStatus":"Success","ServiceMessage":"Success","Room_List":res},indent=2))

