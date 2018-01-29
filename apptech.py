'''

This is the master file for all the Web services
related to Doctor Appt application

'''

from flask import Flask,request, jsonify
from Update import updatecustomerinfo
from UpdateCustomerStatus import updatecustomerstatus
from QueryAppointmentList import Query
from QueryBusinessPrimaryData import QueryBusinessPrimary
from UpdateCustomerFeedback import updatefeedback
from GetCustomerDetails import CustomerDetails
from GetCustomerDetailsAll import getcustomerdetailsall
from QueryBusinessDetailsData import BusinessDetails
from GetBookedTokenNum import bookedtokennumber
from GetAppointmentSchedule  import appointmentschedule
from GetLiveFeed import getlivefeed
from TokenNumberGeneration import tokengeneration
from InsertBusinessDetailsData import insertbusinessdetails
from QueryBusinessPrimaryAll import QueryBusinessPrimaryall
from AverageWaitTime import avgwaittime
from GetCustomerBusinessDetails import getcustomerbusinessdetails
from InsertBusinessLoginData import insertbusinesslogindata
from QueryBusinessLoginData import QueryBusinessLoginData
from AppointmentChatbots import test
from weather import webhook
from UpdateChatbots import updatecustomerinfochatbots
from UpdateBusinessPrimaryData import updatebusinessprimary
from SendEmail import sendemail
import json

app = Flask(__name__)

@app.route("/")
def hello():
   return "Hello World!"
@app.route("/user/<data>")
def helloName(data):
   return data

@app.route('/UpdateCustomerInfo',methods=['POST'])
def updateinfo():
   return updatecustomerinfo(request)

@app.route('/UpdateCustomerStatus',methods=['POST'])
def updatestatus():
   return updatecustomerstatus(request)  
     
@app.route('/QueryAppointmentList',methods=['GET'])
def Queryappointment():
   return Query()
   
@app.route('/QueryBusinessPrimaryData',methods=['GET'])
def Business():
   return QueryBusinessPrimary()
   
@app.route('/UpdateCustomerFeedback',methods=['POST'])
def Customerfeedback():
   return updatefeedback(request)
    
@app.route('/GetCustomerDetails',methods=['GET'])
def getcustomerdetails():
   return CustomerDetails()

@app.route('/GetCustomerDetailsAll',methods=['GET'])
def customerdetailsall():
    return getcustomerdetailsall()
@app.route('/QueryBusinessDetailsData',methods=['GET'])
def QueryBusiness():
   return BusinessDetails()
@app.route('/GetBookedTokenNum',methods=['GET'])
def bookednum():
   return bookedtokennumber()
@app.route('/GetAppointmentSchedule',methods=['GET'])
def schedule():
   return appointmentschedule()
@app.route('/GetLiveFeed',methods=['GET'])
def livefeed():
   return getlivefeed()
@app.route('/TokenNumberGeneration',methods=['POST'])
def Tokengeneration():
   return tokengeneration(request)   
@app.route('/InsertBusinessDetailsData',methods=['POST'])
def insertbusinessdetailsdata():
   return insertbusinessdetails(request)

@app.route('/QueryBusinessPrimaryAll',methods=['GET'])
def businessprimaryall():
   return QueryBusinessPrimaryall()
@app.route('/AverageWaitTime',methods=['GET'])
def waittimecal():
   return avgwaittime()
@app.route('/GetCustomerBusinessDetails',methods=['GET'])
def GetCustomerBusiness():
   return getcustomerbusinessdetails()
@app.route('/InsertBusinessLoginData',methods=['POST'])
def businesslogin():
   return insertbusinesslogindata(request)
@app.route('/QueryBusinessLoginData',methods=['GET'])
def querylogin():
   return QueryBusinessLoginData()
@app.route('/AppointmentChatbots',methods=['POST'])
def CHATBOT():
   return test(request)
@app.route('/weather',methods=['POST'])
def weatehr():
   return webhook(request)
@app.route('/UpdateBusinessPrimaryData',methods=['POST'])
def updateprimarydata():
   return updatebusinessprimary(request)
   
# This is for the chatbot app only - token generation
@app.route('/update',methods=['POST'])
def GetTokenNumber():
   return updatecustomerinfochatbots(request)
@app.route('/sendemail',methods=['POST'])
def email():
   return sendemail(request)

   
@app.errorhandler(404)
def unhandled_exception(e):
   return(e)
@app.errorhandler(500)
def unhandled_exception(e):
 return(e)


if __name__ == "__main__":
    app.run(debug=True)
  #app.run(host="192.168.1.5",port="5000")
