import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the specified path
file_path = 'C:\\Users\\USUARIO\\Documents\\GitHub\\data\\climate_change_impact_on_agriculture_2024.csv'
data = pd.read_csv(file_path, delimiter=',')

# Extract the 'Crop_Type' column
crop_types = data['Crop_Type']

# Generate a histogram of crop types
plt.figure(figsize=(10, 8))
crop_types.value_counts().plot(kind='bar')
plt.title('Histogram of Crop Types')
plt.xlabel('Crop Type')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
