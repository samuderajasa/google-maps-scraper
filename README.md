# Google Maps Scraper :round_pushpin:
Extract data from Google Maps database (name, phone number, address, website, rating, coordinates etc) using Places API

## Requirements :memo:
### 1. Python
Make sure you have Python installed as it written in python language.
- You can [download python here](https://www.python.org/downloads/)
- [How to install python](https://www.digitalocean.com/community/tutorials/install-python-windows-10)

### 2. Googlemaps Library
To install googlemaps library, open command line (Powershell/CMD/terminal):

`pip install googlemaps`

src: https://pypi.org/project/googlemaps/

### 3. XlsxWriter Library
To install pandas library, open command line:

`pip install XlsxWriter`

src: https://xlsxwriter.readthedocs.io/getting_started.html

### 4. Google Console
We will use limited free account with $300 in credits. A credit card is still required (you won't be charged if you run out of credits).
1. Go to https://console.cloud.google.com/
2. Sign up if you don't already have a Google account
3. Agree to the TOS and continue
4. Click the 'Select a Project' button in the upper left then click 'New Project' button
![create project 1](assets/create_project_1.png)
![create project 2](assets/create_project_2.png)

5. Fill in the Project Name and Location then click 'Create'
![create project 3](assets/create_project_3.png)

6. Go to 'Credentials' in the left sidebar to create your API Key
![create project 4](assets/create_project_4.png)

7. Click 'Create Credentials' then select 'API Key'
![create project 5](assets/create_project_5.png)

8. The API key will be created. You will need this key in the code
![create project 6](assets/create_project_6.png)

9. Go to 'Library' on the left sidebar, search for 'Places' then enable it
![create project 7](assets/create_project_7.png)
![create project 8](assets/create_project_8.png)

10. You will be directed to the free trial sign-up page, click 'Agree and Continue' then fill in the details. Your Places Library is ready to use with limited free credits.


## How to Use :book:
### 1. Clone this repository
Download [zip file](https://github.com/samuderajasa/google-maps-scraper/archive/refs/heads/master.zip) or using Git `git clone https://github.com/samuderajasa/google-maps-scraper.git`

### 2. Insert your API key
open the main.py file with text editors then insert your API KEY on line 8

`API_KEY = "Insert API KEY here"`

### 3. Insert series of coordinates covering your target area
For accuracy, the code scrapes the area recursively within a 10 km radius of your defined latitude and longitude coordinates. You need to insert your series of coordinates to cover the area. You can obtain the coordinates of your target area from maps.google.com, then right-click on the location and copy the coordinate to line 15.

### 4. Set your search parameter and fields
The code uses a text search. To define your search keyword, write it on line 27 in the 'query' parameter:

`places_result = gmaps.places(location=x, radius=10000, open_now=False, query="your keyword here")`

If you want to use a nearby search based on place type, you can modify line 26 and define your place type in the 'type' parameter:

`places_result = gmaps.places_nearby(location=x, radius=10000, open_now=False, type="travel_agency")`

you can see diffent type of place types here: https://developers.google.com/maps/documentation/places/web-service/supported_types

Define your data fields on line 35

`my_fields = ['name', 'international_phone_number', 'website', 'formatted_address']`

you can see different type of data fields here : https://developers.google.com/maps/documentation/places/web-service/place-data-fields

### 5. Set excel workbook name to save the result
Replace the workbook path on line 77 with the path where you want the result to be saved.

`workbook = xlsxwriter.Workbook(r"D:\Documents\your_search_result.xlsx")`

### 6. Execute the code
After setting up the code, save it, then open the command line.
Run the code with the following command:

`python main.py`

The code will run in background. The result will be stored to the excel workbook you specified in the code.
