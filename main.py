import requests
import json 
from forecast import forecast_temp
import skin_type
from datetime import date
from datetime import datetime

# Melbourne geological coordinates for api request
lat = -37.814
lon = 144.96332
api_key =  "77c58409917fba6ed7fbe651f700935f"
api_request = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly&units=metric&appid={api_key}")
read_api = json.loads(api_request.text)

#program start
print("Please consider harms of sun damage.")
user_answer=input("Are you intending to leave your home today? y/n\n").lower()

if user_answer == "y":
    print("Then please be mindful of the uv rays.")
    user_check = input("Check UV now? y/n \n").lower()
    current_uv()
    #print skin questionnaire with time to burn here 
    print(skin_type.skin_type_questions())
else:
    print("Sun protection may not be needed. Take care of yourself today!")



 # print(f"The max UV rating for today is {crt_uv}.")

