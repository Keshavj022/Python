import csv
import json

# Writing to a text file
try:
    with open("example.txt", "w") as file:
        file.write("Hello, World!\n")
        file.write("This is a new line.\n")
except IOError as e:
    print(f"An error occurred while writing to the file: {e}")

# Reading from a text file
try:
    with open("example.txt", "r") as file:
        content = file.read()
        print("Text file content:")
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")

# Writing to a CSV file
try:
    with open("data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "City"])
        writer.writerow(["Alice", 30, "New York"])
        writer.writerow(["Bob", 25, "Los Angeles"])
except IOError as e:
    print(f"An error occurred while writing to the CSV file: {e}")

# Reading from a CSV file
try:
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        print("CSV file content:")
        for row in reader:
            print(row)
except FileNotFoundError:
    print("Error: The file does not exist.")

# Writing to a JSON file
data = {"name": "Alice", "age": 30, "city": "New York"}
try:
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
except IOError as e:
    print(f"An error occurred while writing to the JSON file: {e}")

# Reading from a JSON file
try:
    with open("data.json", "r") as file:
        data = json.load(file)
        print("JSON file content:")
        print(data)
except FileNotFoundError:
    print("Error: The file does not exist.")