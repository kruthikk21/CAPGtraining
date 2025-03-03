import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Paris', 'London']
}

df = pd.DataFrame(data)
print(df)
print(df.head())   # First 5 rows
print(df.tail())   # Last 5 rows
print(df.shape)    # (rows, columns)
print(df.columns)  # Column names
print(df.info())   # Summary of the dataset
print(df.describe())  # Statistical summary


print(df['Name'])        # Selecting a column
print(df[['Name', 'Age']])  # Selecting multiple columns
print(df.iloc[1])        # Selecting a row by index
print(df.loc[0:2])       # Selecting multiple rows


print(df[df['Age'] > 30])  # Rows where Age > 30


df['Salary'] = [50000, 60000, 70000] #adding new column
print(df)

df.drop('Salary', axis=1, inplace=True)#deleting a column
print(df)

df.loc[1, 'Age'] = 32


df.rename(columns={'Name': 'Full Name'}, inplace=True)

