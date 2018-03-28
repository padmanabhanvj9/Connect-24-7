from sqlwrapper import dbget
import json
def fetchroomsavailabilityandprice(request):
    result = dbget('select * from ivr_room_availability_rate')
    return(result) 
def fetchpromotionalmessage(request):
    result = dbget('select * from ivr_promotional_cancellation_message')
    return(result) 
