import googlemaps
import pprint
import time
import xlsxwriter
import json

#define API key
API_KEY = "Insert API KEY here"

# define our client
gmaps = googlemaps.Client(key=API_KEY)

# search places range
# the example below is a series of coordinates covering the Jabodetabek area in Indonesia. The coordinates are spaced 10 km apart.
locations = ["-6.131844238340605, 107.01095554056478",
             "-6.20423087003785, 107.01483864016667",
             "-6.290116766936734, 107.02163406446992",
             "-6.369235039296276, 107.01095554056478",
             "-6.167556211802376, 107.12550697881981",
             "-6.263098005484488, 107.12162387921795",
             "-6.354763091443407, 107.11385768001422",
    ]
stored_result = []
for x in locations:
    # uncomment line below to use nearby search  
    # places_result = gmaps.places_nearby(location=x, radius=10000, open_now=False, type="travel_agency")
    places_result = gmaps.places(location=x, radius=10000, open_now=False, query="your keyword here")

    #loop each place for details
    for place in places_result['results']:
        #define place id
        my_placeId = place['place_id']

        #define fields
        my_fields = ['name', 'international_phone_number', 'website', 'formatted_address']

        #request for place details
        places_details = gmaps.place(place_id = my_placeId, fields= my_fields)

        stored_result.append(places_details['result'])

    time.sleep(5)

    try:
        token = places_result["next_page_token"]
    except:
        token = None

    #continue to next page
    while token:
        try:
            places_result_next = gmaps.places_nearby(page_token = token)

            for place in places_result_next['results']:
                #define place id
                my_placeId = place['place_id']

                #define fields
                my_fields = ['name', 'international_phone_number', 'website', 'formatted_address']

                #request for place details
                places_details = gmaps.place(place_id = my_placeId, fields= my_fields)

                stored_result.append(places_details['result'])

            time.sleep(5)
            token = places_result_next["next_page_token"]
        except:
            break

#DUMPING VALUES TO EXCEL

# define the headers, that is just the key of each result dictionary.
row_headers = stored_result[0].keys()

# create a new workbook and a new worksheet.
workbook = xlsxwriter.Workbook(r"D:\Documents\query_restaurant_result.xlsx")
worksheet = workbook.add_worksheet()

# populate the header row
col = 0
for header in row_headers:
    worksheet.write(0, col, header)
    col += 1

row = 1
col = 0
# populate the other rows

# get each result from the list.
for result in stored_result:

    # get the values from each result.
    result_values = result.values()

    # loop through each value in the values component.
    for value in result_values:
        worksheet.write(row, col, value)
        col += 1
    
    # make sure to go to the next row & reset the column.
    row += 1
    col = 0

# close the workbook
workbook.close()