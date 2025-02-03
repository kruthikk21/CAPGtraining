import csv

# Data to be written
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "London"]
]

# Open the CSV file in write mode
with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    # Writing data to the file
    writer.writerows(data)  # Writes multiple rows

