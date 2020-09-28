# UV INDEX AWARENESS 
A terminal app for everyday sun care and awareness! 

# Description 
This application retrieves data from [One Call API](https://openweathermap.org/api/one-call-api?gclid=EAIaIQobChMI-JDk-aKE7AIVZtOWCh0dswvAEAAYASAAEgJCR_D_BwE) for localised uv and temperature reports. 

The application currently holds geographical coordinates for only ***Melbourne, Australia***. All the forecasts and output from this application will therefore be catered for this location. 

![Geographical Coordinates](/img/geographical_coordinates.PNG)

In the future, i hope to add more customisable features for users to access uv and temperature information from other locations. 

---
# What the application ACTUALLY does 
The application allows users to view the max uv rating for the current day.

Users are then prompted to choose a skin type based on [Fitzgerald's skin phototype](https://www.arpansa.gov.au/sites/default/files/legacy/pubs/RadiationProtection/FitzpatrickSkinType.pdf). This selection is stored and used to calculate how long the user has before experiencing sun burn and a warning is given based on the UV index. 

![Skin Types](/img/skintype.PNG)

Lastly, a weather forecast is available for the next 7 days. 

---
# UVI Calculation 
The application has a feature which calculates the amount of time before sun damage occurs based on the user's skin type and the current daily uv rating. 

The calculation of this uv rating is based on Fitzgerald's skin phototypes and uses the following formula. 

```
time before burning (minutes) = (exposure * damage) // radiation_intensity
Where,
exposure = 200 
damage = value differs between each skin type
radiation intensity = 3 * uv 
```
Damage scores are dependant on the user's skin type. For example, a person with skin type 1, will typically be have fair skin, light-coloured hair and almost always burns. This skin type will have a damage value of **2.5** as ooposed to a skin type 5 with a value of 8. 

***The lower the damage value, the less time the user will be able to spend in the sun before sun damage occurs.*** 

This estimated time is based on no sun protection, meaning if the user were to wear sunscreen, the time before sun damage will increase. 

--- 
# Installation
## Dependencies
These items are found within requirements.txt

- certifi == 2020.6.20
- chardet == 3.0.4
- idna == 2.10
- requests == 2.24.0
- urllib3 == 1.25.10

**Certifi** is used for `requests` to  validate the trustworthinss of ssl certficates. 

**Chardet** detects Python2 or 3. 

**Idna** is a protocol that standardises translations to ascii which allows programs to display every known alphabet.

**requests** allows the program to access information from the internet. 

**urllib3** is a HTTP library that assists requests.  

---

## Setup
**Step 1**

**Create a virtual environment** in your coding workspace that has access to the *Python* language. Run the following in your terminal.

- This step installs the required dependencies to run this application
```
pip install -r requirements.txt
```

**Step 2**

**Run** the application
```
python src/main.py
```

---
# Testing
Automated testing was created to check the application's consistency in producing accurate results and general functionality.

The two tests are for the uv calculations mentioned above and skin type analysis output. All variables were held constant including the damage variable which is typically based on a changing uv index. 

Holding the damage variable constant by assigning a static numerical value to it allows for consistent testing. This is because the result of the test will not change no matter when or where you test the program. By doing so, we can be assured the program is functioning properly as the test results will be the same each time. 

The second test also holds the uv variable constant by assigning a static numerical value. The same principle applies to this test which leads to a more trustworthy test.  






