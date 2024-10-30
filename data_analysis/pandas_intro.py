# Pandas Introduction
import pandas as pd

# 1. Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)

# 2. Reading Data from a CSV File
df = pd.read_csv("data.csv")
print(df.head())

# 3. Writing Data to a CSV File
df.to_csv("output.csv", index=False)

# 4. Selecting Columns
ages = df['Age']
print(ages)

# 5. Filtering Rows
adults = df[df['Age'] >= 30]
print(adults)

# 6. Adding a New Column
df['Salary'] = [70000, 80000, 90000]
print(df)

# 7. Dropping a Column
df = df.drop('City', axis=1)
print(df)

# 8. Renaming Columns
df = df.rename(columns={'Name': 'Full Name'})
print(df)

# 9. Handling Missing Values
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
print(df)

# 10. Grouping Data
grouped = df.groupby('Age').mean()
print(grouped)

# 11. Merging DataFrames
df2 = pd.DataFrame({
    'Full Name': ['Alice', 'Bob', 'David'],
    'Location': ['NY', 'CA', 'TX']
})
merged_df = pd.merge(df, df2, on='Full Name', how='inner')
print(merged_df)

# 12. Concatenating DataFrames
concat_df = pd.concat([df, df2], ignore_index=True)
print(concat_df)

# 13. Sorting Data
sorted_df = df.sort_values(by='Age')
print(sorted_df)

# 14. Resetting the Index
df.reset_index(drop=True, inplace=True)
print(df)

# 15. Applying Functions
df['Salary After Tax'] = df['Salary'].apply(lambda x: x * 0.7)
print(df)

# 16. Pivot Tables
pivot_table = df.pivot_table(values='Salary', index='Age', aggfunc='mean')
print(pivot_table)

# 17. String Operations
df['Full Name'] = df['Full Name'].str.upper()
print(df)

# 18. Date and Time Handling
df['Date of Birth'] = pd.to_datetime(['1998-01-01', '1993-05-15', '1988-08-20'])
print(df['Date of Birth'])

# 19. Exporting to Excel
df.to_excel("output.xlsx", index=False)

# 20. Plotting Data (Requires Matplotlib)
import matplotlib.pyplot as plt

df['Age'].plot(kind='bar')
plt.title('Age Distribution')
plt.xlabel('Index')
plt.ylabel('Age')
plt.show()
