import json
import random
from sqlwrapper import gensql

def signup(request):
    d = request.json
    conf_no = (random.randint(1000000000,9999999999))
    d['business_id'] = conf_no
    gensql('insert','extranet_signup',d)
    return(json.dumps({"business_id":conf_no,"ServiceStatus":"Success","ServiceMessage":"Success"},indent=2))
    

