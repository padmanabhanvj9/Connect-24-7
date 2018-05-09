'''
This is the master file for all the Web services
related to IVR application
'''
import json
from flask import Flask,request, jsonify
from flask_cors import CORS
from QueryANITEST import queryanitest
from QueryANI import queryani
from UpdateCustomerLangSelected import updatecustomerlangselected
from FetchExistingBookings import fetchexistingbookings
from CancelCurrentbooking import cancelcurrentbooking
from FetchRoomsAvailabilityandPrice import fetchroomsavailabilityandprice
from FetchRoomsAvailabilityandPrice import fetchpromotionalmessage
from CalculateTotalChargesAndRetrieveConfirmationNumber import calculatetotalchargesandretrieveconfirmationnumber
from UpdatedCustomerProfile import updatedcustomerprofile
from SendSMS import sendsms
from SendEmailIVR import sendemailivr
##extranet
from SignupExtranet import signup
from LoginExtranet import login
from AvailableRoomCount import availableroomcount
from RoomList import roomlist
from RatesandAvailability import ratesandavailability
from InsertRatesandAvailability import insertratesandavailability
from UpdateRatesandAvailability import updateratesandavailability
from AddDiscount import adddiscount
from QueryDiscount import querydiscount
#add
from CheckDate import validationivr
from SendEmail import sendemail


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
   return "Welcome to IVR!"
@app.route('/QueryANI/test',methods=['GET'])
def QueryANITest():
   return queryanitest(request)

@app.route('/QueryANI',methods=['GET','POST'])
def QueryANIinfo():
   return queryani(request)
@app.route('/UpdateCustomerLangSelected',methods=['GET'])
def LangSelected():
   return updatecustomerlangselected(request)
@app.route('/FetchExistingBookings',methods=['GET','POST'])
def ExistingBookings():
   return fetchexistingbookings(request)
@app.route('/CancelCurrentbooking',methods=['GET'])
def Cancelbooking():
   return cancelcurrentbooking(request)
@app.route('/FetchRoomsAvailabilityandPrice',methods=['GET','POST'])
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
@app.route('/SendEmailIVR',methods=['POST'])
def Email():
   return sendemailivr(request)
##extranet
@app.route('/SignupExtranet',methods=['POST'])
def ExSignup():
   return signup(request)
@app.route('/LoginExtranet',methods=['POST'])
def ExLogin():
   return login(request)
@app.route('/AvailableRoomCount',methods=['POST'])
def ExAvailableRoomCount():
   return availableroomcount(request)
@app.route('/RoomList',methods=['POST'])
def ExRoomList():
   return roomlist(request)
@app.route('/RatesandAvailability',methods=['POST'])
def ExRatesandAvailability():
   return ratesandavailability(request)
@app.route('/InsertRatesandAvailability',methods=['POST'])
def ExInsertRatesandAvailability():
   return insertratesandavailability(request)
@app.route('/UpdateRatesandAvailability',methods=['POST'])
def ExUpdateRatesandAvailability():
   return updateratesandavailability(request)
@app.route('/AddDiscount',methods=['POST'])
def Discount():
   return adddiscount(request)
@app.route('/QueryDiscount',methods=['POST'])
def QueryDiscount():
   return querydiscount(request)
#add
@app.route('/ValidationIVR',methods=['POST'])
def CheckDate():
   return validationivr(request)
@app.route('/SendEmail',methods=['POST'])
def  sendemailmessage():
   return sendemail(request)
if __name__ == "__main__":
  app.run(debug=True)
  #app.run(host="192.168.1.10",port=5000)
   
