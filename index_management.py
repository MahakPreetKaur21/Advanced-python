import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv(r'C:\Users\mahak\Downloads\data_jobs.csv')
df.columns=df.columns.str.strip()
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
print(df.index)
print(df.index.dtype)
df.index.name="job_index"
print(df.index.name)
median_pivot = df.pivot_table(values='salary_year_avg', index='job_title_short', aggfunc='median')
print(median_pivot.index.name)
#reset index
df_usa=df[df['job_country']== 'United States']
print(df_usa.head(5))
#print(df_usa.loc[10:20,'job_title_short':'job_country'])
df_usa.reset_index(inplace=True)
print(df_usa.head())
#print(df_usa.loc[:20,'job_title_short':'job_country'])
median_pivot.reset_index(inplace=True)
print(median_pivot)
#set index
median_pivot.set_index('job_title_short', inplace=True)
print(median_pivot)
#sort index
median_pivot.sort_index(inplace=True)
print(median_pivot)