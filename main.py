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

# Accessing fields in api reposnse to retrieve uvi information.
def current_uv():
    crt_uv = read_api["current"]["uvi"]
    return crt_uv

# If conditions reflecting uv index ratings according to australian government standards
def sun_protection(max_uv):
    try:
        if (max_uv <=2):
            print("No sun protection required - UV level is safe.")
        elif (2< max_uv <= 5 ):
                print("Sun protection required - Moderate risk of sun damage from unprotected sun exposure.")
        elif (5 < max_uv <=7 ):
            print("Sun protection required - High risk of sun damage.")
        elif (7 < max_uv <= 10):
            print("Extra sun-proteciton required - Very high risk of sun damage.\n Minimise sun exposure between 10am and 4pm.")
        else: 
            print("Extra sun protection is required - Extreme risk of sun damage.\nEyes and skin can burn in minutes.")
    except TypeError:
        print("There was an error with the inputted uv index")

# Return current temperature and feels-like temperature
def current_temperature():
    crt_temp = read_api["current"]["temp"]
    crt_feel = read_api["current"]["feels_like"]
    print(f"The current temperature is {crt_temp} but feels like {crt_feel}.")
    
def forcast_temperature():
    today = date.today()
    current_day = today
    try: 
        for temperature in read_api["daily"]:
            forecast_temp = temperature["temp"]["max"]
            print(f"The temperature for {current_day} is {forecast_temp}")
            current_day= current_day +datetime.timedelta(days=1) 
    except TypeError:
        return "There is a type error"

# #current date and time
# now = datetime.now()

# now = datetime.now()

# def current_time(self):
#     """Convert datetime into string to retrieve minutes, hours, AM/PM."""
#     print(now.strftime("%I:%M %p"))

# def current_month(self):
#     """Printing current month by using strftime() and formate code %B for displaying month."""
#     print(now.strftime("%B"))  

# def current_day(self):
#     """Print current day with strftime() using code %A. """
#     print(now.strftime("%A"))

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

