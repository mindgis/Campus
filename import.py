from sys import argv, exit
import csv
import cs50

db = cs50.SQL("sqlite:///students.db")

# If incorrect usage
if len(argv) != 2:
    print("Usage: python import.py characters.csv")
    exit(1)

# Import tables
with open(argv[1], 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Split names
        names = []
        for parts in row["name"].split(" "):
            names.append(parts)
        # Condition for name length
        if len(names) == 2:
            db.execute("INSERT INTO students (first, last, house, birth) VALUES(?, ?, ?, ?)",
                       names[0], names[1], row["house"], row["birth"])
        elif len(names) == 3:
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                       names[0], names[1], names[2], row["house"], row["birth"])