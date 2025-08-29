'''
# TaxiFareModel front
'''
import streamlit as st

'''
# Taxifare Model
### We are going to predict your fare amount :
'''

''''''
''''''
'''
Choose your parameters :
'''

date=st.date_input('Choose a date : ')
time=st.time_input('Chosse a time : ')
pickup_longitude=st.number_input('Choose a pickup longitude : ')
pickup_latitude=st.number_input('Choose a pickup latitude : ')
dropoff_longitude=st.number_input('Choose a dropoff longitude : ')
dropoff_latitude=st.number_input('Choose a dropoff latitude : ')
passenger_count=int(st.number_input('Choose the number of passengers : '))
import datetime
pickup_datetime=datetime.datetime.combine(date,time)
url = 'https://taxifare.lewagon.ai/predict'

params = {'pickup_datetime':pickup_datetime,
          'pickup_longitude' : pickup_longitude,
          'pickup_latitude' : pickup_latitude,
          'dropoff_longitude' : dropoff_longitude,
          'dropoff_latitude' : dropoff_latitude,
          'passenger_count' : passenger_count
          }

import requests
response=requests.get(url,params=params,timeout=20)
predictions=response.json()
prediction=predictions['fare']
st.write('We are predicting your fare amount will be around ', round(prediction,2),'dollars')
