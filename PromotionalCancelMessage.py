from sqlwrapper import dbget
import json
import datetime
def promotionalcancelmessage(request):
    try:
        tfn = request.json['TFN']
        b_id = json.loads(dbget("select id from ivr_dialed_number where dialed_number='"+tfn+"' "))
        print(b_id[0]['id'])
        message = json.loads(dbget("select ivr_promotional_message from ivr_promotional_cancellation_message join \
                                    ivr_hotel_list on ivr_hotel_list.id = ivr_promotional_cancellation_message.id \
                                    where ivr_promotional_cancellation_message.id='"+str(b_id[0]['id'])+"' "))
        message = message[0]['ivr_promotional_message']
        print(message)
        a = {"ServiceStatus":"Success","ServiceMessage":"Success","message":message}
        return(json.dumps(a))
    except:
        a = {"ServiceStatus":"Success","ServiceMessage":"Success"}
        return(json.dumps(a))
