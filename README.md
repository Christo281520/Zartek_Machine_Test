# \# Ride Sharing API (Zartek Machine Test)

# \##  Description

# This project is a backend Ride Sharing API built using Django and Django REST Framework.

# \## 🔗 Base URL

# http://127.0.0.1:8000/

# see the page

# \## 👤 User API

# \### Register User

# POST /api/register/

# Request:

# {

# &#x20; "username": "test",

# &#x20; "password": "1234"

# }

# \---

# \## 🚗 Ride API

# \### Create Ride

# POST /api/rides/

# see the ride details and adding the rides

# Request:

# {

# &#x20; "rider": 1,

# &#x20; "pickup\_location": "Kochi",

# &#x20; "dropoff\_location": "Ernakulam"

# }

# \---

# \### Get All Rides

# GET /api/rides/

# \---

# \### Get Single Ride

# GET /api/rides/{id}/

#  for see single ride instances 

# \---

# \### Update Ride Status

# POST /api/rides/{id}/update_status/

# in there POST /api/rides/{id}/update_status/ also click extra action in there update_status in there so it will go there and we can 
   update single rider status

# Request:

# {

# &#x20; "status": "started"

# }

# \---

# \## ⭐ Bonus Feature

# \### Accept Ride

# POST /api/rides/{id}/accept_ride/

# This allows a driver to accept a ride and automatically updates the ride status to "started".

# \---

# \## 📌 Status Values

# \- requested

# \- started

# \- completed

# \- cancelled

# \---

# \## ⚙️ Tech Stack

# \- Python

# \- Django

# \- Django REST Framework

# \---

# \## 📝 Notes

# \- Use browser (DRF UI) to test APIs

# \- Admin panel available at /admin/

# \- Also try to add Login but only POST not to GET if you want then install thunder client in the estensions in the VScode
