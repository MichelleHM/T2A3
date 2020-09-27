from forecast import forecast_temp
from py import current_uv
from skin_type import skin_type_questions


print("Please consider .")
user_answer=input("Are you intending to leave your home today? y/n\n").lower()

if user_answer == "y":
    print("Then please be mindful of the uv rays.")
    user_check = input("Check UV now? y/n \n").lower()
    current_uv()
    # skin_type_questions()

else:
    print("Sun protection may not be needed. Take care of yourself today!")
