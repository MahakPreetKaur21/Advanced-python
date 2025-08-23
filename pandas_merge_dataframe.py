import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\mahak\Downloads\data_jobs.csv')
df.columns=df.columns.str.strip()
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
# create two dataframes
job_data={ 'job_id':[1,2,3,4,5],
          'job_title':['Data Scientist', 'Software Engineer', 'Product Manager', 'Marketing Director', 'HR Manager'],
          'company_name': ['Google', 'Microsoft', 'Apple', 'Nike', 'Starbucks'],
          'job_location': ['Mountain View, CA', 'Redmond, WA', 'Cupertino, CA', 'Beaverton, OR', 'Seattle, WA']
}

company_data = {
    'company_name': ['Google', 'Microsoft', 'Apple', 'Nike', 'Starbucks'],
    'industry': ['Technology', 'Technology', 'Technology', 'Apparel', 'Food & Beverage'],
    'company_size': ['100,000+', '100,000+', '100,000+', '75,000+', '346,000+']
}

df_jobs=pd.DataFrame(job_data)
df_companies=pd.DataFrame(company_data)
print(df_jobs)
print(df_companies)

#merge(): Combine DataFrames based on common columns or indices, similar to SQL joins (inner, outer, left, right).
#It merges rows from the DataFrame based on the specific keys.

df_job_company = df_jobs.merge(df_companies, on='company_name')

print(df_job_company)
