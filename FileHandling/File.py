#*************************FILE HANDLING*************************************
'''
File handling allows us to:

 Save data permanently
 Read old data later
 Store logs
 Store user records
 Work with CSV and JSON files

This is the foundation for databases.

#1. Opening a File
Syntax:
file = open("filename.txt", "mode")
Example:
file = open("data.txt", "r")

#2. File Modes
| Mode | Meaning      |
| ---- | ------------ |
| r    | Read         |
| w    | Write        |
| a    | Append       |
| x    | Create file  |
| r+   | Read + Write |

#3. Writing to a File
file = open("data.txt", "w")
file.write("Hello World")
file.close()

!!!!!!!!!Important!!!!!!!!!!!!!!1
Mode "w" overwrites existing content.

file = open("data.txt", "w")
file.write("New Data")

#4. Reading a File
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

#5. Reading Line by Line
file = open("data.txt", "r")
for line in file:
    print(line)
file.close()

#6. read(), readline(), readlines()
read()
Reads entire file.
content = file.read()

readline()
Reads one line
line = file.readline()

readlines()
Returns list.
lines = file.readlines()
print(lines)

#7.Append Mode
Instead of deleting old data:
file = open("data.txt", "a")
file.write("\nDeep Learning")
file.close()

#8. Using with
with open("data.txt", "r") as file:
content = file.read()
    print(content)

No need for file.close

#9.Writing Multiple Lines
with open("students.txt", "w") as file:

    file.write("Shreyash\n")
    file.write("Rahul\n")
    file.write("Amit\n")

#10.Exception Handling with Files
try:

    with open("abc.txt", "r") as file:

        print(file.read())

except FileNotFoundError:

    print("File not found")

#11.CSV Files
CSV = Comma Separated Values
name,age,marks
Shreyash,22,90
Rahul,21,85

$$$$$$$$$$$$$$$$$$Writing CSV$$$$$$$$$$$$$$$$$$$$
    import csv

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(
        ["Name", "Age", "Marks"]
    )

    writer.writerow(
        ["Shreyash", 22, 90]
    )


$$$$$$$$$$Reading CSV$$$$$$$$$$$$$$$$

import csv

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:

        print(row)

#12.JSON Files

$$$$$$$$$$$$$$$$$Writing JSON$$$$$$$$$$$$$
import json

student = {
    "name": "Shreyash",
    "age": 22
}

with open(
    "student.json",
    "w"
) as file:

    json.dump(
        student,
        file
    )

$$$$$$$$$$$$$Reading JSON$$$$$$$$$$$$$$
import json

with open(
    "student.json",
    "r"
) as file:

    data = json.load(file)

print(data)

################ MEMORY TRICK #################
| Function    | Purpose                |
| ----------- | ---------------------- |
| read()      | Read whole file        |
| readline()  | Read one line          |
| readlines() | Read all lines as list |
| write()     | Write data             |
| append()    | Add data               |
| json.dump() | Save JSON              |
| json.load() | Read JSON              |

'''