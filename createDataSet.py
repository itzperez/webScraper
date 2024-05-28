import csv
from scraper import scraper

""" 
-> I used Zenrows free trial to scrape these urls 
-> I call the Zenrows api in 'scraper.py' lines 5, 6, 13
-> Free trial only fetches 20 urls
-> I had to create four differnt free trial accounts in order to scrape these urls
-> With the first trial, I scraped the first three urls  while 'BioDiesel', 'Diesel', 'Gasoline' commented out
-> With the second trial, I scraped the fourth url while 'Electric', 'Flex Fuel', 'Natural Gas', 'Diesel', 'Gasoline' commented out 
-> With the third trial, I scraped the fifth url while 'Electric', 'Flex Fuel', 'Natural Gas', & 'BioDiesel' 'Gasoline' commented out
-> With the fourth trial, I scraped the sixth url while 'Electric', 'Flex Fuel', 'Natural Gas', & 'BioDiesel' 'Diesel' commented out
-> When switching trials, the Zenrows API key needs to be updated on 'scraper.py' line 5 """

urls = [
    {'fuelType': 'Electric', 'url': 'https://www.commercialtrucktrader.com/Used-electric/trucks-for-sale?condition=U&fuelType=electric&sort=create_date%3Adesc&class=CLASS%204%20%28GVW%2014001%20-%2016000%29%7C4%2CCLASS%205%20%28GVW%2016001%20-%2019500%29%7C5%2CCLASS%206%20%28GVW%2019501%20-%2026000%29%7C6%2CCLASS%207%20%28GVW%2026001%20-%2033000%29%7C7%2CCLASS%208%20%28GVW%2033001%20-%20150000%29%20%7C8&page=1'},
    # {'fuelType': 'Flex Fuel', 'url': 'https://www.commercialtrucktrader.com/Used-flexFuel/trucks-for-sale?condition=U&fuelType=flexFuel&sort=create_date%3Adesc&class=CLASS%204%20%28GVW%2014001%20-%2016000%29%7C4%2CCLASS%205%20%28GVW%2016001%20-%2019500%29%7C5%2CCLASS%206%20%28GVW%2019501%20-%2026000%29%7C6&page=1'},
    # {'fuelType': 'Natural Gas', 'url': 'https://www.commercialtrucktrader.com/Used-naturalGas/trucks-for-sale?condition=U&fuelType=naturalGas&sort=create_date%3Adesc&class=CLASS%205%20%28GVW%2016001%20-%2019500%29%7C5%2CCLASS%204%20%28GVW%2014001%20-%2016000%29%7C4%2CCLASS%206%20%28GVW%2019501%20-%2026000%29%7C6%2CCLASS%207%20%28GVW%2026001%20-%2033000%29%7C7%2CCLASS%208%20%28GVW%2033001%20-%20150000%29%20%7C8&page=1'},
    # {'fuelType': 'BioDiesel', 'url': 'https://www.commercialtrucktrader.com/Used-bioDiesel/trucks-for-sale?condition=U&fuelType=bioDiesel&sort=create_date%3Adesc&class=CLASS%205%20%28GVW%2016001%20-%2019500%29%7C5%2CCLASS%204%20%28GVW%2014001%20-%2016000%29%7C4%2CCLASS%206%20%28GVW%2019501%20-%2026000%29%7C6%2CCLASS%207%20%28GVW%2026001%20-%2033000%29%7C7%2CCLASS%208%20%28GVW%2033001%20-%20150000%29%20%7C8&page=1'},
    # {'fuelType': 'Diesel', 'url': 'https://www.commercialtrucktrader.com/Used-diesel/trucks-for-sale?condition=U&fuelType=diesel&sort=create_date%3Adesc&class=CLASS%205%20%28GVW%2016001%20-%2019500%29%7C5%2CCLASS%204%20%28GVW%2014001%20-%2016000%29%7C4%2CCLASS%206%20%28GVW%2019501%20-%2026000%29%7C6%2CCLASS%207%20%28GVW%2026001%20-%2033000%29%7C7%2CCLASS%208%20%28GVW%2033001%20-%20150000%29%20%7C8&page=1'},
    # {'fuelType': 'Gasoline', 'url': 'https://www.commercialtrucktrader.com/Used-gasoline/trucks-for-sale?condition=U&fuelType=gasoline&sort=create_date%3Adesc&class=CLASS%204%20%28GVW%2014001%20-%2016000%29%7C4%2CCLASS%205%20%28GVW%2016001%20-%2019500%29%7C5%2CCLASS%206%20%28GVW%2019501%20-%2026000%29%7C6%2CCLASS%207%20%28GVW%2026001%20-%2033000%29%7C7%2CCLASS%208%20%28GVW%2033001%20-%20150000%29%20%7C8&page=1'}
]

rows = []
for elem in urls:
    print('FuelType:', elem['fuelType'])
    print('hi')
    result = scraper(elem['fuelType'], elem['url'])
    rows.extend(result)

#name of csv file
filename = 'usedTrucks.csv'

#IF CREATING DATA SET FOR THE FIRST TIME, (using the first free trial) use lines 31 - 54 and comment out 56 - 58
fields = [
    'id',
    'price',
    'class',
    'make',
    'model',
    'category',
    'year',
    'fuelType',
    'mileage',
    'description',
    'city',
    'state',
    'sellerType',
    'listingDateMonth',
    'listingDateYear',
    'url',
    'timestamp'
]

with open(filename, 'w') as file:
    writerObject = csv.writer(file)
    writerObject.writerow(fields)
    writerObject.writerows(rows)

#IF CONTINUING TO WRITE THE DATA SET, (using the second trial, third trial, fourth trial), comment out lines 31 - 54 and uncomment 56 - 58
# with open(filename, 'a', newline='') as file:
#     writerObject = csv.writer(file)
#     writerObject.writerows(rows)
    
