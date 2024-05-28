from zenrows import ZenRowsClient
from parseHTML import parse, createRows

def scraper(fuelType, url):
      client = ZenRowsClient("54d5664d8c4bbc3d293484a83f1ed35a56ccee84")
      params = {"js_render":"true","antibot":"true"}
      rows = []
      currentURL = url
      pageNumber = 1
      while True:
            response = client.get(currentURL, params=params)
            arrayOfListings = parse(response.text)
            #edge case where no listings are pulled from the url
            if arrayOfListings == None:
                  break
                  
            pageScraped = createRows(arrayOfListings, fuelType)
            rows.extend(pageScraped)
            #given that Commercial Truck Trader renders 38 listings per page, we can check if we are in the last page of listings
            if len(arrayOfListings) < 38:
                  break 
            #move to next page
            pageNumber += 1
            """ 
            -> Commercial Truck Trader caps searches at the 10th page, even if more listings are available
            -> Because each page has 38 listings, the most listings we can view is 380
            -> If we try to move to a page beyond page 10(for example if we manually update the url to the 11th page '...&page=11'), we'll be redirected to page 10"""
            if pageNumber == 11:
                  break
            currentURL = currentURL[:-1] + str(pageNumber)
      return rows










