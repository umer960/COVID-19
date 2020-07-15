# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 14:52:10 2020

@author: Umerrr
"""



import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Umerrr\Downloads\Weekly couns of death by states.csv")


df['deaths minus only covid']= df['All Cause']-df['COVID-19 (U071, Underlying Cause of Death)']



df['deaths minus total covid']= df['All Cause']-df['COVID-19 (U071, Multiple Cause of Death)']-df['COVID-19 (U071, Underlying Cause of Death)']


Analysis = df.groupby(['MMWR Year', 'MMWR Week']).sum()[['All Cause','deaths minus only covid', 'deaths minus total covid']]

Analysis = Analysis.reset_index()


State_wise = df.groupby('Jurisdiction of Occurrence')[['All Cause','deaths minus only covid', 'deaths minus total covid', 'MMWR Year']].mean().sort_values('All Cause', ascending = False)
State_wise = State_wise.reset_index()
top_10 = State_wise[1:11]

sns.scatterplot(x='Jurisdiction of Occurrence',y='All Cause', data= top_10, color='blue', alpha=0.7, label='All', s=300)
sns.scatterplot(x='Jurisdiction of Occurrence',y='deaths minus total covid', data= top_10, color='red', alpha=0.6, label='Without All COVID-19 Cases (only/multiple)', s=300 )
ty = sns.scatterplot(x='Jurisdiction of Occurrence',y='deaths minus only covid', data= top_10, color='green', alpha=0.7, label= 'Without COVID only Disease', s=300)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
fig=plt.gcf()
fig.set_size_inches(13,5)
sns.despine(left=True)
ty.set_title('Data Source: Center of Disease Control')
ty.set_ylabel('Number of deaths')


#sns.swarmplot(size=11,x='MMWR Year',y='deaths minus only covid', data= Analysis, color='red', alpha=0.4, label='All without Covid')
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

#weeks_26 = Analysis[Analysis['MMWR Week'] <= 26]
#weeks_26_heatmap = weeks_26.pivot_table(index='MMWR Year', columns='MMWR Week', values='All Cause')
#f = sns.heatmap(weeks_26_heatmap, alpha=0.9, cmap='coolwarm', lw=1)
#f.set_title('Heat Map')

