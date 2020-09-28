from functions import skin, sun_protection
import unittest 
from unittest.mock import patch
class TestFunctions(unittest.TestCase):
    
    def test_burn(self):
        skin.uv_index = 1
        skin_test = skin("skin1",1)
        result = skin_test.burn_time()
        expectation = 66
        self.assertEqual(result, expectation)

    @patch("functions.current_uv")
    def test_sun_protection(self, current_uv):
        current_uv.side_effect = [1,4,10]
        result = sun_protection()
        self.assertEqual(result,"With a UV rating of 1,no sun protection is required - UV level is safe.\n")
        result = sun_protection()
        self.assertEqual(result,"With a UV rating of 4, sun protection required - Moderate risk of sun damage from unprotected sun exposure.\n")
        result = sun_protection()
        self.assertEqual(result,"With a UV rating of 10, extra sun-proteciton required - Very high risk of sun damage.\n Minimise sun exposure between 10am and 4pm.\n")
