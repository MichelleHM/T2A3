import requests
import json 

# Melbourne geological coordinates for api request
lat = -37.814
lon = 144.96332
api_key =  "77c58409917fba6ed7fbe651f700935f"
api_request = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly&units=metric&appid={api_key}")
read_api = json.loads(api_request.text)


def current_uv():
        crt_uv = read_api["current"]["uvi"]
        return crt_uv

def sun_protection(): #how can i get this function to call current uv function for crt_uv
        """If conditions reflecting uv index ratings according to australian government standards """
        crt_value = current_uv()
        try:  
            if (crt_value <=2):
                print("No sun protection required - UV level is safe.")
            elif (2< crt_value <= 5 ):
                print("Sun protection required - Moderate risk of sun damage from unprotected sun exposure.")
            elif (5 < crt_value <=7 ):
                print("Sun protection required - High risk of sun damage.")
            elif (7 < crt_value <= 10):
                print("Extra sun-proteciton required - Very high risk of sun damage.\n Minimise sun exposure between 10am and 4pm.")
            else: 
                print("Extra sun protection is required - Extreme risk of sun damage.\nEyes and skin can burn in minutes.")
        except TypeError:
            print("There was an error with the inputted uv index")

class skin:
    exposure = 200
    uv_index = current_uv()
    radiation_intensity = (3 * uv_index )
    b_time = 0

    def __init__(self,name, damage):
        self.name = name
        self.damage = damage

    def burn_time(self):
        """ calculation for minutes before specific skin type gets sun damage"""
        b_time = (self.exposure * self.damage) // self.radiation_intensity
        return b_time

    @property 
    def minutes_iteration(self):
        """Time to burn changes with the skin type and current uv rating. """
        return ("With today's uv rating, you have " + str(self.burn_time()) + "minutes before sun burn.")

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
    [6] deeply pigmented dark skin, almost black eyes, black hair, never burns, always tans darkly.  """ ))
   
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
