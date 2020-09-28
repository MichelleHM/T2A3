import main

class uv_index_information():
# Accessing fields in api reposnse to retrieve uvi information.
    @classmethod
    def current_uv():
        crt_uv = read_api["current"]["uvi"]
        return crt_uv

    @classmethod:
    class sun_protection:

def sun_protection(max_uv): #how can i get this function to call current uv function for crt_uv
    """If conditions reflecting uv index ratings according to australian government standards """
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
