import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\mahak\Downloads\data_jobs.csv')
df.columns=df.columns.str.strip()
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
df_in = df[df['job_country'] == 'India'].copy()
df_in['job_posted_month']=df_in['job_posted_date'].dt.strftime('%B')
# extract the month name from 'job_posted_date'
df_in['job_posted_month'] =df_in['job_posted_date'].dt.to_period('M')
df_in_pivot = df_in.pivot_table(index='job_posted_month', columns='job_title_short', aggfunc='size')
df_in=df_in.sort_values('job_posted_month')
print(df_in_pivot)
df_in_pivot.plot(kind='line')
plt.show()
#top 3
top_3 = df_in['job_title_short'].value_counts().head(3)
top_3 = top_3.index.tolist()
print(top_3)
df_in_pivot[top_3].plot(kind='line')
plt.title('Monthly Job Postings for Top Data Jobs in the India')
plt.xlabel('2023')
plt.ylabel('job_count')
plt.legend()
plt.show()