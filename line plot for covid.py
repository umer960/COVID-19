# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 15:28:15 2020

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

g = sns.lineplot(data=Analysis[['All Cause', 'deaths minus only covid', 'deaths minus total covid']])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
g.set_title('Data Source: Center of Disease Control (CDC)')
g.set_xlabel('Number of Weeks(Continous since 2019-Present)')
g.set_ylabel('Number of deaths per week')
sns.despine(left=True)




