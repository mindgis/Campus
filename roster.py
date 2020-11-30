from sys import argv, exit
import csv
import cs50

db = cs50.SQL("sqlite:///students.db")

# If incorrect usage
if len(argv) != 2:
    print("Usage: python import.py house")
    exit(1)

# Query database for all students in house and sort alphabetically by last name, then first name
rows = db.execute("SELECT first, middle, last, birth FROM students WHERE house=? ORDER BY last", argv[1])
# Print out each student's full name and birth year
for row in rows:
    # Condition for number of names
    if row["middle"] == None:
        print(row["first"], row["last"], end="")
        print(", born", row["birth"])
    else:
        print(row["first"], row["middle"], row["last"], end="")
        print(", born", row["birth"])