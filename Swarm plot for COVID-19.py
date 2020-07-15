# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:08:57 2020

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

sns.swarmplot(size=11,x='MMWR Year',y='deaths minus only covid', data= Analysis, color='red', alpha=0.4, label='All without Covid')
g = sns.swarmplot(size=11,x='MMWR Year',y='All Cause', data= Analysis, color='Blue', alpha=0.4, label='All')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.despine(left=True)
g.set_title('Data Source: Center of Disease Control')