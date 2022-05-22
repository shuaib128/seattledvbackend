from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser

# Create your views here.
# Square API Config
from square.client import Client
client = Client(
  access_token="EAAAEBqKkfiy_koFoOk4qOL6Vhra7G9EYqb-3H-EWONsIRJqIV-r4moRTp0Htqav",
  environment="production"
)

#Get all services from square
class ServicesView(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def post(self, request, format=None):
        # Get catalogs from square
        catalog = None
        result_catalog = client.catalog.search_catalog_items(
            body = {
                    "product_types": [
                    "APPOINTMENTS_SERVICE"
                ]
            }
        )

        if result_catalog.is_success():
            catalog = result_catalog.body
        elif result_catalog.is_error():
            catalog = result_catalog.errors

        response = Response()
        response.data = {
            'catalog': catalog,
        }
        return response



# User create or retrive view
class UserView(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def post(self, request, format=None):
        firstname = request.data["FirstName"]
        lastname = request.data["LastName"]
        email = request.data["email"]
        number = request.data["PhoneNumber"]
        adress = request.data["Adress"]
        userstatus = None
        userID = None
        responce = None

        result = client.customers.search_customers(
        body = {
            "query": {
                "filter": {
                        "email_address": {
                            "exact": email
                        }
                    }
                }
            }
        )


        if result.is_success() and len(result.body) != 0:
            userstatus = "exists"
            userID = result.body["customers"][0]["id"]
            responce = result.body
        elif result.is_error() or len(result.body) == 0:
            result = client.customers.create_customer(
            body = {
                    "given_name": firstname,
                    "family_name": lastname,
                    "email_address": email,
                    "address": {},
                    "phone_number": number
                }
            )
            if result.is_success():
                responce = result.body
                userstatus = "exists"
                userID = result.body["customer"]['id']
            elif result.is_error():
                responce = result.body
                userstatus = "notexists"

        response = Response()
        response.data = {
            'userstatus': userstatus,
            "userid": userID,
            "responce": responce
        }
        return response



# Booking View
class BookingView(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def post(self, request, format=None):
        # Client Message
        booked = None
        data = request.data["data"]
        booking_id = request.data["data"]["service"]["item_data"]["variations"][0]["id"]
        booking_version = request.data["data"]["service"]["version"]

        # Appoentment information
        # appertment_condetion = "Apartment available for work" if data[
        #     "Appertment"] == 'true' else "Apartment not available for work"
        # mold_ondetion = "Car has mold" if data["Mold"] == 'true' else "Car has no mold"
        # hair_condetion = "Car has pet hair" if data["PetHair"] == 'true' else "Car has no pet hair"
        # car = data["Car"]
        # car_condetion = "Car condetion: Bad" if data["Bad"] == 'true' else "Car condetion: Good" if data[
        #     "Good"] == 'true' else "Car condetion: Excellent"
        # seller_note = f"\n{appertment_condetion}\n {mold_ondetion}\n {hair_condetion}\n {car}\n {car_condetion}"

        # Booking data
        result = client.bookings.create_booking(
        body={
                "booking": {
                "start_at": data["selectedDate"],
                "location_id": "LBHV0DX52EPXJ",
                "customer_id": data["userID"],
                "customer_note": "data[user_message]",
                "seller_note": "seller_note",
                "appointment_segments": [
                        {
                        "duration_minutes": 45,
                        "service_variation_id": booking_id,
                        "team_member_id": "TMNiWb9pJncjDMGf",
                        "service_variation_version": booking_version
                        }
                    ]
                }
            }
        )


        if result.is_success():
            booked = "booked"
        elif result.is_error():
            booked = "failed"
            print(result)

        response = Response()
        response.data = {
            "booked" : booked
        }
        return response