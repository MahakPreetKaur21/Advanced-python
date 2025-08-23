import pandas as pd
import matplotlib.pyplot as plt
import os
df=pd.read_csv(r'C:\Users\mahak\Downloads\data_jobs.csv')
df.columns=df.columns.str.strip()
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
#concat(): Combine DataFrames by rows (axis = 0) or columns (axis=1).
#Sticks the DataFrames together without using any keys.
# Sample dataset of job postings in January
job_postings_jan = pd.DataFrame({
    'job_id': [1, 2, 3, 4, 5],
    'job_title': ['Data Scientist', 'Data Analyst', 'Machine Learning Engineer', 'Data Scientist', 'Data Engineer'],
    'company': ['Company A', 'Company B', 'Company C', 'Company D', 'Company E'],
    'job_posted_date': pd.to_datetime(['2024-01-02', '2024-01-07', '2024-01-14', '2024-01-19', '2024-01-24'])
})

print(job_postings_jan)
# Sample dataset of job postings in February
job_postings_feb = pd.DataFrame({
    'job_id': [6, 7, 8, 9, 10],
    'job_title': ['Data Scientist', 'Data Analyst', 'Machine Learning Engineer', 'Data Scientist', 'Data Engineer'],
    'company': ['Company F', 'Company G', 'Company H', 'Company I', 'Company J'],
    'job_posted_date': pd.to_datetime(['2024-02-05', '2024-02-09', '2024-02-12', '2024-02-18', '2024-02-22'])
})
print(job_postings_feb)
job_combine_postings=pd.concat([job_postings_jan,job_postings_feb],ignore_index=True)
print(job_combine_postings)


df['job_posted_month'] = df['job_posted_date'].dt.strftime('%b')
# make data frame for each month using a loop
month=df['job_posted_month'].unique()
dict_months= {}
for month in month:
    dict_months[month] = df[df['job_posted_month'] == month]
print(type(dict_months))
print(dict_months['Jan'])
quarter_1 = [dict_months['Jan'], dict_months['Feb'], dict_months['Mar']]

df_q1 = pd.concat(quarter_1, ignore_index=True)

print(df_q1)

#Inspecting to confirm.
df_q1['job_posted_month'].value_counts().plot(kind='bar')
plt.show()

df_q1.to_csv('quater_1.csv')
print(df_q1)
print("File saved at:", os.path.abspath('quater_1.csv'))
