# COVID-19

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


#IT WAS THEN PLOTTED WITH A SIMPLE LINE PLOT

Analysis.plot.line()

#THEN WE ANALYZE THE TOP 10 STATES IF THE HAVE TOTAL DEATHS GOING UP OR DOWN WITH OR WITHOUT COVID

State_wise = df.groupby('Jurisdiction of Occurrence')[['All Cause','deaths minus multiple cause covid', 'deaths minus total covid']].mean().sort_values('All Cause', ascending = False)
State_wise = State_wise.reset_index()
top_10 = State_wise[1:11]

#WE WILL THEM RUN SCATTER PLOT TO SEE IF THE TOP 10 STATES EFFECTTED HAD A SIGNIFICANT CHANGE IN DEATH RATES BECAUSE OF COVID OR NOT

#IMPORTANT!! THE BELOW CODE IS COMMENTTED OUT. IN ORDER TO MAKE IT WORK WE WOULD NE TO COMMENT OUT 'ANALYSIS.PLOT.LINE() OTHERWISE THAT IS ALSO PLOTTED ON THE SAME GRAPH.

#sns.scatterplot(x='Jurisdiction of Occurrence',y='All Cause', data= top_10, color='blue', alpha=0.3)
#sns.scatterplot(x='Jurisdiction of Occurrence',y='deaths minus total covid', data= top_10, color='red', alpha=0.3)
#sns.scatterplot(x='Jurisdiction of Occurrence',y='deaths minus multiple cause covid', data= top_10, color='green', alpha=0.3)

#OUR FINAL ANALYSIS INCLUDE RESETTING THE INDEX COLUMN FOR ANALYSIS TABLE. THIS WILL MAKE THE 'MMWR YEAR' AS A SEPERATE COLUMN AND WE CAN USE IT IN OUR ANALYSIS
#WE WILL BE PLOTTING BOXPLOTS TO SEE HOW DIFFERENT THE DEATH TALLY IS WITH AND WITHOUT COVID AS COMPARED TO 2019.

#Analysis = Analysis.reset_index()
#sns.boxplot(x='MMWR Year',y='All Cause', data= Analysis, color='blue')
#sns.boxplot(x='MMWR Year',y='deaths minus multiple cause covid', data= Analysis, color='red')
