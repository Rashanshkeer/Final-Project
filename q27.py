import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the relevant sheets into DataFrames
file_path = 'rehospitalization.xlsx'
general_data_df = pd.read_excel(file_path, sheet_name='GeneralData')
hospitalization_df = pd.read_excel(file_path, sheet_name='hospitalization1')

# Merge the data on 'Patient' column
merged_df = pd.merge(general_data_df, hospitalization_df, on='Patient', how='inner')

# Identify rehospitalization based on time difference between admissions
merged_df['rehospitalization'] = merged_df.groupby('Patient')['Admission_Entry_Date'].diff().dt.days < 30

# Pairplot to visualize the relationships between weight, height, BMI, and rehospitalization
sns.pairplot(merged_df, vars=['משקל', 'גובה', 'BMI'], hue='rehospitalization')
plt.suptitle('Relationship between Weight, Height, BMI, and Rehospitalization', y=1.02)
plt.show()

# Correlation matrix to check the statistical relationship
correlation_matrix = merged_df[['משקל', 'גובה', 'BMI', 'rehospitalization']].corr()
print("Correlation matrix:\n", correlation_matrix)

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap between Weight, Height, BMI, and Rehospitalization')
plt.show()
