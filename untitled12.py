# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 15:28:15 2020

@author: Umerrr
"""

import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv(r"C:\Users\Umerrr\Downloads\Weekly couns of death by states.csv")


df['deaths minus multiple cause covid']= df['All Cause']-df['COVID-19 (U071, Multiple Cause of Death)']



df['deaths minus total covid']= df['All Cause']-df['COVID-19 (U071, Multiple Cause of Death)']-df['COVID-19 (U071, Underlying Cause of Death)']


Analysis = df.groupby(['MMWR Year', 'MMWR Week']).sum()[['All Cause','deaths minus multiple cause covid', 'deaths minus total covid']]



#Analysis.plot.line()

#Analysis = Analysis.reset_index()

State_wise = df.groupby('Jurisdiction of Occurrence')[['All Cause','deaths minus multiple cause covid', 'deaths minus total covid']].mean().sort_values('All Cause', ascending = False)


State_wise = State_wise.reset_index()

top_10 = State_wise[1:11]

sns.scatterplot(x='Jurisdiction of Occurrence',y='All Cause', data= top_10, color='blue', alpha=0.3)
sns.scatterplot(x='Jurisdiction of Occurrence',y='deaths minus total covid', data= top_10, color='red', alpha=0.3)
sns.scatterplot(x='Jurisdiction of Occurrence',y='deaths minus multiple cause covid', data= top_10, color='green', alpha=0.3)


#sns.boxplot(x='MMWR Year',y='All Cause', data= Analysis, color='blue')
#sns.boxplot(x='MMWR Year',y='deaths minus multiple cause covid', data= Analysis, color='red')




