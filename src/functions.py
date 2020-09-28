import requests
import json 
from datetime import date, datetime, timedelta

# Melbourne geological coordinates for api request
lat = -37.814
lon = 144.96332
api_key =  "77c58409917fba6ed7fbe651f700935f"
api_request = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly&units=metric&appid={api_key}")
read_api = json.loads(api_request.text)


def current_uv():
        crt_uv = read_api["current"]["uvi"]
        return crt_uv

def sun_protection():
        """If conditions reflecting uv index ratings according to australian government standards """
        crt_value = current_uv()
        try:  
            if (crt_value <=2):
                return(f"With a UV rating of {crt_value},no sun protection is required - UV level is safe.\n")
            elif (2< crt_value <= 5 ):
                return(f"With a UV rating of {crt_value}, sun protection required - Moderate risk of sun damage from unprotected sun exposure.\n")
            elif (5 < crt_value <=7 ):
                return(f"With a UV rating of {crt_value}, sun protection required - High risk of sun damage.\n")
            elif (7 < crt_value <= 10):
                return(f"With a UV rating of {crt_value}, extra sun-proteciton required - Very high risk of sun damage.\n Minimise sun exposure between 10am and 4pm.\n")
            else: 
                return(f"At {crt_value} UVI, extra sun protection is required - Extreme risk of sun damage.\nEyes and skin can burn in minutes.\n")
        except TypeError:
            return("There was an error with the inputted uv index")

class skin:
    exposure = 200
    uv_index = current_uv()
    b_time = 0

    def __init__(self,name, damage):
        self.name = name
        self.damage = damage
        self.radiation_intensity = (3 * self.uv_index )
        
    def burn_time(self):
        """ calculation for minutes before specific skin type gets sun damage"""
        b_time = (self.exposure * self.damage) // self.radiation_intensity
        return b_time

    @property 
    def minutes_iteration(self):
        """Time to burn changes with the skin type and current uv rating. """
        return ("With today's uv rating, you have " + str(self.burn_time()) + " minutes before sun burn.")

# calling skin class and calculating time before sun burn for each skin type
def skin_type_questions():
    skin1 = skin("skin1",2.5)
    skin2 = skin("skin2", 3)
    skin3 = skin("skin3",4 )
    skin4 = skin("skin4", 5)
    skin5 = skin("skin5",8)
    skin6 = skin("skin6",15)

    skin_type = int(input("""What skin type do you have?\n
    [1] Fair skin, light-coloured hair, always burns and never tans.
    [2] Fair skin, light-colouted hair, often burns, rarely tans.
    [3] Fair to medium skin, light or medium coloured eyes, burns occasionally, sometimes tans.
    [4] Medium or olive (before sun exposure), dark eyes, medium-dark hair, rarely burns, tans often.
    [5] Medium to dark skin, dark eyes, dark hair, almost never burns, always tans.
    [6] deeply pigmented dark skin, almost black eyes, black hair, never burns, always tans darkly.\n""" ))
   
    try: 
        if skin_type == 1:
            print(skin1.minutes_iteration)
        elif skin_type == 2:    
            print(skin2.minutes_iteration)
        elif skin_type ==3:
            print(skin3.minutes_iteration)
        elif skin_type ==4:
            print(skin4.minutes_iteration)
        elif skin_type ==5:
            print(skin5.minutes_iteration)
        elif skin_type ==6: 
            print(skin6.minutes_iteration)
        else: 
            print("No skin type was inputted.")
    except TypeError:
        print("THere has been a type error - change input to integer")

def current_temperature():
    crt_temp = read_api["current"]["temp"]
    crt_feel = read_api["current"]["feels_like"]
    print(f"The current temperature is {crt_temp} but feels like {crt_feel}.")

def forecast_temp():
    """For loop to concatenate forecasted temperature with future dates """
    today = date.today()
    current_day = today
    try: 
        for temperature in read_api["daily"]:
            forecast_temp = temperature["temp"]["max"]
            print(f"The temperature for {current_day} is {forecast_temp} degrees celsius.")
            current_day= current_day + timedelta(days=1) 
    except TypeError:
        return "There is a type error"