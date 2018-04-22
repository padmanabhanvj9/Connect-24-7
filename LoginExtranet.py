import json
from sqlwrapper import gensql,dbfetch

def login(request):

    d,e = request.json,{}
    a = { k : v for k,v in d.items() if k != 'user_password'}
    e = { k : v for k,v in d.items() if k == 'user_password'}
    print(a)
    print(e,e['user_password'])
    data = gensql('select','extranet_signup','user_password',a)
    data = json.loads(data)
    data = data[0]
    print(data,type(data))
    if data['user_password'] == e['user_password']:
       print("password matched") 
       return(json.dumps({"ServiceStatus":"Success","ServiceMessage":"Success"},indent=2))
    
    return(json.dumps({"ServiceStatus":"Failure","ServiceMessage":"Failure"},indent=2))

