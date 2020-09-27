# Function for forecasting temperature for next 7 days from the current day. 
def forecast_temp():
    """For loop to concatenate forecasted temperature with future dates """
    today = date.today()
    current_day = today
    try: 
        for temperature in read_api["daily"]:
            forecast_temp = temperature["temp"]["max"]
            print(f"The temperature for {current_day} is {forecast_temp}")
            current_day= current_day +datetime.timedelta(days=1) 
    except TypeError:
        return "There is a type error"

