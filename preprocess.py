import pandas as pd
from sklearn.preprocessing import StandardScaler

# Create the dataset
data = pd.read_excel('Data.xlsx')

# Create a DataFrame
df = pd.DataFrame(data)

# View the data
print("Original Data:\n", df)

# Handle missing data (if any)
df.dropna(inplace=True)  # This will remove any rows with missing values

# Convert Bioactivity_Class to binary values (Active = 1, Inactive = 0)
df['Bioactivity_Class'] = df['Bioactivity_Class'].apply(lambda x: 1 if x == 'Active' else 0)

# Select relevant features for model input
X = df[['MolWt', 'TPSA', 'NumHDonors', 'NumHAcceptors', 'LogP']]
y = df['Bioactivity_Class']  # Target variable (Active/Inactive)

# Normalize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create a new DataFrame with scaled features
X_scaled_df = pd.DataFrame(X_scaled, columns=['MolWt', 'TPSA', 'NumHDonors', 'NumHAcceptors', 'LogP'])

# Show preprocessed data
print("\nPreprocessed Features (Scaled):\n", X_scaled_df)
print("\nTarget (Bioactivity Class):\n", y)
