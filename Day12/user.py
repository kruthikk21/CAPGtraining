import pandas as pd

file = open("./Day12/userinput.csv", 'a+')  # Open file in append+ mode

print("Enter number of employees:")
n = int(input())

data = []

for i in range(n):
    name = input("Enter the name: ")
    age = input("Enter the age: ")
    salary = input("Enter the salary: ")
    data.append([name, age, salary])

# Writing data to file
for i in data:
    file.write(",".join(i) + "\n")  3
    

file.close()  # Close the file

# Reading the CSV file using pandas
df = pd.read_csv("./Day12/userinput.csv", names=['name', 'age', 'salary'])
print(df)
