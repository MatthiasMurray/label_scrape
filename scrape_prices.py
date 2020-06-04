##this script contains a module that obtains price information for preprocessing in sentiment labeling

##Yahoo outlines historical price access steps:

## 1) Go to Yahoo Finance:
##       https://finance.yahoo.com/

## 2) Enter a quote in the search field (top)

## 3) Select a quote in the search results to view it

## 4) Click Historical Data

## 5) Select a Time Period, data to Show, Frequency

## 6) Click Apply

## 7) Click Download Data


##DEPENDENCIES
import time
import selenium
from selenium import webdriver
##END DEPENDENCIES


##PARTS 1-3
def quotepage(tick):
  drivepath = '/usr/local/bin/chromedriver'
  
  driver = webdriver.Chrome(drivepath)
  
  #PART 1
  try:
    driver.get('https://finance.yahoo.com/')
  except:
    time.sleep(1)
    try:
      driver.get('https://finance.yahoo.com/')
    except:
      return 'ERROR: FAIL TO LOAD YAHOO FINANCE HOME. CHECK CONNECTION.'

  #PART 2
  try:
    company_search_box = driver.find_element_by_id('yfin-usr-qry')
    company_search_box.send_keys(tick.upper())
  except:
    time.sleep(1)
    driver.get(driver.getCurrentUrl())
    try:
      company_search_box = driver.find_element_by_id('yfin-usr-qry')
      company_search_box.send_keys(tick.upper())
    except:
      return 'ERROR: FAIL TO SEARCH TICKER. CHECK SYNTAX OR CONNECTION.'
    
