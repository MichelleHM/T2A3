from uv_info import current_uv

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





    # @staticmethod
    # def skin_types():
    #     """Calcualtion for each skin type's burn time.
        
    #      Multiplying damage factor with exposure and dividing with current radiation intensity."""
    #     skin1 = skin("skin1",2.5)
    #     skin2 = skin("skin2", 3)
    #     skin3 = skin("skin",4 )
    #     skin4 = skin("skin", 5)
    #     skin5 = skin("skin",8)
    #     skin6 = skin("skin",15)
        
        
        
        # def minute_iteration(self):
        # #i need to make a printe statement to iterate how many minutes before sunburn
        # return f"With today's uv rating, you have {self.name.burn_time()} minutes before sun damage occurs."


# skin_type = input("""What skin type do you have?\n
# [1] Fair skin, light-coloured hair, always burns and never tans.
# [2] Fair skin, light-colouted hair, often burns, rarely tans.
# [3] Fair to medium skin, light or medium coloured eyes, burns occasionally, sometimes tans.
# [4] Medium or olive (before sun exposure), dark eyes, medium-dark hair, rarely burns, tans often.
# [5] Medium to dark skin, dark eyes, dark hair, almost never burns, always tans.
# [6] deeply pigmented dark skin, almost black eyes, black hair, never burns, always tans darkly.  """ )

# if 

# skin1 = skin("skin1",2.5)
# skin2 = skin("skin2", 3)
# skin3 = skin("skin3",4 )
# skin4 = skin("skin4", 5)
# skin5 = skin("skin5",8)
# skin6 = skin("skin6",15)

# print("With today's uv rating, you have " + str(skin1.burn_time()) + " minutes before sun burn.")
# print(skin2.burn_time)
# # print()