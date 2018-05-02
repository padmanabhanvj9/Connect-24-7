from sqlwrapper import gensql
import urllib.request
import time
import json

def sendsms(request):
     name = request.json['name']
     phone = request.json['phone']
     message = request.json['message']
     conf_no = request.json['conf_no']
     hotel_name = request.json['hotel_name']
     arrival = request.json['arrival']
     depature = request.json['depature']
     room_type = request.json['room_type']
     all_message = ("hi, "+name+". "+message+".  Confirmation Number is "+conf_no+", Arrival Date: "+arrival+", Depature Date:"+depature+", Room Type:"+room_type+", by    "+hotel_name+"")
     url = "https://control.msg91.com/api/sendhttp.php?authkey=195833ANU0xiap5a708d1f&mobiles="+phone+"&message="+all_message+"&sender=Infoit&route=4&country=91"
     req = urllib.request.Request(url)
     with urllib.request.urlopen(req) as response:
         the_page = response.read()
         the_page = the_page[1:]
         print(the_page)
         the_page = str(the_page)
     return(json.dumps({"Return":"SMS Sent Successfully","Return_Code":"SSS","Status": "Success","Status_Code": "200","Key":the_page},indent =2))


      

    
