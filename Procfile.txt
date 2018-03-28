web: gunicorn ivr_master:app

worker: gunicorn sqlwrapper.py
worker: gunicorn QueryANI.py
worker: gunicorn FetchExistingBookings.py
worker: gunicorn FetchRoomsAvailabilityandPrice.py
worker: gunicorn UpdateCustomerLangSelected.py