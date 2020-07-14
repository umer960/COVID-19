# COVID-19

import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv(r"C:\Users\Umerrr\Downloads\Weekly couns of death by states.csv")


df['deaths minus multiple cause covid']= df['All Cause']-df['COVID-19 (U071, Multiple Cause of Death)']



df['deaths minus total covid']= df['All Cause']-df['COVID-19 (U071, Multiple Cause of Death)']-df['COVID-19 (U071, Underlying Cause of Death)']


Analysis = df.groupby(['MMWR Year', 'MMWR Week']).sum()[['All Cause','deaths minus multiple cause covid', 'deaths minus total covid']]



Analysis.plot.line()



State_wise = df.groupby('Jurisdiction of Occurrence')[['All Cause','deaths minus multiple cause covid', 'deaths minus total covid']].mean().sort_values('All Cause', ascending = False)


State_wise = State_wise.reset_index()

top_10 = State_wise[1:11]



#sns.boxplot(x='MMWR Year',y='All Cause', data= Analysis, color='blue')
#sns.boxplot(x='MMWR Year',y='deaths minus multiple cause covid', data= Analysis, color='red')
