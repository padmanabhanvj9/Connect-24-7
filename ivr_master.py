'''
This is the master file for all the Web services
related to IVR application
'''
import json
from flask import Flask,request, jsonify
from QueryANI import queryani
from UpdateCustomerLangSelected import updatecustomerlangselected
from FetchExistingBookings import fetchexistingbookings
from CancelCurrentbooking import cancelcurrentbooking
from FetchRoomsAvailabilityandPrice import fetchroomsavailabilityandprice
from FetchRoomsAvailabilityandPrice import fetchpromotionalmessage
from CalculateTotalChargesAndRetrieveConfirmationNumber import calculatetotalchargesandretrieveconfirmationnumber
from UpdatedCustomerProfile import updatedcustomerprofile
from SendSMS import sendsms

app = Flask(__name__)

@app.route("/ivr")
def hello():
   return "Hello IVR!"
@app.route('/QueryANI',methods=['GET'])
def QueryANIinfo():
   return queryani(request)
@app.route('/UpdateCustomerLangSelected',methods=['GET'])
def LangSelected():
   return updatecustomerlangselected(request)
@app.route('/FetchExistingBookings',methods=['GET'])
def ExistingBookings():
   return fetchexistingbookings(request)
@app.route('/CancelCurrentbooking',methods=['GET'])
def Cancelbooking():
   return cancelcurrentbooking(request)
@app.route('/FetchRoomsAvailabilityandPrice',methods=['GET'])
def FetchRooms():
   return fetchroomsavailabilityandprice(request)
@app.route('/FetchPromotionalMessage',methods=['GET'])
def FetchPromotionalMessage():
   return fetchpromotionalmessage(request)
@app.route('/CalculateTotalChargesAndRetrieveConfirmationNumber',methods=['POST'])
def CalculateTotalCharges():
   return calculatetotalchargesandretrieveconfirmationnumber(request)
@app.route('/UpdatedCustomerProfile',methods=['POST'])
def UpdatedProfile():
   return updatedcustomerprofile(request)
@app.route('/SendSMS',methods=['POST'])
def SMS():
   return sendsms(request)

if __name__ == "__main__":
  app.run(debug=True)
  #app.run(host="192.168.1.6",port=5000)
   

   
