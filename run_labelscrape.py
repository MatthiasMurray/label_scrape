##THIS APPROACH IS DEPRECATED/SLATED FOR REMOVAL.
##PULLING DATA FROM YFINANCE API DIRECTLY IS MORE
##EFFICIENT. HAVE TO CHECK THAT YFINANCE APPROACH
##IS ACCEPTABLE FOR COMMERCIAL APPLICATIONS.

from scrape_prices import *
import sys

tick = sys.argv[1]
vers = int(sys.argv[2])

if vers == 1:
  qp = quotepage(tick)
  
  if type(qp)==str:
    print(qp)

  sd = setdates(qp)

  if type(sd)==str:
    print(sd)
  else:
    print('Check downloads for '+tick.upper()+'.csv')

elif vers == 2:
  qp = fastquote(tick)
  fastfinish(qp) 
