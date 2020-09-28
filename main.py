import requests
import json 
from functions import current_uv, skin_type_questions, sun_protection
from datetime import date
from datetime import datetime

#program start
print("Please consider harms of sun damage.")
user_answer=input("Are you intending to leave your home today? y/n\n").lower()

if user_answer == "y":
    print("Then please be mindful of the uv rays.")
    user_check = input("Check UV now? y/n \n").lower()
    current_uv()
    #print skin questionnaire with time to burn here 
    #input temperature for next seven days
    skin_type_questions()
    sun_protection()
else:
    print("Sun protection may not be needed. Take care of yourself today!")