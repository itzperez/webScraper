from bs4 import BeautifulSoup
import json
import re
import datetime


def parse(htmlString):
    soup = BeautifulSoup(htmlString, 'html.parser')
    """ 
    -> within the html file, <script> window.searchData </script is where the listing data is stored (in the form of a dictionary) 
    -> use beautifulSoup to extract this dictionary """
    tag = soup.select_one('#listings')
    tag = tag.select_one('div')
    tag = tag.select_one('script')
    dictionaryAsString = tag.text

    # clean up string in order to convert from string to dict
    dictionaryAsString = dictionaryAsString.replace(' window.searchData = ', '')
    dictionaryAsString = dictionaryAsString.strip()
    dictionaryAsString = dictionaryAsString.replace('filters: {', '"filters": {')

    #json.loads requires keys to be double quotted, currently the following keys are not double quotted
    dictionaryAsString = dictionaryAsString.replace('search: {', '"search": {')
    dictionaryAsString = dictionaryAsString.replace('featured: {', '"featured": {')
    dictionaryAsString = dictionaryAsString.replace('dealerGroupData: [', '"dealerGroupData": [')
    dictionaryAsString = dictionaryAsString.replace('dealerData: [', '"dealerData": [')
    #currently there is an placeholder comma at the end of the dictionary, json.loads needs this removed in order to convert string to dict type
    dictionaryAsString = dictionaryAsString[:-3] + dictionaryAsString[-2:]

    dataDict = json.loads(dictionaryAsString)
    #only need the array of listings
    searchKey = dataDict['search']
    arrayOfListings = searchKey["results"]

    #case where page rendered no results, scraping is over
    if len(arrayOfListings) == 0:
       return None
    return arrayOfListings


def createRows(arrayOfListings, fuelType):
    rows = []
    for listing in arrayOfListings:

      #if price unknown, disregard
      price = listing['price']['raw']
      #Commercial Truck Trader assigns value 0 to listings with unknown price
      if price == 0:
         continue

      #if mileage unknown, disregard
      if 'mileage' in listing:
         mileage = listing['mileage']['raw']
      else: 
         continue
      
      #string in the format 'Month Day Year'
      listingDate = listing['create_date_formatted']['raw']
      listingDateYear = re.search('[\d-]+$', listingDate).group()
      #if listing date more thann 2 years old, disregard
      if int(datetime.date.today().strftime('%Y')) - int(listingDateYear) > 2:
         continue
          
      row = []

      row.append(listing['id']['raw'])
      row.append(price)
      #some attributes are not in the dictionary; check before indexing in order to avoid error
      if 'class_id' in listing:
         row.append(listing['class_id']['raw'])
      else:
         row.append('unknown')

      if 'make_name' in listing:
         row.append(listing['make_name']['raw'][0])
      else: 
         row.append('unknown')
      
      if 'model_name' in listing:
         row.append(listing['model_name']['raw'][0])
      else:
         row.append('unknown')
      if 'category_name' in listing:
         row.append(listing['category_name']['raw'][0])
      else:
         row.append('unknown')     
      if 'year' in listing:
         row.append(listing['year']['raw'])
      else:
         row.append('unknown')

      row.append(fuelType)
      
      row.append(mileage)

      if 'description' in listing:
         description = listing['description']['raw']
         #description strings sometimes have <p> tags; remove in order to improve readability
         if description.startswith('<p>'):
            description = description[3:]
            if description.endswith('<p>'):
               description = description[:-3]
         row.append(description)
      else:
         row.append('unknown')
      if 'city' in listing:
         row.append(listing['city']['raw'])
      else:
         row.append('unknown')
      if 'state_code' in listing:
         row.append(listing['state_code']['raw'])
      else:
         row.append('unknown')
      if 'seller_type' in listing:
         row.append(listing['seller_type']['raw'])
      else: 
         row.append('unknown')
         
      listingDateMonth = re.search('([^\s]+)', listingDate).group()
      row.append(listingDateMonth)
      row.append(listingDateYear)

      row.append(listing['ad_detail_url']['raw'])
      #timestamp of when program is run 
      row.append(datetime.date.today().strftime('%Y-%m-%d'))
      rows.append(row)
    return rows





