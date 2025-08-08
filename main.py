import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('hospital_records.csv')

# Convert dates
df['Admission_Date'] = pd.to_datetime(df['Admission_Date'])
df['Discharge_Date'] = pd.to_datetime(df['Discharge_Date'])

# 1. Gender distribution
df['Gender'].value_counts().plot(kind='bar', title='Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# 2. Age distribution
df['Age'].plot(kind='hist', bins=10, title='Age Distribution')
plt.xlabel('Age')
plt.show()

# 3. Patients per Department
df['Department'].value_counts().plot(kind='bar', title='Patients per Department')
plt.xlabel('Department')
plt.ylabel('Number of Patients')
plt.xticks(rotation=45)
plt.show()

# 4. Diagnosis Frequency
df['Diagnosis'].value_counts().plot(kind='bar', title='Diagnosis Frequency')
plt.xlabel('Diagnosis')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# 5. Treatment Types
df['Treatment'].value_counts().plot(kind='pie', autopct='%1.1f%%', title='Treatment Types')
plt.ylabel('')
plt.show()

# 6. Outcomes Distribution
df['Outcome'].value_counts().plot(kind='bar', title='Patient Outcomes')
plt.xlabel('Outcome')
plt.ylabel('Count')
plt.show()

# 7. Payment Methods
df['Payment_Method'].value_counts().plot(kind='pie', autopct='%1.1f%%', title='Payment Methods')
plt.ylabel('')
plt.show()

# 8. Average Bill per Department
df.groupby('Department')['Bill_Amount'].mean().sort_values().plot(kind='barh', title='Average Bill per Department')
plt.xlabel('Average Bill Amount')
plt.show()

# 9. Length of Stay
df['Length_of_Stay'] = (df['Discharge_Date'] - df['Admission_Date']).dt.days
df['Length_of_Stay'].plot(kind='hist', bins=15, title='Length of Stay Distribution')
plt.xlabel('Days')
plt.show()
