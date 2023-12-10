import numpy as np 
import pandas as pd 

data = pd.read_csv('D:\Master\ProgrammingApplications\cars.csv') 
print(data.head()) 
print(data['manufacturer_name'].unique()) 
print(data['location_region'].unique())
print(data['feature_8'].unique())
print(data['feature_9'].unique())