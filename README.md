# COVID-19
#https://healthdata.gov/dataset/weekly-counts-deaths-state-and-select-causes-2019-2020

import numpy as np
import pandas as pd
import seaborn as sns

#THE FILE WAS TAKEN FROM CENTER OF DISEASE CONTROL WEBSITE AS A CSV FILE.  

df = pd.read_csv(r"C:\Users\Umerrr\Downloads\Weekly couns of death by states.csv")

#A NEW CALCULATED FIELD WAS CREATED FROM THE DATA USING THE FOLLOWING CODE

df['deaths minus multiple cause covid']= df['All Cause']-df['COVID-19 (U071, Multiple Cause of Death)']
df['deaths minus total covid']= df['All Cause']-df['COVID-19 (U071, Multiple Cause of Death)']-df['COVID-19 (U071, Underlying Cause of Death)']

#THE DATA WAS GROUPED BY YEAR AND WEEKS TO CACULATE THE IMPACT OF COVID CASES ON TOTAL CASES

Analysis = df.groupby(['MMWR Year', 'MMWR Week']).sum()[['All Cause','deaths minus multiple cause covid', 'deaths minus total covid']]



