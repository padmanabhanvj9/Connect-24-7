web: gunicorn ivr_master:app

worker: gunicorn sqlwrapper.py
worker: gunicorn QueryANI.py
worker: gunicorn FetchExistingBookings.py
worker: gunicorn FetchRoomsAvailabilityandPrice.py
worker: gunicorn UpdateCustomerLangSelected.py
worker: gunicorn FetchPromotionalMessage.py
worker: gunicorn CalculateTotalChargesAndRetrieveConfirmationNumber.py
worker: gunicorn UpdatedCustomerProfile.py
worker: gunicorn CancelCurrentbooking.py
worker: gunicorn SendSMS.py
