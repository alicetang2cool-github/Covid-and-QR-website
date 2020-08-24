import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')
import pandas as pd
import datetime
import os 
import pickle

rawList = ['https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv', 
           'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv']

USconfirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv', header=0)
allstates = USconfirmed['Province_State'] 
states_unique = set(allstates)
for a in states_unique:
    isState = USconfirmed['Province_State'] == a
    data = {}
    data[a] = USconfirmed[isState]
    TS = data[a].iloc[:,11:].sum(axis=0) #find sum of all countieshin 
    Days = pd.to_datetime(list(TS.keys()),format="%m/%d/%y") #make date into correct date list
    Y = TS.tolist()  #make cases into list
    today = datetime.date.today()  #plotting starts
    plt.plot(Days,Y)
    plt.xticks(rotation=45) 
    plt.xlim([datetime.date(2020,3,1), today])
    plt.title("{} State COVID-19 Cases".format(a))
    plt.xlabel('Time')
    plt.ylabel('Number of total Confirmed Case') #plotting ends
    plt.tight_layout()
    plt.savefig('imageOfCases/{}.png'.format(a)) # replace this with a full path
    plt.clf()

myPlace = "Los Angeles"
ismyplace = USconfirmed['Admin2'] == myPlace
data = {}
data[myPlace] = USconfirmed[ismyplace]
TS = data[myPlace].iloc[:,11:].sum(axis=0)
Days = pd.to_datetime(list(TS.keys()),format="%m/%d/%y") #make date into correct date list
Y = TS.tolist()  #make cases into list
today = datetime.date.today()  #plotting starts
plt.plot(Days,Y)
plt.xticks(rotation=45) 
plt.xlim([datetime.date(2020,3,1), today])
plt.title("{} State COVID-19 Cases".format(myPlace))
plt.xlabel('Time')
plt.ylabel('Number of total Confirmed Cases') #plotting ends
plt.savefig('imageOfCases/{}.png'.format(myPlace)) # replace this with a full path
plt.clf()



USconfirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv', header=0)
allstates = USconfirmed['Province_State'] 
states_unique = set(allstates)
for a in states_unique:
    isState = USconfirmed['Province_State'] == a
    data = {}
    data[a] = USconfirmed[isState]
    TS = data[a].iloc[:,12:].sum(axis=0) #find sum of all counties
    Days = pd.to_datetime(list(TS.keys()),format="%m/%d/%y") #make date into correct date list
    Y = TS.tolist()  #make cases into list
    today = datetime.date.today()  #plotting starts
    plt.plot(Days,Y)
    plt.xticks(rotation=45) 
    plt.xlim([datetime.date(2020,3,1), today])
    plt.title("{} State COVID-19 Deaths".format(a))
    plt.xlabel('Time')
    plt.ylabel('Number of total Confirmed Deaths') #plotting ends
    plt.savefig('imageOfDeaths/{}.png'.format(a)) # replace this with a full path
    plt.clf()


myPlace = "Los Angeles"
ismyplace = USconfirmed['Admin2'] == myPlace
data = {}
data[myPlace] = USconfirmed[ismyplace]
TS = data[myPlace].iloc[:,12:].sum(axis=0)
Days = pd.to_datetime(list(TS.keys()),format="%m/%d/%y") #make date into correct date list
Y = TS.tolist()  #make cases into list
today = datetime.date.today()  #plotting starts
plt.plot(Days,Y)
plt.xticks(rotation=45) 
plt.xlim([datetime.date(2020,3,1), today])
plt.title("{} State COVID-19 Deaths".format(myPlace))
plt.xlabel('Time')
plt.ylabel('Number of total Confirmed Deaths') #plotting ends
plt.savefig('imageOfDeaths/{}.png'.format(myPlace)) # replace this with a full path
plt.clf()


