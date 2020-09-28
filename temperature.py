class 

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
