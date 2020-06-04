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
  
  #IF SUCCESSFUL, NO NEED TO SElECT A QUOTE.
  #CURRENTLY FAILS IF NOT AUTOMATICALLY DIRECTED TO A QUOTE
  try:
    search_but = driver.find_element_by_id('header-desktop-search-button')
    search_but.click()
  except:
    time.sleep(1)
    try:
      search_but = driver.find_element_by_id('header-desktop-search-button')
      search_but.click()
      quote_url = driver.getCurrentUrl()
      if not ('quote' in quote_url):
        return 'ERROR: POSSIBLE INVALID QUOTE. CHECK CONNECTION OR SYNTAX -- YAHOO DID NOT AUTOMATICALLY RECOGNIZE QUOTE'
    except:
      return 'ERROR: FAILED TO CLICK SEARCH BUTTON. CHECK CONNECTION OR SYNTAX.'

  return driver

##PARTS 4-6
def setdates(dr,start='2015-01-01',end='2020-06-03'):
  
  #PART 4: Enter dates
  try:
    startdatebox = dr.find_element_by_name('startDate')
    startdatebox.send_keys(start)
  except:
    return 'ERROR: FAILED TO SET START DATE'
  
  try:
    enddatebox = dr.find_element_by_name('endDate')
    enddatebox.send_keys(end)
  except:
    return 'ERROR: FAILED TO SET END DATE'


  #PART 5: LAZY APPROACH: SHOULD BE DAILY/HISTORICAL BY DEFAULT. SKIP TO PART 6...
  
  #PART 6: CLICK APPLY
  try:
    apply_but = driver.find_elements_by_tag_name('button')[5]
    apply_but.click()
  except:
    return 'ERROR: FAILURE TO APPLY DATES/PREFS. CHECK CONNECTION/SYNTAX'
  
  time.sleep(1)
    

  #PART 7: CLICK DOWNLOAD
  try:
    downl_but = driver.find_elements_by_tag_name('svg')
    downl_but.click()
  except:
    return 'ERROR: FAILURE TO DOWNLOAD'
