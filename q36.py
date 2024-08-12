import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Load the GeneralData table into a DataFrame
file_path = 'rehospitalization.xlsx'
general_data_df = pd.read_excel(file_path, sheet_name='GeneralData')

# Select numeric columns for PCA
numeric_columns = general_data_df.select_dtypes(include=['float64', 'int64']).columns
numeric_data = general_data_df[numeric_columns].dropna()

# Standardize the data before applying PCA
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numeric_data)

# Apply PCA
pca = PCA(n_components=2)  # You can adjust the number of components
pca_result = pca.fit_transform(scaled_data)

# Create a DataFrame with the PCA results
pca_df = pd.DataFrame(data=pca_result, columns=['PC1', 'PC2'])

# Plot the explained variance ratio
plt.figure(figsize=(10, 7))
sns.barplot(x=['PC1', 'PC2'], y=pca.explained_variance_ratio_)
plt.title('Explained Variance Ratio by Principal Components')
plt.xlabel('Principal Component')
plt.ylabel('Variance Explained')
plt.show()

# Optionally, add PCA components to the original DataFrame
general_data_df['PC1'] = pca_df['PC1']
general_data_df['PC2'] = pca_df['PC2']

# Display the first few rows of the DataFrame with PCA components
general_data_df.head()
