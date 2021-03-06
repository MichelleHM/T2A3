import requests
import json 
from functions import current_uv, skin_type_questions, sun_protection, forecast_temp, current_temperature
from datetime import date
from datetime import datetime

#program start
print("Please consider the harms of sun damage.\n")
user_answer=input("Are you intending to leave your home today? y/n\n").lower()

if user_answer == "y":
    print("Be mindful of the uv rays.")
    user_check = input("Check UV now? y/n \n").lower()
    if user_check == "y":
        skin_type_questions()
        print(sun_protection())
    else:
        exit
    user_temperature = input("Would you like to see the forecasted weather?y/n\n").lower()
    if user_temperature == "y":
        current_temperature()
        forecast_temp()
    else:
        exit
else:
    print("Sun protection may not be needed. Take care of yourself today!")