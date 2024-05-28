import csv
from scraper import scraper


# data sources that will be scraped
urls = [
    {'fuelType': 'Electric', 'url': 'https://www.commercialtrucktrader.com/Used-electric/trucks-for-sale?condition=U&fuelType=electric&sort=create_date%3Adesc&class=CLASS%204%20%28GVW%2014001%20-%2016000%29%7C4%2CCLASS%205%20%28GVW%2016001%20-%2019500%29%7C5%2CCLASS%206%20%28GVW%2019501%20-%2026000%29%7C6%2CCLASS%207%20%28GVW%2026001%20-%2033000%29%7C7%2CCLASS%208%20%28GVW%2033001%20-%20150000%29%20%7C8&page=1'},
    {'fuelType': 'Flex Fuel', 'url': 'https://www.commercialtrucktrader.com/Used-flexFuel/trucks-for-sale?condition=U&fuelType=flexFuel&sort=create_date%3Adesc&class=CLASS%204%20%28GVW%2014001%20-%2016000%29%7C4%2CCLASS%205%20%28GVW%2016001%20-%2019500%29%7C5%2CCLASS%206%20%28GVW%2019501%20-%2026000%29%7C6&page=1'},
    {'fuelType': 'Natural Gas', 'url': 'https://www.commercialtrucktrader.com/Used-naturalGas/trucks-for-sale?condition=U&fuelType=naturalGas&sort=create_date%3Adesc&class=CLASS%205%20%28GVW%2016001%20-%2019500%29%7C5%2CCLASS%204%20%28GVW%2014001%20-%2016000%29%7C4%2CCLASS%206%20%28GVW%2019501%20-%2026000%29%7C6%2CCLASS%207%20%28GVW%2026001%20-%2033000%29%7C7%2CCLASS%208%20%28GVW%2033001%20-%20150000%29%20%7C8&page=1'},
    {'fuelType': 'BioDiesel', 'url': 'https://www.commercialtrucktrader.com/Used-bioDiesel/trucks-for-sale?condition=U&fuelType=bioDiesel&sort=create_date%3Adesc&class=CLASS%205%20%28GVW%2016001%20-%2019500%29%7C5%2CCLASS%204%20%28GVW%2014001%20-%2016000%29%7C4%2CCLASS%206%20%28GVW%2019501%20-%2026000%29%7C6%2CCLASS%207%20%28GVW%2026001%20-%2033000%29%7C7%2CCLASS%208%20%28GVW%2033001%20-%20150000%29%20%7C8&page=1'},
    {'fuelType': 'Diesel', 'url': 'https://www.commercialtrucktrader.com/Used-diesel/trucks-for-sale?condition=U&fuelType=diesel&sort=create_date%3Adesc&class=CLASS%205%20%28GVW%2016001%20-%2019500%29%7C5%2CCLASS%204%20%28GVW%2014001%20-%2016000%29%7C4%2CCLASS%206%20%28GVW%2019501%20-%2026000%29%7C6%2CCLASS%207%20%28GVW%2026001%20-%2033000%29%7C7%2CCLASS%208%20%28GVW%2033001%20-%20150000%29%20%7C8&page=1'},
    {'fuelType': 'Gasoline', 'url': 'https://www.commercialtrucktrader.com/Used-gasoline/trucks-for-sale?condition=U&fuelType=gasoline&sort=create_date%3Adesc&class=CLASS%204%20%28GVW%2014001%20-%2016000%29%7C4%2CCLASS%205%20%28GVW%2016001%20-%2019500%29%7C5%2CCLASS%206%20%28GVW%2019501%20-%2026000%29%7C6%2CCLASS%207%20%28GVW%2026001%20-%2033000%29%7C7%2CCLASS%208%20%28GVW%2033001%20-%20150000%29%20%7C8&page=1'}
]

rows = []
for elem in urls:
    result = scraper(elem['fuelType'], elem['url'])
    rows.extend(result)

# name of csv file
filename = 'usedTrucks.csv'

# defining attributes for the data set
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

