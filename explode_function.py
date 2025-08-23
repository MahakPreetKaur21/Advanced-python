import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\mahak\Downloads\data_jobs.csv')
#explode() - transforms each element of a list-like to a row
#Expand list-like data within a DataFrame column into separate rows.
#Commonly used to split list data into individual rows for analysis (hint hint) or when working with JSON data in a DataFrame.
data = {
    'job_title_short': ['Data Analyst', 'Data Scientist', 'Data Engineer'],
    'job_skills': [['excel', 'sql', 'python'], ['python', 'r'], ['aws', 'python', 'airflow']]
}

df_skills = pd.DataFrame(data)

print(df_skills)
df_exploded = df_skills.explode('job_skills')

print(df_exploded)
print(df_exploded.value_counts('job_skills'))
print(df_exploded.value_counts('job_skills').plot(kind='bar'))
plt.show()