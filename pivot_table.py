#import library
import pandas as pd
import matplotlib.pyplot as plt

#create dataframe and read csv
df = pd.read_csv(r'C:\Users\mahak\Downloads\data_jobs.csv')

#strip extra spaces in column names
df.columns = df.columns.str.strip()

#data cleanup
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
#Country & Job Title Analysis
print(df.pivot_table(
    values='salary_year_avg',
    index=['job_country', 'job_title_short'],
    aggfunc={'salary_year_avg': ['min', 'max', 'median']}
))

#Pivoting Countries and Job Title's Median Salary

df_job_country_salary = df.pivot_table(
    values='salary_year_avg',        # The data to aggregate
    index='job_country',             # Rows (index of pivot table)
    columns='job_title_short',       # Columns (pivot table headers)
    aggfunc='median'                 # Aggregation function
)

print(df_job_country_salary)


top_countries = df['job_country'].value_counts().head(6).index

# filter df_job_country_salary for top 6 countries
df_job_country_salary = df_job_country_salary.loc[top_countries]

# filter df_job_country_salary for list of 6 job titles
job_titles = ['Data Analyst', 'Data Engineer', 'Data Scientist'] # 'Senior Data Analyst', 'Senior Data Engineer', 'Senior Data Scientist']
df_job_country_salary = df_job_country_salary[job_titles]

df_job_country_salary.plot(kind='bar')
plt.ylabel('Median Salary ($USD)')
plt.xlabel('')
plt.title('Median Salary by Country and Job Title')  
plt.xticks(rotation=45, ha='right')
plt.show()