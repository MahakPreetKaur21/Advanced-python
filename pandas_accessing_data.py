#import library
import pandas as pd
import matplotlib.pyplot as plt
#create dataframe and read csf
df=pd.read_csv(r'C:\Users\mahak\Downloads\data_jobs.csv')
#data cleanup
df['job_posted_date']=pd.to_datetime(df['job_posted_date'])
#print(df.head())
#iloc() for withut lables
#print(df.iloc[0:5])
#print(df.iloc[0:5,0:6])

print(df.loc[10:20,'job_title_short':'job_work_from_home'])
