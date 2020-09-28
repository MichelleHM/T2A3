# Doucmentation for Application
This terminal application aims to give the user information regarding UV rays to increase awareness on the harms of unprotected sun exposure. 

### Input and Output Handling 
The application retrieves data from an API through a get request. The API used is from [One Call](https://openweathermap.org/api/one-call-api?gclid=EAIaIQobChMI-JDk-aKE7AIVZtOWCh0dswvAEAAYASAAEgJCR_D_BwE) and requires parameters to be inserted into the API url to be functional. 

The terminal application uses the following parameters to customise the data retrieved. 
- Latitude 
- Longitude 
- Exclusions
    - Minutely
    - Hourly
- API key 

The geographical coordinates are referred via the inputted latitude and longitude. Based on the coordinates in the terminal application, all called data from the api pertain to Melbourne, Australia. Option to customise the geograghical location is left to discretion of the user. The user can change the given coordinates defined in variables `lat` and `lon` on main.py to their desired location. 

The exclusions in this API are to simplify the output for forecasted dates. In this application, the 

