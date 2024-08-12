import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Open the Excel file
file_path = 'rehospitalization.xlsx'

# Load the GeneralData table into a DataFrame
general_data_df = pd.read_excel(file_path, sheet_name='GeneralData')

# Display basic information about the DataFrame
general_data_info = general_data_df.info()

# Display summary statistics for the DataFrame
general_data_description = general_data_df.describe()

# Plot histograms for each numeric column in the DataFrame
numeric_columns = general_data_df.select_dtypes(include='number').columns

# Set up the matplotlib figure
plt.figure(figsize=(20, 15))

for i, column in enumerate(numeric_columns, 1):
    plt.subplot(5, 4, i)
    sns.histplot(general_data_df[column], kde=True)
    plt.title(f'Histogram of {column}')

plt.tight_layout()
plt.show()

# Display correlation heatmap
plt.figure(figsize=(15, 10))
correlation_matrix = general_data_df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

general_data_info, general_data_description


## Add screenshot
