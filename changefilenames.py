#For inserting label information into the filenames for each SEC filing

#DEPENDENCIES
from useapi import *
from label_filename import *
import numpy as np
import os
import shutil
import pandas as pd
#END DEPENDENCIES

def highestmonth(x):
  date = ''.join(x.split('-'))
  year = int(date[:4])
  month = int(date[4:6])
 
  if np.mod(month,3)==0:
    out = month-3
  else:
    out = month-np.mod(month,3)

  if out == 0:
    year -= 1
    return [year,12]
  else:
    return [year,out]

pathmain = '/Users/Matthias/Documents/LexisNexis/SEC_10qs/scraped_files'

os.chdir(pathmain)

folds = ['Technology','HealthCare','ConsumerServices','ConsumerDurables','CapitalGoods','nan','Finance','Miscellaneous','ConsumerNonDurables','PublicUtilities','BasicIndustries','Transportation','Energy']

hm = highestmonth(str(pd.datetime.now())[:10])

for folder in folds:
  foldpath = pathmain+'/'+folder
  
  os.chdir(foldpath)

  for f in os.listdir(foldpath):
    
    step1 = f.split('_')
    year = int(step1[1][:4])
    month = int(step1[1][4:6])
    if year <= hm[0] and month <= hm[1]:
      newf = label_fileName(f)
    else:
      newf = f[:-4]+'_THISQ.xml'
    shutil.copy(foldpath+'/'+f,foldpath+'/'+newf)
