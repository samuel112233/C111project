import pandas as pd 
import random
import statistics
import csv
import plotly.figure_factory as ff 
import plotly.graph_objects as go 
df=pd.read_csv('medium_data.csv')
data=df['Math_score'].tolist()
mean=statistics.mean(data)
std=statistics.stdev(data)

def randomSetOfMeans(counter):
    dataSet=[]
    for i in range(0,counter):
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return mean

meanList=[]
for i in range(0,1000):
    setOfMeans=randomSetOfMeans(100)
    meanList.append(setOfMeans)
m1=statistics.mean(meanList)
s1=statistics.stdev(meanList)
print(m1,s1)


fsds,fsde=m1-s1,m1+s1
ssds,ssde=m1-2*s1,m1+2*s1
tsds,tsde=m1-3*s1,m1+3*s1
df=pd.read_csv('data3.csv')
data=df['Math_score'].tolist()
mean=statistics.mean(data)
std=statistics.stdev(data)
fig=ff.create_distplot([meanList],['Student Marks'],show_hist=False)
fig.add_trace(go.Scatter(x=[m1,m1],y=[0,0.17],mode='lines',name='mean'))
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='mean'))
fig.add_trace(go.Scatter(x=[ssde,ssde],y=[0,0.17],mode='lines',name='stdev2end'))
fig.add_trace(go.Scatter(x=[tsde,tsde],y=[0,0.17],mode='lines',name='stdev3end'))
fig.show()
zscore=(mean-m1)/std
print(zscore)
