import pandas as pd
import matplotlib.pyplot as plt
#create dataframe and read csf
df=pd.read_csv(r'C:\Users\mahak\Downloads\data_jobs.csv')
# example 1
def inflation(salary):
    return salary * 1.03

df['salary_year_inflated'] = df['salary_year_avg'].apply(inflation)

print(df[pd.notna(df['salary_year_avg'])][['salary_year_avg', 'salary_year_inflated']])

# example 2
def projected_salary(row):
    if 'Senior' in row['job_title_short']:
        return  1.05 * row['salary_year_avg']
    else:
        return  1.03 * row['salary_year_avg']

df['salary_year_inflated'] = df.apply(projected_salary, axis=1)

print(df[pd.notna(df['salary_year_avg'])][['job_title_short', 'salary_year_avg', 'salary_year_inflated']])

