from sqlwrapper import gensql
import json
import datetime
#from datetime import datetime
def fetchexistingbookings(request):
    today_date = datetime.datetime.utcnow().date()
    no = request.args["conf_no"]
    d = {}
    d['customer_confirmation_number'] = no
    result = (gensql('select','ivr_room_customer_booked','*',d))    
    return(result)
