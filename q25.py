import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data related to doctors and hospitalizations
file_path = 'rehospitalization.xlsx'

# Load the relevant sheets into DataFrames
doctor_df = pd.read_excel(file_path, sheet_name='hDoctor')
hospitalization_df = pd.read_excel(file_path, sheet_name='hospitalization1')

# Merge the DataFrames on the doctor code
merged_df = pd.merge(doctor_df, hospitalization_df, left_on='קוד רופא', right_on='רופא משחרר-קוד', how='inner')

# Calculate the workload for each doctor (e.g., number of hospitalizations handled)
doctor_workload = merged_df.groupby('קוד רופא').size()

# Add this workload information back to the DataFrame
merged_df['workload'] = merged_df['קוד רופא'].map(doctor_workload)

# Assuming 'Release_Type' or another column in hospitalization_df indicates rehospitalization
sns.scatterplot(x='workload', y='ימי אשפוז', data=merged_df)
plt.title('Relationship between Doctor Workload and Rehospitalization')
plt.xlabel('Doctor Workload')
plt.ylabel('Rehospitalization (Days of Hospitalization)')
plt.show()

# To statistically check the correlation
correlation = merged_df['workload'].corr(merged_df['ימי אשפוז'])
print(f'Correlation between doctor workload and rehospitalization: {correlation}')


# Add screenshot