
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