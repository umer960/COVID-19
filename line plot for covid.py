# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 15:28:15 2020

@author: Umerrr
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#https://healthdata.gov/dataset/weekly-counts-deaths-state-and-select-causes-2019-2020

df = pd.read_csv(r"C:\Users\Umerrr\Downloads\Weekly couns of death by states.csv")


df['deaths minus only covid']= df['All Cause']-df['COVID-19 (U071, Underlying Cause of Death)']



df['deaths minus total covid']= df['All Cause']-df['COVID-19 (U071, Multiple Cause of Death)']-df['COVID-19 (U071, Underlying Cause of Death)']


Analysis = df.groupby(['MMWR Year', 'MMWR Week']).sum()[['All Cause','deaths minus only covid', 'deaths minus total covid']]

Analysis = Analysis.reset_index()

Analysis['MMWR Year']= Analysis['MMWR Year'].apply(str)
Analysis['MMWR Week']=Analysis['MMWR Week'].apply(str)


Analysis['Year_Week'] = Analysis[['MMWR Year', 'MMWR Week']].agg('-'.join, axis=1)


sns.lineplot(data=Analysis, x='Year_Week', y='All Cause', label='All')
sns.lineplot(data=Analysis, x='Year_Week', y='deaths minus only covid', label= "deaths without 'only COVID'")
g = sns.lineplot(data=Analysis, x='Year_Week', y='deaths minus total covid', label= 'deaths without any COVID')

g.set(xticklabels=[])

#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
g.set_title('Data Source: Center of Disease Control (CDC)')
g.set_xlabel('Sum of Cases by weeks since January, 2019 - Present')
g.set_ylabel('Number of deaths per week')
sns.despine(left=True)
fig=plt.gcf()
fig.set_size_inches(12,5)




