import numpy as np 
import pandas as pd 

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

data = pd.read_csv('D:\Master\ProgrammingApplications\cars.csv',nrows=10) 
#print(data.head()) 
#print(data['manufacturer_name'].unique()) 
#print(data['location_region'].unique())
#print(data['feature_8'].unique())
#print(data['feature_9'].unique())
#print(data['manufacturer_name'].count())
#print(data['manufacturer_name'].value_counts())

print(pd.get_dummies(data, columns = ['manufacturer_name']))
#print(pd.get_dummies(data, columns = ['model_name']))
#print(pd.get_dummies(data, columns = ['transmission','color']))
#print(pd.get_dummies(data, columns = ['engine_fuel','engine_has_gas','engine_type','body_type']))
#print(pd.get_dummies(data, columns = ['has_warranty','state','drivetrain','is_exchangeable']))
#print(pd.get_dummies(data, columns = ['location_region','up_counter','feature_0','feature_1']))
#print(pd.get_dummies(data, columns = ['feature_2','feature_3','feature_4','feature_5','feature_6']))
#print(pd.get_dummies(data, columns = ['feature_7','feature_8','feature_9'])) 
#data['Remarks'].value_counts() 
