# Instructions 

Commerical Truck Trader is the largest US-based e-commerice website for the buying and selling of trucks. The project
'usedTrucksScraper' scrapes Commercial Truck Tarder for used truck data. The output of running the scraper is a 
csv data set. 

## Setting up programming environment

1. You'll need an integrated development environment (IDE) that can run Python code (e.g. Pycharm)
  a. I'll be using Visual Studio Code
    i. Note that this invovles downloading the package 'code-runner'
2. You'll also need to download the following external packages: [zenrows](https://pypi.org/project/zenrows/)
  b. [beautifulSoup](https://pypi.org/project/beautifulsoup4/)


## Adjusting parameters of the scraper

The urls that are in 'createDataSet.py' contain the following search filters: 'Used', 'Class 4 - 8', 'FuelType', 'Newly Listed'
Load the urls onto the browser if you wish to adjust the filters. Once the search filter is updated, do not forget to copy the 
new url and feed it into lines 15 - 22 of 'createDataSet.py'


## Running the program

The root file of the project is 'createDataSet.py'. To run the scraper run the program from this file. 

## Potential issues

Currently, the scraper relies on the third API Zenrows to bypass bot detection. I relied on free trials in order to 
scrape the data. Each free trail allots 20 urls to scrape. If you're running the program with free trials, make sure 
to update the API on line 5 of 'scraper.py' with the new API. 
