import json
import datetime
import logging
import psycopg2
from flask import Flask,request
app = Flask(__name__)

def newtimeslot(data):
    
    d,f = {},{}
    morning,afternoon,evening,slot = [],[],[],[]
    for i  in data:
        for loc in i["morning"]:
            loc = loc['time']
            a = loc[0:5]
            b = loc[6:11]
            a = datetime.datetime.strptime(a, '%H:%M')
            b = datetime.datetime.strptime(b, '%H:%M')
            a = a.strftime("%I:%M %p")
            b = b.strftime("%I:%M %p")
            x = a+' - '+b
            d['time']= x
            morning.append(d.copy())
        for loc in i["afternoon"]:
                loc = loc['time']
                a = loc[0:5]
                b = loc[6:11]
                a = datetime.datetime.strptime(a, '%H:%M')
                b = datetime.datetime.strptime(b, '%H:%M')
                a = a.strftime("%I:%M %p")
                b = b.strftime("%I:%M %p")
                x = a+' - '+b
                d['time']= x
                afternoon.append(d.copy())
        for loc in i["evening"]:
                    loc = loc['time']
                    a = loc[0:5]
                    b = loc[6:11]
                    a = datetime.datetime.strptime(a, '%H:%M')
                    b = datetime.datetime.strptime(b, '%H:%M')
                    a = a.strftime("%I:%M %p")
                    b = b.strftime("%I:%M %p")
                    x = a+' - '+b
                    d['time']= x
                    evening.append(d.copy())            
                
    f['morning'] = morning
    f['afternoon'] = afternoon
    f['evening'] = evening
    slot.append(f)
    return(slot)

def appointmentschedule():

    if request.args.get('business_id'):
        business_id = request.args['business_id']
    if request.args.get('appointment_date'):
        appointment_date = request.args['appointment_date']
    current_time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    current_time = current_time.strftime('%H:%M')
    today_date = datetime.datetime.utcnow().date().strftime ("%Y-%m-%d")
    if today_date != appointment_date:
        current_time = '00:00'  
    try:		
     con = psycopg2.connect(user='quywvejawxhnse',password='065fe8ac62d76caa061d1e517b2f0107b5776f767037c2e29cad16c259a771cf',host='ec2-176-34-113-15.eu-west-1.compute.amazonaws.com',port='5432',database='d3opaj0jiqsm0h')
     cur = con.cursor()
    except psycopg2.Error :
       return (json.dumps({'Status': 'Failure','Message':'DB connection Error'}, sort_keys=True, indent=4)) 
        
    sql = ("select business_hour_start,business_hour_end,business_break_time_start,business_break_time_end,business_avg_wait_time_min from  business_primary where business_id = "+business_id+"")
    cur.execute(sql)
    
    row = cur.fetchone()
    start_time = row[0]
    end_time = row[1]
    slot_time = row[4]
    break_time_s= row[2]
    break_time_e= row[3]
    afternoon= '12:00'
    evening= '18:00'
    breaks,hours,test=[],[],[]
    booked_time = []
    psql = ("select customer_appointment_time from  customer_details where business_id="+business_id+" and customer_appointment_date= '"+appointment_date+"' and customer_current_status in ('booked','checkedout')")
    cur.execute(psql)
    for line in cur.fetchall():
        for field in line:
           booked_time.append(field)       
    time = datetime.datetime.strptime(start_time, '%H:%M')
    end = datetime.datetime.strptime(end_time, '%H:%M')
    break_st = datetime.datetime.strptime(break_time_s, '%H:%M')
    break_ed = datetime.datetime.strptime(break_time_e, '%H:%M')
    af = datetime.datetime.strptime(afternoon, '%H:%M')
    ev = datetime.datetime.strptime(evening, '%H:%M')
    test= [break_st.strftime("%H:%M"),break_ed.strftime("%H:%M")]
    t = '-'.join(test[0:2])
    while break_st <= break_ed:
        breaks.append(break_st.strftime("%H:%M"))
        break_st += datetime.timedelta(minutes=slot_time)
    while time <= end:
         hours.append(time.strftime("%H:%M"))
         time += datetime.timedelta(minutes=slot_time)
    x= len(breaks)
    for i in hours[:]:
         if i in breaks[1:x-1]:
             hours.remove(i)
    (list1,list2,list3,result)= ([],[],[],[])
    d,f = {},{}
    indexval = 0
    for i in range(len(hours)-1):
        a = (hours[indexval:indexval+2])
        if afternoon > a[0]:
           x = '-'.join(hours[indexval:indexval+2])
           d['time']=x
           list1.append(d.copy())
           if t == x or x < current_time:
              list1.remove(list1[-1])
           elif x in booked_time:
              list1.remove(list1[-1]) 
        elif evening > a[0]:
           x = '-'.join(hours[indexval:indexval+2])
           d['time']=x
           list2.append(d.copy())
           if t == x or x < current_time:
              list2.remove(list2[-1])
           elif x in booked_time:
              list2.remove(list2[-1])   
        else:
           x = '-'.join(hours[indexval:indexval+2])
           d['time']=x
           list3.append(d.copy())
           if t == x or x < current_time:
              list3.remove(list3[-1])
           elif x in booked_time:
              list3.remove(list3[-1])   
        indexval += 1
    f['morning'] = list1
    f['afternoon'] = list2
    f['evening'] = list3
    result.append(f)
    cur.close()
    con.close()
    
    return(json.dumps(newtimeslot(result),indent =2))
 

