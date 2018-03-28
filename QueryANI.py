import json
from flask import Flask,request,jsonify
from sqlwrapper import gensql

def queryani(request):
    ani = request.args["ani"]
    d,e = {},{}
    d['customer_ani'] = ani
    e['customer_mobile'] = ani
    tab1 = (gensql('select','ivr_customer_profile','customer_language_pref',d))
    print(tab1)
    tab2 = (gensql('select',' ivr_room_customer_booked','*',e))
    print(tab2)
    #tab = tab1['customer_language_pref']
    #print(tab1)
    tab = tab1+tab2
    return(tab)

    
