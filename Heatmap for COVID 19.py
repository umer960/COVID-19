# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:37:31 2020

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

weeks_26 = Analysis[Analysis['MMWR Week'] <= 26]
weeks_26_heatmap = weeks_26.pivot_table(index='MMWR Year', columns='MMWR Week', values='All Cause')
f = sns.heatmap(weeks_26_heatmap, alpha=0.9, cmap='coolwarm',lw=1,linecolor='white')
f.set_title('Data Source: Center for Disease Control (Heatmap)')
