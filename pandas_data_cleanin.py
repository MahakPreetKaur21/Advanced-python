#import library
import pandas as pd
import matplotlib.pyplot as plt

#create dataframe and read csv
df = pd.read_csv(r'C:\Users\mahak\Downloads\data_jobs.csv')

#strip extra spaces in column names
df.columns = df.columns.str.strip()

#data cleanup
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])

#drop rows with all NaN
df_cleaned = df.dropna(how='all')
print(df_cleaned.info())

#fill missing values
df_filled = df.copy()
df_filled['salary_rate'] = df_filled['salary_rate'].fillna(0)
df_filled['salary_year_avg'] = df_filled['salary_year_avg'].fillna(0)
df_filled['salary_hour_avg'] = df_filled['salary_hour_avg'].fillna(0)

#display cleaned data
print(df_filled.iloc[:10, 11:14])
